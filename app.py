from flask import Flask, request, jsonify, render_template
from flask_cors import CORS
from marshmallow import Schema, fields, ValidationError
import os
import uuid
import time
import requests
from dotenv import load_dotenv
import warnings

# LangChain imports
from langchain_google_genai import GoogleGenerativeAIEmbeddings
from langchain_community.chat_message_histories import ChatMessageHistory
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_text_splitters import RecursiveCharacterTextSplitter

# Optional OpenAI fallback
try:
    from langchain_openai import ChatOpenAI
except Exception:
    ChatOpenAI = None

# Load environment variables
load_dotenv()
warnings.filterwarnings('ignore')

app = Flask(__name__)
CORS(app, resources={r"/api/*": {"origins": "*"}})

# Environment variables
NVIDIA_API_KEY = os.getenv("NVIDIA_API_KEY")
OPENROUTER_API_KEY = os.getenv("OPENROUTER_API_KEY")
GOOGLE_API_KEY = os.getenv("GOOGLE_API_KEY")
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
GITHUB_PER_PAGE = 25

# Request schema
class ChatRequestSchema(Schema):
    conversation_id = fields.Str(required=True)
    question = fields.Str(required=True)
    use_realtime = fields.Bool(missing=True)

# Core chat handling class
class OpenSourceChat:
    def __init__(self):
        # Embeddings (Google)
        try:
            self.embeddings = GoogleGenerativeAIEmbeddings(
                model="models/embedding-001",
                google_api_key=GOOGLE_API_KEY,
            )
        except Exception:
            self.embeddings = None

        # LLM – try NVIDIA first, then Google, then OpenAI fallback, then dummy
        self.llm = None
        
        # Try NVIDIA first
        if NVIDIA_API_KEY and not self.llm:
            try:
                from langchain_nvidia_ai_endpoints import ChatNVIDIA
                self.llm = ChatNVIDIA(
                    model="meta/llama-3.1-8b-instruct",
                    api_key=NVIDIA_API_KEY,
                    temperature=0.7,
                )
                print("[OK] Using NVIDIA LLM")
            except Exception as e:
                print(f"NVIDIA LLM init error: {e}")
        
        # Try Google Gemini as fallback
        if GOOGLE_API_KEY and not self.llm:
            try:
                from langchain_google_genai import ChatGoogleGenerativeAI
                self.llm = ChatGoogleGenerativeAI(
                    model="gemini-1.5-pro",
                    google_api_key=GOOGLE_API_KEY,
                    temperature=0.7,
                )
                print("[OK] Using Google Gemini LLM")
            except Exception as e:
                print(f"Google LLM init error: {e}")

        # Try OpenAI as second fallback
        if ChatOpenAI and OPENAI_API_KEY and not self.llm:
            try:
                self.llm = ChatOpenAI(
                    model="gpt-4o-mini",
                    api_key=OPENAI_API_KEY,
                    temperature=0.7,
                )
                print("[OK] Using OpenAI LLM")
            except Exception as e:
                print(f"OpenAI LLM init error: {e}")

        # Final fallback - dummy LLM
        if not self.llm:
            class DummyLLM:
                def invoke(self, _):
                    return "I cannot answer because no language model API key is configured."
            self.llm = DummyLLM()
            print("[WARNING] Using Dummy LLM (no valid API keys)")

        # Helpers
        self.text_splitter = RecursiveCharacterTextSplitter(
            chunk_size=1000,
            chunk_overlap=200,
            length_function=len,
        )
        self.message_history = ChatMessageHistory()
        self.vectorstore = None
        self.user_preferences = {
            "languages": [],
            "interests": [],
            "previous_repos": [],
            "skill_level": "beginner",
            "last_queries": [],
            "preferences_updated": {},
        }

    # GitHub repository search
    def search_repositories(self, query: str = "", language: str = "", force_refresh: bool = False):
        if not query and not language:
            return []
        search_query = query
        if language:
            search_query += f" language:{language}"
        url = f"https://api.github.com/search/repositories?q={search_query}&sort=stars&order=desc&per_page={GITHUB_PER_PAGE}"
        headers = {"Authorization": f"token {GITHUB_TOKEN}"} if GITHUB_TOKEN else {}
        try:
            response = requests.get(url, headers=headers)
            if response.status_code == 200:
                items = response.json().get("items", [])
                return [{
                    "name": item["full_name"],
                    "description": item["description"],
                    "stars": item["stargazers_count"],
                    "language": item["language"],
                    "url": item["html_url"],
                    "open_issues_count": item["open_issues_count"],
                } for item in items]
            return []
        except Exception as e:
            print(f"GitHub Search Error: {e}")
            return []

    # Main response generation
    def get_response(self, question: str, use_realtime: bool = True, force_refresh: bool = False):
        if not self.llm:
            return {"answer": "I'm unable to connect to the language model. Please check server configuration."}
        # Contextual repo search for recommendation‑type queries
        context_data = {}
        lower_q = question.lower()
        if any(word in lower_q for word in ["find", "search", "recommend", "show"]):
            language = None
            for lang in ["python", "javascript", "typescript", "rust", "go", "java", "c++"]:
                if lang in lower_q:
                    language = lang
                    break
            query = (
                question.replace("find", "")
                .replace("search", "")
                .replace("projects", "")
                .replace("repos", "")
                .strip()
            )
            repos = self.search_repositories(query, language)
            context_data["repositories"] = repos
        # Build prompt with optional repo list
        repo_context = ""
        if context_data.get("repositories"):
            repo_list = "\n".join(
                [
                    f"- {r['name']}: {r['description']} ({r['stars']} ⭐)"
                    for r in context_data["repositories"][:5]
                ]
            )
            repo_context = f"\n\nHere are some repositories you might like:\n{repo_list}\n"
        
        prompt = ChatPromptTemplate.from_messages(
            [
                (
                    "system",
                    "You are an expert Open Source Assistant. Provide concise, helpful answers. Use any provided repository context.",
                ),
                ("user", f"Question: {question}{repo_context}"),
            ]
        )
        
        # Handle both real LLMs and DummyLLM
        try:
            chain = prompt | self.llm | StrOutputParser()
            answer = chain.invoke({})
        except Exception as e:
            # Fallback: try direct invocation for DummyLLM or other simple LLMs
            try:
                response = self.llm.invoke(f"Question: {question}{repo_context}")
                # Check if response is a string or has a content attribute
                if isinstance(response, str):
                    answer = response
                elif hasattr(response, 'content'):
                    answer = response.content
                else:
                    answer = str(response)
            except Exception as inner_e:
                answer = f"Error generating response: {str(inner_e)}"
        return {"answer": answer, "context_data": context_data}

    # Stub methods for future expansion
    def initialize_vectorstore(self, curated_data: list = None):
        pass

    def search_issues(self, repo_full_name: str, force_refresh: bool = False):
        return []

    def get_contribution_guide(self, repo_full_name: str, force_refresh: bool = False):
        return ""

    def get_project_insights(self, repo_full_name: str, force_refresh: bool = False):
        return {}

    def crawl_for_open_source_info(self, topic: str = None, language: str = None):
        return []

    def get_stackoverflow_questions(self, repo_name: str = None, topic: str = None):
        return []

# Instantiate chat handler
chat_instance = OpenSourceChat()

# Routes
@app.route("/start-conversation", methods=["POST"])
def start_conversation_route():
    try:
        conversation_id = str(uuid.uuid4())
        return jsonify({"status": "success", "conversation_id": conversation_id})
    except Exception as e:
        return jsonify({"error": "Error starting conversation", "details": str(e)}), 500

@app.route("/api/chat", methods=["POST"])
def chat_route():
    try:
        data = request.get_json()
        schema = ChatRequestSchema()
        validated = schema.load(data)
        answer = chat_instance.get_response(
            question=validated["question"],
            use_realtime=validated.get("use_realtime", True),
        )
        return jsonify(answer)
    except ValidationError as ve:
        return jsonify({"error": "Invalid request", "details": ve.messages}), 400
    except Exception as e:
        return jsonify({"error": "Chat error", "details": str(e)}), 500

@app.route("/api/reset", methods=["POST"])
def reset_route():
    try:
        # In a real app with database, we would clear the conversation history here
        # For now, we just acknowledge the reset
        return jsonify({"status": "success", "message": "Conversation reset"})
    except Exception as e:
        return jsonify({"error": "Reset error", "details": str(e)}), 500

# Minimal additional routes (optional but kept for compatibility)
@app.route("/api/search", methods=["GET"])
def search_repositories_route():
    try:
        query = request.args.get("query", "")
        language = request.args.get("language", "")
        force_refresh = request.args.get("force_refresh", "false").lower() == "true"
        start_time = time.time()
        repos = chat_instance.search_repositories(query, language, force_refresh)
        return jsonify({"repositories": repos, "processing_time": round(time.time() - start_time, 2)})
    except Exception as e:
        return jsonify({"error": "Search error", "details": str(e)}), 500

@app.route("/", methods=["GET"])
def index():
    return render_template("index.html")

if __name__ == "__main__":
    port = int(os.getenv("PORT", 5000))
    app.run(host="0.0.0.0", port=port, debug=True)

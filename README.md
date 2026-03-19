# Open Source Assistant 🚀

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent AI-powered assistant designed to help developers discover, understand, and contribute to open source projects. Built with Flask, LangChain, and multiple LLM providers including **NVIDIA NIM (Llama 3.1)**, Google Gemini, and OpenAI.

## ✨ Current Features

### 🤖 Intelligent Conversational AI
- **Natural Language Understanding**: Ask questions about open source in plain English
- **Context-Aware Responses**: Powered by state-of-the-art language models
- **Multi-Model Support**: NVIDIA NIM (primary), with fallbacks to Google Gemini and OpenAI
- **Flexible Architecture**: Graceful degradation if API keys are unavailable

### 🔍 GitHub Integration
- **Repository Search**: Find projects by keywords and programming language
- **Smart Filtering**: Sort by stars, language, and relevance
- **Live Data**: Direct integration with GitHub API
- **Contextual Recommendations**: Get repository suggestions within conversations

### 💬 Interactive Chat Interface
- **Modern Web UI**: Clean, responsive design with dark theme
- **Real-time Responses**: Fast AI-powered answers
- **Conversation Management**: Reset and start new conversations
- **Quick Actions**: Pre-built buttons for common queries (Beginner Guide, Python, JavaScript, Node.js, MySQL, React Issues)

## 🏗️ Architecture

```
┌─────────────────┐
│   Frontend      │
│  (HTML/CSS/JS)  │
└────────┬────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│   Flask API     │◄────►│   LangChain      │
│    (app.py)     │      │   Integration    │
└────────┬────────┘      └──────────────────┘
         │
         ├──────────────┬──────────────┐
         ▼              ▼              ▼
  ┌────────────┐ ┌────────────┐ ┌──────────┐
  │  GitHub    │ │  NVIDIA    │ │   LLM    │
  │    API     │ │    NIM     │ │ Fallback │
  └────────────┘ └────────────┘ └──────────┘
```  └────────────┘ └────────────┘ └──────────┘ └──────────┘
```

## 🚀 Getting Started

### Prerequisites
- Python 3.8 or higher
- pip package manager
- GitHub Personal Access Token (required)
- At least one LLM API key (NVIDIA, Google, or OpenAI)

### Installation

**1. Clone the repository**
```bash
git clone https://github.com/pshreyas77/open-source-assistant.git
cd open-source-assistant
```

**2. Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\\Scripts\\activate

# On macOS/Linux
source venv/bin/activate
```

**3. Install dependencies**
```bash
pip install -r requirements.txt
```

**4. Set up environment variables**

Create a `.env` file in the root directory:

```env
# NVIDIA NIM API Key (Primary LLM Provider)
NVIDIA_API_KEY=your_nvidia_api_key_here

# Google API Key (Fallback LLM + Embeddings)
GOOGLE_API_KEY=your_google_api_key_here

# OpenAI API Key (Secondary Fallback)
OPENAI_API_KEY=your_openai_api_key_here

# OpenRouter API Key (Alternative Provider)
OPENROUTER_API_KEY=your_openrouter_api_key_here

# GitHub Personal Access Token (Required)
GITHUB_TOKEN=your_github_personal_access_token_here
```

**Getting API Keys:**
- **NVIDIA API**: Visit [NVIDIA NIM](https://build.nvidia.com/explore) and create a free account
- **Google API**: Get your key from [Google AI Studio](https://makersuite.google.com/app/apikey)
- **OpenAI API**: Sign up at [OpenAI Platform](https://platform.openai.com/api-keys)
- **GitHub Token**: Go to GitHub Settings → Developer Settings → Personal Access Tokens → Generate new token (classic)
  - Required scopes: `public_repo`, `read:org`, `read:user`

**5. Run the application**
```bash
python app.py
```

The application will start on `http://localhost:5000`

## 📖 Usage

### Web Interface

Navigate to `http://localhost:5000` in your browser and start asking questions:

- "Find beginner-friendly Python projects"
- "Show me JavaScript web development repositories"
- "Recommend projects for machine learning"
- "How do I make my first pull request?"

### API Endpoints

#### Start Conversation
```http
POST /start-conversation
```
Returns a unique conversation ID.

#### Chat
```http
POST /api/chat
Content-Type: application/json

{
  "conversation_id": "unique-id",
  "question": "Find Python projects for beginners",
  "use_realtime": true
}
```

#### Search Repositories
```http
GET /api/search?query=machine+learning&language=python
```

#### Reset Conversation
```http
POST /api/reset
```

## 🛠️ Technologies Used

### Backend Framework
- **Flask 3.1.0**: Lightweight web framework
- **Flask-CORS**: Cross-origin resource sharing support

### AI & Machine Learning
- **LangChain**: Framework for building LLM applications
- **NVIDIA NIM (Llama 3.1)**: Primary language model
- **Google Gemini**: Fallback LLM and embeddings provider
- **OpenAI GPT**: Secondary fallback option
- **Google Generative AI**: Embeddings (infrastructure ready)

### Data & Validation
- **Requests**: HTTP library for API calls
- **Marshmallow**: Object serialization and validation
- **Pydantic**: Data validation using Python type annotations
- **Python-dotenv**: Environment variable management

### Additional Infrastructure
- **FAISS**: Vector similarity search (infrastructure ready)
- **SQLAlchemy**: Database toolkit (infrastructure ready)
- **Gunicorn**: Production WSGI server for deployment

## 📁 Project Structure

```
open-source-assistant/
├── app.py                 # Main Flask application and API routes
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .env.example          # Environment variables template
├── .gitignore            # Git ignore rules
├── Procfile              # Deployment configuration
├── static/               # Static assets (CSS, JS)
│   ├── styles.css
│   └── script.js
├── templates/            # HTML templates
│   └── index.html        # Main web interface
└── README.md             # This file
```

## 🎯 How It Works

### LLM Provider Chain
The application tries LLM providers in this order:
1. **NVIDIA NIM** (Llama 3.1) - If `NVIDIA_API_KEY` is set
2. **Google Gemini** (gemini-1.5-flash) - If `GOOGLE_API_KEY` is set
3. **OpenAI** (gpt-4o-mini) - If `OPENAI_API_KEY` is set
4. **Dummy LLM** - Returns error message if no keys configured

### Repository Search
When you ask questions like "Find Python projects":
1. System detects search intent from your query
2. Extracts programming language if mentioned
3. Calls GitHub API to search repositories
4. LLM uses this context to provide intelligent recommendations
5. Returns top 5 results with descriptions and star counts

## 🤝 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes**
4. **Commit with clear messages**
   ```bash
   git commit -m "Add amazing feature"
   ```
5. **Push to your fork**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request**

### Development Setup
```bash
# Install dev dependencies
pip install -r requirements.txt

# Run with debug mode
export FLASK_ENV=development
python app.py
```

### Code Style
- Follow PEP 8 guidelines
- Use meaningful variable names
- Add docstrings to functions
- Comment complex logic

## 🚧 Roadmap & Planned Features

The following features are planned for future releases:

### Phase 1: Enhanced Search & Discovery
- [ ] Issue search by repository
- [ ] Contribution guide fetching (CONTRIBUTING.md)
- [ ] Project insights (commit frequency, PR merge rates)
- [ ] Beginner-friendly issue filtering

### Phase 2: RAG & Knowledge Base
- [ ] FAISS vector store implementation
- [ ] RAG pipeline for context-enhanced responses
- [ ] Curated knowledge base of contribution workflows
- [ ] Semantic search capabilities

### Phase 3: Multi-Source Data
- [ ] Web crawling (DEV.to, Reddit, RSS feeds)
- [ ] Stack Overflow integration
- [ ] Trending projects aggregation
- [ ] Community health scores

### Phase 4: Advanced Features
- [ ] Smart caching system (repository, issue, guide caches)
- [ ] User preference learning
- [ ] Persistent storage (PostgreSQL/MongoDB)
- [ ] User authentication and personalized dashboards
- [ ] GitLab and Bitbucket support
- [ ] Discord/Slack bot integration
- [ ] Multi-language support (i18n)
- [ ] Code review assistance
- [ ] PR template generation

## 🐛 Known Limitations

- **GitHub API Rate Limits**: Free tier allows 5,000 requests/hour (authenticated), 60/hour (unauthenticated)
- **LLM API Quotas**: Each provider has their own rate limits and quotas
- **No Persistence**: Conversations are not stored between sessions
- **Basic Search**: Currently only searches repositories by keyword and language

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Shreyas P**
- GitHub: [@pshreyas77](https://github.com/pshreyas77)
- Project Link: [https://github.com/pshreyas77/open-source-assistant](https://github.com/pshreyas77/open-source-assistant)
- Live Demo: [open-source-assistant.onrender.com](https://open-source-assistant.onrender.com/)

## 🙏 Acknowledgments

- [NVIDIA NIM](https://build.nvidia.com/) for providing powerful AI capabilities
- [LangChain](https://www.langchain.com/) for the excellent LLM framework
- [GitHub API](https://docs.github.com/en/rest) for comprehensive repository data
- [Google Gemini](https://ai.google.dev/) for AI capabilities
- [OpenAI](https://openai.com/) for GPT models
- Open source community for inspiration and support

## 📞 Support

If you encounter any issues or have questions:
1. Check the [Issues](https://github.com/pshreyas77/open-source-assistant/issues) page
2. Create a new issue with detailed information
3. Reach out via GitHub Discussions

## ⭐ Star This Project

If you find this project useful, please consider giving it a star! It helps others discover the project.


## Changelog

- **v0.2.0**: Added support for multiple LLM providers and enhanced conversation context
- **v0.1.0**: Initial release with core repository search and filtering features

---

**Made with ❤️ for the open source community**

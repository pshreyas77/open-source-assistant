# Open Source Assistant 🚀

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![Flask](https://img.shields.io/badge/Flask-3.1.0-green.svg)](https://flask.palletsprojects.com/)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)

An intelligent AI-powered assistant designed to help developers discover, understand, and contribute to open source projects. Built with cutting-edge technologies including Google Gemini AI, LangChain, and advanced RAG (Retrieval-Augmented Generation) capabilities.

## ✨ Features

### 🤖 Intelligent Conversational AI
- **Natural Language Understanding**: Ask questions about open source in plain English
- **Context-Aware Responses**: Remembers conversation history and user preferences
- **Personalized Recommendations**: Learns from your interests, programming languages, and skill level

### 🔍 Real-Time Data Integration
- **GitHub API Integration**: Live search for repositories, issues, and contribution guides
- **Web Crawling**: Aggregates trending projects from GitHub, DEV.to, Reddit, and RSS feeds
- **Stack Overflow Integration**: Finds relevant Q&A for repositories and topics
- **Smart Caching**: Intelligent caching system to reduce API calls and improve performance

### 🎯 Project Discovery
- **Smart Repository Search**: Find projects matching your skills and interests
- **Issue Finder**: Discover beginner-friendly issues labeled "good first issue" or "help wanted"
- **Project Insights**: Get detailed statistics on commit frequency, PR merge rates, and community health
- **Contribution Guides**: Automatically fetches and summarizes CONTRIBUTING.md files

### 📊 Advanced Analytics
- **Community Health Scores**: Evaluate project maintainability and responsiveness
- **Technology Stack Analysis**: See what languages and frameworks projects use
- **Activity Metrics**: Track commit frequency and PR response times
- **Contributor Information**: View top contributors and their contribution counts

### 🧠 Machine Learning Powered
- **Vector Store (FAISS)**: Semantic search through curated open source knowledge
- **Multi-Model Support**: Google Gemini AI with fallback to FastEmbed for embeddings
- **RAG Pipeline**: Context-enhanced responses using LangChain
- **Preference Learning**: Automatically extracts and learns from user queries

## 🏗️ Architecture

```
┌─────────────────┐
│   Frontend      │
│  (Templates)    │
└────────┬────────┘
         │
         ▼
┌─────────────────┐      ┌──────────────────┐
│   Flask API     │◄────►│  LangChain       │
│   (app.py)      │      │  RAG Pipeline    │
└────────┬────────┘      └──────────────────┘
         │
         ├──────────────┬──────────────┬──────────────┐
         ▼              ▼              ▼              ▼
┌────────────┐  ┌────────────┐  ┌──────────┐  ┌──────────┐
│  GitHub    │  │   Google   │  │  FAISS   │  │   Web    │
│    API     │  │  Gemini AI │  │  Vector  │  │ Crawlers │
└────────────┘  └────────────┘  └──────────┘  └──────────┘
```

## 🚀 Getting Started

### Prerequisites

- Python 3.8 or higher
- pip package manager
- GitHub Personal Access Token
- Google Gemini API Key

### Installation

1. **Clone the repository**
```bash
git clone https://github.com/pshreyas77/open-source-assistant.git
cd open-source-assistant
```

2. **Create a virtual environment** (recommended)
```bash
python -m venv venv

# On Windows
venv\Scripts\activate

# On macOS/Linux
source venv/bin/activate
```

3. **Install dependencies**
```bash
pip install -r requirements.txt
```

4. **Set up environment variables**

Create a `.env` file in the root directory:
```env
GOOGLE_API_KEY=your_google_gemini_api_key_here
GITHUB_TOKEN=your_github_personal_access_token_here
```

**Getting API Keys:**
- **Google Gemini API**: Visit [Google AI Studio](https://makersuite.google.com/app/apikey)
- **GitHub Token**: Go to GitHub Settings → Developer Settings → Personal Access Tokens → Generate new token (classic)
  - Required scopes: `public_repo`, `read:org`, `read:user`

5. **Run the application**
```bash
python app.py
```

The application will start on `http://localhost:5000`

## 📖 Usage

### Web Interface

Navigate to `http://localhost:5000` in your browser and start asking questions:

**Example Queries:**
- "Find me beginner-friendly Python projects for web development"
- "What are the trending machine learning repositories this week?"
- "Show me issues in tensorflow/tensorflow for beginners"
- "How do I contribute to the React project?"
- "Give me insights about the kubernetes/kubernetes repository"

### API Endpoints

The assistant provides a comprehensive REST API:

#### Chat Endpoint
```bash
POST /api/chat
Content-Type: application/json

{
  "conversation_id": "unique-id",
  "question": "Find Python projects for beginners",
  "use_realtime": true,
  "force_refresh": false
}
```

#### Repository Search
```bash
GET /api/search/repositories?query=machine+learning&language=python
```

#### Issue Search
```bash
GET /api/search/issues?repo=owner/repo-name
```

#### Contribution Guide
```bash
GET /api/contribution_guide?repo=owner/repo-name
```

#### Project Insights
```bash
GET /api/project_insights?repo=owner/repo-name
```

#### Trending Projects
```bash
GET /api/trending?topic=web+development&language=javascript
```

#### Stack Overflow Questions
```bash
GET /api/stackoverflow?repo=owner/repo-name
```

#### Reset Conversation
```bash
POST /api/reset
```

## 🛠️ Technologies Used

### Backend Framework
- **Flask 3.1.0**: Lightweight web framework
- **Flask-CORS**: Cross-origin resource sharing support

### AI & Machine Learning
- **Google Gemini (gemini-2.5-flash-lite)**: Large language model for conversational AI
- **LangChain**: Framework for building LLM-powered applications
- **FAISS**: Facebook AI Similarity Search for vector storage
- **FastEmbed**: Lightweight embeddings (optional fallback)

### Data Processing
- **BeautifulSoup4**: Web scraping and HTML parsing
- **Feedparser**: RSS feed parsing
- **Requests**: HTTP library for API calls

### Validation & Schemas
- **Marshmallow**: Object serialization and validation
- **Pydantic**: Data validation using Python type annotations

### Additional Tools
- **Python-dotenv**: Environment variable management
- **SQLAlchemy**: Database toolkit (for future extensions)

## 📁 Project Structure

```
open-source-assistant/
├── app.py                 # Main Flask application and API routes
├── requirements.txt       # Python dependencies
├── .env                   # Environment variables (create this)
├── .gitignore            # Git ignore rules
├── static/               # Static assets (CSS, JS)
│   └── ...
├── templates/            # HTML templates
│   └── index.html        # Main web interface
└── README.md             # This file
```

## 🎯 Key Features Explained

### Intelligent User Preference Learning

The assistant automatically learns from your questions:
- **Programming Languages**: Detects mentions of Python, JavaScript, Java, etc.
- **Interests**: Identifies topics like web dev, ML, DevOps, game dev
- **Skill Level**: Adapts to beginner, intermediate, or advanced users
- **Repository History**: Remembers previously discussed projects

### Smart Caching System

Implements three-tier caching:
- **Repository Cache**: 30-minute TTL
- **Issue Cache**: 15-minute TTL
- **Guide Cache**: 60-minute TTL

Benefits:
- Reduces GitHub API rate limit consumption
- Improves response times
- Force refresh option available when needed

### RAG (Retrieval-Augmented Generation)

The system uses a curated knowledge base including:
- Contribution workflow best practices
- Recommended beginner-friendly repositories
- Language-specific project suggestions
- Open source etiquette and guidelines

### Multi-Source Data Aggregation

Crawls and aggregates data from:
1. **GitHub Trending**: Real-time trending repositories
2. **DEV.to**: Latest articles and tutorials
3. **Reddit**: Community discussions (r/opensource, language subreddits)
4. **RSS Feeds**: OpenSource.com, Changelog
5. **Stack Overflow**: Relevant Q&A

## 🔧 Configuration

### Environment Variables

```env
# Required
GOOGLE_API_KEY=your_google_api_key
GITHUB_TOKEN=your_github_token

# Optional
PORT=5000                    # Server port (default: 5000)
DISABLE_RAG=false            # Disable RAG for constrained deployments
```

### Customizing Search Behavior

Edit these constants in `app.py`:

```python
GITHUB_PER_PAGE = 25         # Results per page

CACHE_CONFIG = {
    "repo": {"expiry": 1800},   # 30 minutes
    "issue": {"expiry": 900},   # 15 minutes
    "guide": {"expiry": 3600},  # 60 minutes
}
```

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

## 🐛 Known Issues & Limitations

- **GitHub API Rate Limits**: Free tier allows 5,000 requests/hour (authenticated)
- **Web Scraping Reliability**: Some sites may block or rate-limit scraping
- **Embedding Quotas**: Google Gemini embeddings have daily quotas
- **RAG Accuracy**: Vector search quality depends on knowledge base size

## 🔮 Future Enhancements

- [ ] User authentication and personalized dashboards
- [ ] Persistent storage for user preferences (PostgreSQL/MongoDB)
- [ ] GitLab and Bitbucket support
- [ ] Integration with Discord/Slack bots
- [ ] Advanced filtering (CI/CD status, test coverage)
- [ ] Contribution tracking and gamification
- [ ] Multi-language support (i18n)
- [ ] Code review assistance
- [ ] PR template generation
- [ ] Repository health scoring algorithm

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 👤 Author

**Shreyas P**
- GitHub: [@pshreyas77](https://github.com/pshreyas77)
- Project Link: [https://github.com/pshreyas77/open-source-assistant](https://github.com/pshreyas77/open-source-assistant)
- Website: [open-source-assistant.onrender.com](https://open-source-assistant.onrender.com)

## 🙏 Acknowledgments

- [Google Gemini](https://ai.google.dev/) for providing powerful AI capabilities
- [LangChain](https://www.langchain.com/) for the excellent RAG framework
- [GitHub API](https://docs.github.com/en/rest) for comprehensive repository data
- [FAISS](https://github.com/facebookresearch/faiss) by Facebook Research
- Open source community for inspiration and support

## 📞 Support

If you encounter any issues or have questions:

1. Check the [Issues](https://github.com/pshreyas77/open-source-assistant/issues) page
2. Create a new issue with detailed information
3. Reach out via GitHub Discussions

## ⭐ Star History

If you find this project useful, please consider giving it a star! It helps others discover the project.

---

**Made with ❤️ by developers, for developers**

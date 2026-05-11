# Language-Learner 🌍

An AI-powered language learning platform that helps users learn new languages through interactive conversations, vocabulary exercises, and personalized lessons.

## Features

- **AI Language Tutor**: Interactive conversations with AI to practice real-world language skills
- **Vocabulary Builder**: Learn and practice new words with spaced repetition
- **Grammar Lessons**: AI-generated grammar explanations and exercises
- **Conversation Practice**: Practice speaking/writing with an AI tutor
- **Progress Tracking**: Monitor your learning progress over time
- **Multi-Language Support**: Currently supports German (easily extensible to other languages)

## Tech Stack

- **Backend**: Python 3.11+ with FastAPI
- **Frontend**: React 18+ with TypeScript
- **AI Integration**: OpenAI API (GPT-4 recommended)
- **Database**: SQLite (development) / PostgreSQL (production)
- **Containerization**: Docker & Docker Compose

## Project Structure

```
Language-Learner/
├── backend/                 # Python FastAPI server
│   ├── app/
│   │   ├── main.py         # FastAPI app entry
│   │   ├── models/         # Pydantic models
│   │   ├── routes/         # API endpoints
│   │   ├── services/       # Business logic & AI integration
│   │   └── db/             # Database models
│   ├── requirements.txt
│   └── .env.example
├── frontend/               # React TypeScript app
│   ├── src/
│   │   ├── pages/         # Page components
│   │   ├── components/    # Reusable components
│   │   ├── hooks/         # Custom React hooks
│   │   ├── services/      # API services
│   │   └── types/         # TypeScript types
│   ├── package.json
│   └── .env.example
├── docker-compose.yml
└── README.md
```

## Getting Started

### Prerequisites
- Python 3.11+
- Node.js 18+
- OpenAI API key (get one at https://platform.openai.com)

### Quick Start

1. **Clone and setup**:
```bash
git clone <repo>
cd Language-Learner
```

2. **Backend setup**:
```bash
cd backend
cp .env.example .env
# Add your OpenAI API key to .env
pip install -r requirements.txt
python -m uvicorn app.main:app --reload
```

3. **Frontend setup** (in a new terminal):
```bash
cd frontend
npm install
npm start
```

4. **Access the app**:
- Frontend: http://localhost:3000
- Backend API: http://localhost:8000
- API Docs: http://localhost:8000/docs

## Environment Variables

Create `.env` files in both `backend/` and `frontend/` directories.

**Backend (.env)**:
```
OPENAI_API_KEY=your_key_here
DATABASE_URL=sqlite:///./language_learner.db
ENVIRONMENT=development
```

**Frontend (.env)**:
```
REACT_APP_API_URL=http://localhost:8000
```

## API Endpoints

- `POST /api/auth/register` - Register a new user
- `POST /api/auth/login` - Login user
- `GET /api/lessons/german` - Get German lessons
- `POST /api/lessons/{id}/solve` - Submit lesson answer
- `GET /api/vocabulary` - Get vocabulary list
- `POST /api/tutor/chat` - Chat with AI tutor
- `GET /api/progress` - Get learning progress

## Contributing

Fork the repo and submit pull requests for improvements!

## License

MIT
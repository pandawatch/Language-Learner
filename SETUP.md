# Setup and Installation Guide

## Prerequisites

Before you begin, make sure you have:
- Python 3.11+
- Node.js 18+
- npm or yarn
- OpenAI API key (get one at https://platform.openai.com/api-keys)

## Backend Setup

### 1. Navigate to backend directory
```bash
cd backend
```

### 2. Create a Python virtual environment
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

### 4. Create .env file
```bash
cp .env.example .env
```

Edit `.env` and add your OpenAI API key:
```
OPENAI_API_KEY=sk-...your-key-here...
DATABASE_URL=sqlite:///./language_learner.db
ENVIRONMENT=development
SECRET_KEY=your-secret-key-here
```

### 5. Run the backend
```bash
python -m uvicorn app.main:app --reload
```

The backend will be available at `http://localhost:8000`

## Frontend Setup

### 1. Navigate to frontend directory
```bash
cd frontend
```

### 2. Install dependencies
```bash
npm install
```

### 3. Create .env file
```bash
cp .env.example .env
```

Edit `.env`:
```
REACT_APP_API_URL=http://localhost:8000
```

### 4. Run the frontend
```bash
npm start
```

The frontend will be available at `http://localhost:3000`

## Docker Setup

### Using Docker Compose

1. Create a `.env` file in the root directory with your OpenAI API key:
```bash
OPENAI_API_KEY=sk-...your-key-here...
```

2. Run Docker Compose:
```bash
docker-compose up --build
```

This will start both backend (port 8000) and frontend (port 3000).

## API Documentation

Once the backend is running, visit:
- **Interactive API Docs**: http://localhost:8000/docs
- **Alternative API Docs**: http://localhost:8000/redoc

## Features

### Authentication
- Register a new account
- Login with email and password
- JWT token-based authentication

### Lessons
- Browse German lessons by difficulty
- Track lesson completion
- Get AI-generated lessons on specific topics

### Vocabulary
- View all available vocabulary
- Add words to your learning list
- Track vocabulary progress with spaced repetition

### AI Tutor
- Have real-time conversations in German
- Get grammar corrections and suggestions
- Practice common phrases and expressions
- View learning progress and streaks

## Common Commands

### Backend

```bash
# Run with auto-reload (development)
python -m uvicorn app.main:app --reload

# Run production server
uvicorn app.main:app --host 0.0.0.0 --port 8000

# Database initialization (if needed)
python -c "from app.db.database import Base, engine; Base.metadata.create_all(bind=engine)"
```

### Frontend

```bash
# Start development server
npm start

# Build for production
npm run build

# Run tests
npm test

# Eject webpack config (one-way operation, not recommended)
npm eject
```

## Troubleshooting

### Backend won't start
- Check that port 8000 is not in use
- Verify your OpenAI API key is valid
- Check Python version (requires 3.11+)

### Frontend won't start
- Delete `node_modules` and `package-lock.json`, then run `npm install`
- Check that port 3000 is not in use
- Check Node version (requires 18+)

### API connection issues
- Ensure backend is running on `http://localhost:8000`
- Check CORS settings in backend if getting CORS errors
- Verify `REACT_APP_API_URL` in frontend `.env`

## Next Steps

1. **Customize German curriculum**: Add more vocabulary and lessons
2. **Add more languages**: Extend the platform to support French, Spanish, etc.
3. **Implement audio**: Add speech recognition and text-to-speech
4. **User analytics**: Track learning patterns and provide insights
5. **Mobile app**: Create React Native or Flutter mobile version

## Environment Variables Reference

### Backend (.env)
- `OPENAI_API_KEY`: Your OpenAI API key (required)
- `DATABASE_URL`: Database connection string (default: sqlite:///./language_learner.db)
- `ENVIRONMENT`: Environment type - 'development' or 'production' (default: development)
- `SECRET_KEY`: JWT secret key (change in production)
- `ALGORITHM`: JWT algorithm (default: HS256)
- `ACCESS_TOKEN_EXPIRE_MINUTES`: Token expiration time in minutes (default: 30)

### Frontend (.env)
- `REACT_APP_API_URL`: Backend API URL (default: http://localhost:8000)

## Support

For issues or questions, please check the project README.md or create an issue in the repository.

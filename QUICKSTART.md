# 🚀 Quick Start Guide

Get your AI Language Learner running in minutes!

## 🎯 What You Get

- 🤖 AI-powered German tutor using OpenAI GPT
- 📚 Structured lessons with exercises
- 📖 500+ German vocabulary words
- 💬 Real-time conversation practice
- 📊 Progress tracking and streaks
- 🎨 Beautiful, modern UI with Tailwind CSS

## ⚡ Express Setup (5 minutes)

### 1. Clone and Enter Directory
```bash
git clone <your-repo-url>
cd Language-Learner
```

### 2. Get OpenAI API Key
1. Go to https://platform.openai.com/api-keys
2. Create a new API key
3. Copy it (you'll need it in step 3)

### 3. Backend Setup
```bash
cd backend

# Create virtual environment
python -m venv venv
source venv/bin/activate  # Or on Windows: venv\Scripts\activate

# Install dependencies
pip install -r requirements.txt

# Create environment file
cp .env.example .env

# Edit .env and add your OpenAI API key
# OPENAI_API_KEY=sk-your-key-here
nano .env  # or use your editor

# Start the backend
python -m uvicorn app.main:app --reload
```

Backend will be at: **http://localhost:8000**

### 4. Frontend Setup (in a new terminal)
```bash
cd frontend

# Install dependencies
npm install

# Create environment file
cp .env.example .env

# Start the frontend
npm start
```

Frontend will open at: **http://localhost:3000**

## 🎓 How to Use

1. **Create Account**: Register with email/password
2. **Browse Lessons**: Start with beginner German lessons
3. **Learn Vocabulary**: Add words to your learning list
4. **Chat with AI**: Practice real conversations in German
5. **Track Progress**: See your learning streaks and stats

## 📚 Features in Detail

### AI Tutor 🤖
- Natural conversation in German
- Automatic grammar corrections
- Vocabulary suggestions
- Pronunciation help

### Lessons 📚
- 10+ pre-built lessons
- Multiple difficulty levels
- Generated lessons on any topic
- Progress tracking

### Vocabulary 📖
- 500+ German words
- Spaced repetition system
- Difficulty ratings
- Part-of-speech tagging

### Dashboard 📊
- View learning stats
- Track completion rates
- Monitor streaks
- See languages in progress

## 🛠️ API Endpoints

**All endpoints require authentication except health check**

### Authentication
- `POST /api/auth/register` - Create new account
- `POST /api/auth/login` - Login user
- `POST /api/auth/verify` - Verify token

### Lessons
- `GET /api/lessons/german` - Get all German lessons
- `GET /api/lessons/{id}` - Get specific lesson
- `POST /api/lessons/{id}/complete` - Mark lesson complete

### Vocabulary
- `GET /api/vocabulary` - Get all vocabulary
- `GET /api/vocabulary/user` - Get user's vocabulary
- `POST /api/vocabulary/add` - Add word to list
- `POST /api/vocabulary/mark-correct` - Mark word as learned

### Tutor
- `POST /api/tutor/chat` - Chat with AI tutor
- `GET /api/tutor/progress` - Get learning progress
- `POST /api/tutor/lesson/generate` - Generate new lesson
- `POST /api/tutor/vocabulary/exercise` - Generate vocab exercise

**Full API docs at:** http://localhost:8000/docs

## 🐳 Docker (Optional)

```bash
# Make sure .env file exists in root with OpenAI API key
docker-compose up --build
```

Then visit http://localhost:3000

## 🔧 Configuration

### Backend (.env)
```env
OPENAI_API_KEY=sk-...your-key...    # required
DATABASE_URL=sqlite:///./language_learner.db
ENVIRONMENT=development
SECRET_KEY=change-in-production
```

### Frontend (.env)
```env
REACT_APP_API_URL=http://localhost:8000
```

## 📱 What's Included

```
Language-Learner/
├── backend/          # Python FastAPI server
│   ├── app/
│   │   ├── main.py              # FastAPI app
│   │   ├── routes/              # API endpoints
│   │   ├── services/            # Business logic
│   │   ├── models/              # Database models
│   │   └── db/                  # Database setup
│   └── requirements.txt
│
├── frontend/         # React TypeScript app
│   ├── src/
│   │   ├── pages/              # Page components
│   │   ├── components/         # Reusable components
│   │   ├── services/           # API client
│   │   ├── hooks/              # Custom hooks
│   │   └── types/              # TypeScript types
│   └── package.json
│
├── docker-compose.yml
├── SETUP.md                    # Detailed setup guide
└── README.md
```

## 🚨 Troubleshooting

### "ModuleNotFoundError: No module named 'openai'"
```bash
pip install -r requirements.txt
```

### "Cannot find module 'react'"
```bash
cd frontend
npm install
```

### "Connection refused" (frontend can't reach backend)
- Check backend is running on port 8000
- Check `REACT_APP_API_URL` in frontend/.env

### "Invalid OpenAI API key"
- Go to https://platform.openai.com/api-keys
- Create/regenerate your key
- Add to backend/.env

## 🎯 Next Steps

1. ✅ Get it running locally (you just did this!)
2. 🌐 Deploy backend to Heroku/Railway
3. 🔗 Deploy frontend to Vercel/Netlify
4. 🗣️ Add more languages
5. 🎵 Add audio/speech features
6. 📊 Create learning analytics dashboard

## 📖 Learn More

- [Setup Guide](SETUP.md) - Detailed configuration
- [Backend API Docs](http://localhost:8000/docs) - Interactive API docs
- [React Documentation](https://react.dev)
- [FastAPI Documentation](https://fastapi.tiangolo.com)
- [OpenAI Documentation](https://platform.openai.com/docs)

## 💡 Tips

- Start with simple greetings in the tutor
- Add vocabulary gradually to avoid overload
- Try different lesson topics using AI generation
- Check progress dashboard for motivation
- Practice daily for best results

## 🤝 Contributing

Found a bug? Have an idea? 
- Create an issue
- Submit a pull request
- Share your feedback

## ⚖️ License

MIT - Feel free to use this for learning and teaching!

---

**Happy Learning! 🎓🌍✨**

Have fun learning German with your personal AI tutor!

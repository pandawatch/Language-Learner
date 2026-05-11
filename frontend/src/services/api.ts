import axios from "axios";
import { TokenResponse, Lesson, Vocabulary, Progress } from "../types";

const API_URL = process.env.REACT_APP_API_URL || "http://localhost:8000";

const apiClient = axios.create({
  baseURL: API_URL,
});

// Add token to requests if available
apiClient.interceptors.request.use((config) => {
  const token = localStorage.getItem("access_token");
  if (token) {
    config.headers.Authorization = `Bearer ${token}`;
  }
  return config;
});

// Auth endpoints
export const authService = {
  register: (email: string, password: string, username: string) =>
    apiClient.post<TokenResponse>("/api/auth/register", {
      email,
      password,
      username,
    }),

  login: (email: string, password: string) =>
    apiClient.post<TokenResponse>("/api/auth/login", { email, password }),

  verifyToken: (token: string) =>
    apiClient.post("/api/auth/verify", { token }),
};

// Lessons endpoints
export const lessonsService = {
  getGermanLessons: () => apiClient.get<Lesson[]>("/api/lessons/german"),

  getLesson: (id: number) => apiClient.get<Lesson>(`/api/lessons/${id}`),

  completeLesson: (lessonId: number, score: number) =>
    apiClient.post(`/api/lessons/${lessonId}/complete`, {
      score,
      token: localStorage.getItem("access_token"),
    }),

  generateLesson: (topic: string, difficulty: string = "beginner") =>
    apiClient.post("/api/tutor/lesson/generate", { topic, difficulty }),
};

// Vocabulary endpoints
export const vocabularyService = {
  getVocabulary: () => apiClient.get<Vocabulary[]>("/api/vocabulary"),

  getUserVocabulary: () =>
    apiClient.get<Vocabulary[]>("/api/vocabulary/user", {
      params: { token: localStorage.getItem("access_token") },
    }),

  addVocabulary: (vocabId: number) =>
    apiClient.post("/api/vocabulary/add", {
      vocab_id: vocabId,
      token: localStorage.getItem("access_token"),
    }),

  markCorrect: (vocabId: number) =>
    apiClient.post("/api/vocabulary/mark-correct", {
      vocab_id: vocabId,
      token: localStorage.getItem("access_token"),
    }),
};

// Tutor endpoints
export const tutorService = {
  chat: (message: string, conversationHistory: any[] = []) =>
    apiClient.post("/api/tutor/chat", {
      message,
      language: "german",
      conversation_history: conversationHistory,
      token: localStorage.getItem("access_token"),
    }),

  getProgress: () =>
    apiClient.get<Progress>("/api/tutor/progress", {
      params: { token: localStorage.getItem("access_token") },
    }),

  generateVocabularyExercise: (words: string[], exerciseType: string = "multiple_choice") =>
    apiClient.post("/api/tutor/vocabulary/exercise", {
      words,
      exercise_type: exerciseType,
      token: localStorage.getItem("access_token"),
    }),
};

export default apiClient;

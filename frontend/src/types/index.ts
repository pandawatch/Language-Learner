export interface User {
  id: number;
  email: string;
  username: string;
  created_at: string;
}

export interface TokenResponse {
  access_token: string;
  token_type: string;
  user: User;
}

export interface Lesson {
  id: number;
  title: string;
  language: string;
  difficulty: number;
  content: string;
  exercise: string;
}

export interface Vocabulary {
  id: number;
  german: string;
  english: string;
  pronunciation?: string;
  part_of_speech: string;
  difficulty: number;
}

export interface ChatMessage {
  role: "user" | "assistant";
  content: string;
  language: string;
}

export interface Progress {
  total_lessons_completed: number;
  total_vocabulary_learned: number;
  current_streak: number;
  last_activity?: string;
  languages: string[];
}

import os
from openai import OpenAI
from typing import Optional, List

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))


class AITutorService:
    """Service for AI-powered language tutoring"""

    def __init__(self):
        self.model = "gpt-3.5-turbo"
        self.language = "German"

    def create_system_prompt(self, proficiency_level: str = "beginner") -> str:
        """Create a system prompt for the language tutor"""
        return f"""You are an expert German language tutor. Your role is to help users learn German through interactive conversations.

Proficiency Level: {proficiency_level}

Guidelines:
1. Respond mostly in German (with English translations in brackets when necessary for beginners)
2. Correct minor mistakes naturally during conversation
3. Suggest new vocabulary and phrases relevant to the conversation
4. Be encouraging and supportive
5. Ask follow-up questions to keep the conversation going
6. Use simple, clear language appropriate for the proficiency level
7. Provide pronunciation tips when needed

Format your responses as:
- Main response in German
- [English translation]
- 🎯 New vocabulary: word - definition
- 💡 Grammar tip: (if relevant)
- 📝 Suggestion: Help with what to say next"""

    async def chat(
        self,
        user_message: str,
        conversation_history: Optional[List[dict]] = None,
        proficiency_level: str = "beginner",
    ) -> dict:
        """Chat with the AI tutor"""

        if conversation_history is None:
            conversation_history = []

        # Prepare messages for the API
        messages = [
            {"role": "system", "content": self.create_system_prompt(proficiency_level)},
            *conversation_history,
            {"role": "user", "content": user_message},
        ]

        response = client.chat.completions.create(
            model=self.model, messages=messages, temperature=0.7, max_tokens=500
        )

        ai_response = response.choices[0].message.content

        # Extract suggestions and corrections from the response
        suggestions = self._extract_suggestions(ai_response)
        corrections = self._extract_corrections(ai_response)

        return {
            "response": ai_response,
            "suggestions": suggestions,
            "corrections": corrections,
        }

    def generate_lesson(
        self, topic: str, difficulty: str = "beginner", lesson_type: str = "dialogue"
    ) -> dict:
        """Generate a German lesson based on topic and difficulty"""

        prompt = f"""Create a {difficulty} German {lesson_type} lesson about "{topic}".

Format:
TITLE: [lesson title]

CONTENT:
[Main content - dialogue, explanation, or story]

VOCABULARY:
[Key words with translations and pronunciation]

EXERCISE:
[Practice exercise for the student]

ANSWERS:
[Suggested answers/corrections]"""

        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=1000,
        )

        return {"lesson": response.choices[0].message.content}

    def generate_vocabulary_exercise(
        self, words: List[str], exercise_type: str = "multiple_choice"
    ) -> dict:
        """Generate vocabulary exercises"""

        words_str = ", ".join(words)
        prompt = f"""Create a {exercise_type} vocabulary exercise with these German words: {words_str}

Format as JSON:
{{
  "exercise": "description",
  "questions": [
    {{
      "question": "...",
      "options": ["...", "...", "...", "..."],
      "correct_answer": "..."
    }}
  ]
}}"""

        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=800,
        )

        return {"exercise": response.choices[0].message.content}

    def evaluate_user_response(self, user_response: str, reference: str) -> dict:
        """Evaluate user's response and provide feedback"""

        prompt = f"""Evaluate this German language student's response and provide feedback.

Reference/Expected: {reference}
Student's Response: {user_response}

Provide:
1. Accuracy (0-100%)
2. Grammar corrections if needed
3. Alternative improvements
4. Positive feedback

Format as JSON:
{{
  "accuracy": 85,
  "is_correct": true/false,
  "corrections": "...",
  "improvements": ["...", "..."],
  "positive_feedback": "..."
}}"""

        response = client.chat.completions.create(
            model=self.model,
            messages=[{"role": "user", "content": prompt}],
            temperature=0.7,
            max_tokens=500,
        )

        return {"evaluation": response.choices[0].message.content}

    def _extract_suggestions(self, response: str) -> List[str]:
        """Extract vocabulary and phrase suggestions from response"""
        suggestions = []
        if "Suggestion:" in response or "📝" in response:
            lines = response.split("\n")
            for line in lines:
                if "Suggestion:" in line or "📝" in line:
                    suggestions.append(line.replace("Suggestion:", "").replace("📝", "").strip())
        return suggestions[:3]  # Return top 3 suggestions

    def _extract_corrections(self, response: str) -> Optional[str]:
        """Extract grammar corrections from response"""
        if "Grammar tip:" in response or "💡" in response:
            lines = response.split("\n")
            for line in lines:
                if "Grammar tip:" in line or "💡" in line:
                    return line.replace("Grammar tip:", "").replace("💡", "").strip()
        return None

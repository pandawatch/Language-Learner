import React, { useState, useRef, useEffect } from "react";
import { tutorService } from "../services/api";
import { ChatMessage } from "../types";

const Tutor: React.FC = () => {
  const [messages, setMessages] = useState<ChatMessage[]>([]);
  const [input, setInput] = useState("");
  const [loading, setLoading] = useState(false);
  const messagesEndRef = useRef<HTMLDivElement>(null);

  const scrollToBottom = () => {
    messagesEndRef.current?.scrollIntoView({ behavior: "smooth" });
  };

  useEffect(() => {
    scrollToBottom();
  }, [messages]);

  const handleSendMessage = async (e: React.FormEvent) => {
    e.preventDefault();
    if (!input.trim()) return;

    const userMessage: ChatMessage = {
      role: "user",
      content: input,
      language: "german",
    };

    setMessages((prev) => [...prev, userMessage]);
    setInput("");
    setLoading(true);

    try {
      const response = await tutorService.chat(input, messages);
      const assistantMessage: ChatMessage = {
        role: "assistant",
        content: response.data.response,
        language: "german",
      };
      setMessages((prev) => [...prev, assistantMessage]);
    } catch (err) {
      console.error("Error:", err);
    } finally {
      setLoading(false);
    }
  };

  return (
    <div className="h-screen flex flex-col bg-gray-50">
      <div className="flex-1 overflow-y-auto p-6 space-y-4">
        <div className="max-w-2xl mx-auto">
          {messages.length === 0 && (
            <div className="text-center py-16">
              <h1 className="text-3xl font-bold mb-4 text-gray-800">🎯 AI Language Tutor</h1>
              <p className="text-gray-600">Start a conversation in German to practice with our AI tutor!</p>
            </div>
          )}

          {messages.map((message, idx) => (
            <div key={idx} className={`flex ${message.role === "user" ? "justify-end" : "justify-start"}`}>
              <div
                className={`max-w-xs lg:max-w-md px-4 py-3 rounded-lg ${
                  message.role === "user" ? "bg-blue-500 text-white" : "bg-white border border-gray-200 text-gray-800"
                }`}
              >
                <p>{message.content}</p>
              </div>
            </div>
          ))}

          {loading && (
            <div className="flex justify-start">
              <div className="bg-white border border-gray-200 px-4 py-3 rounded-lg text-gray-800">
                <p>Typing...</p>
              </div>
            </div>
          )}

          <div ref={messagesEndRef} />
        </div>
      </div>

      <div className="border-t bg-white p-6">
        <form onSubmit={handleSendMessage} className="max-w-2xl mx-auto flex gap-2">
          <input
            type="text"
            value={input}
            onChange={(e) => setInput(e.target.value)}
            disabled={loading}
            placeholder="Type your message in German or English..."
            className="flex-1 px-4 py-2 border border-gray-300 rounded-lg focus:outline-none focus:border-blue-500"
          />
          <button
            type="submit"
            disabled={loading}
            className="bg-blue-500 hover:bg-blue-600 text-white px-6 py-2 rounded-lg font-semibold transition disabled:opacity-50"
          >
            Send
          </button>
        </form>
      </div>
    </div>
  );
};

export default Tutor;

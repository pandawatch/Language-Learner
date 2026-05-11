import React, { useEffect, useState } from "react";
import { lessonsService } from "../services/api";
import { Lesson } from "../types";

const Lessons: React.FC = () => {
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [loading, setLoading] = useState(true);
  const [selectedLesson, setSelectedLesson] = useState<Lesson | null>(null);

  useEffect(() => {
    const fetchLessons = async () => {
      try {
        const response = await lessonsService.getGermanLessons();
        setLessons(response.data);
      } catch (err) {
        console.error("Error fetching lessons:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchLessons();
  }, []);

  if (loading) {
    return <div className="flex items-center justify-center h-screen">Loading...</div>;
  }

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-6 py-8">
        <h1 className="text-4xl font-bold mb-8 text-gray-800">📚 German Lessons</h1>

        <div className="grid grid-cols-1 lg:grid-cols-3 gap-8">
          {/* Lessons List */}
          <div className="lg:col-span-2 space-y-4">
            {lessons.map((lesson) => (
              <div
                key={lesson.id}
                onClick={() => setSelectedLesson(lesson)}
                className={`p-6 rounded-lg cursor-pointer transition-all ${
                  selectedLesson?.id === lesson.id
                    ? "bg-blue-500 text-white shadow-lg"
                    : "bg-white hover:shadow-md"
                }`}
              >
                <h3 className="text-xl font-bold mb-2">{lesson.title}</h3>
                <p className={selectedLesson?.id === lesson.id ? "text-blue-100" : "text-gray-600"}>
                  {lesson.content.substring(0, 80)}...
                </p>
                <div className="flex gap-2 mt-4">
                  <span
                    className={`px-3 py-1 rounded text-sm font-semibold ${
                      selectedLesson?.id === lesson.id
                        ? "bg-blue-600"
                        : "bg-blue-100 text-blue-800"
                    }`}
                  >
                    Level {lesson.difficulty}
                  </span>
                </div>
              </div>
            ))}
          </div>

          {/* Lesson Detail */}
          {selectedLesson && (
            <div className="bg-white rounded-lg shadow-lg p-6 h-fit sticky top-6">
              <h2 className="text-2xl font-bold mb-4">{selectedLesson.title}</h2>

              <div className="mb-6">
                <h3 className="text-lg font-semibold mb-2">Content</h3>
                <p className="text-gray-700 mb-4">{selectedLesson.content}</p>
              </div>

              <div className="mb-6">
                <h3 className="text-lg font-semibold mb-2">Exercise</h3>
                <p className="text-gray-700 mb-4">{selectedLesson.exercise}</p>
              </div>

              <div className="mb-4">
                <span className="bg-blue-100 text-blue-800 px-3 py-1 rounded text-sm font-semibold">
                  Difficulty Level: {selectedLesson.difficulty}/5
                </span>
              </div>

              <button className="w-full bg-blue-500 hover:bg-blue-600 text-white font-semibold py-3 rounded-lg transition">
                Complete Lesson
              </button>
            </div>
          )}
        </div>
      </div>
    </div>
  );
};

export default Lessons;

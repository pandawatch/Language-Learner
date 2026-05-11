import React, { useEffect, useState } from "react";
import { tutorService, lessonsService } from "../services/api";
import { Progress, Lesson } from "../types";

const Dashboard: React.FC = () => {
  const [progress, setProgress] = useState<Progress | null>(null);
  const [lessons, setLessons] = useState<Lesson[]>([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    const fetchData = async () => {
      try {
        const [progressRes, lessonsRes] = await Promise.all([
          tutorService.getProgress(),
          lessonsService.getGermanLessons(),
        ]);

        setProgress(progressRes.data);
        setLessons(lessonsRes.data);
      } catch (err) {
        console.error("Error fetching data:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchData();
  }, []);

  if (loading) {
    return <div className="flex items-center justify-center h-screen">Loading...</div>;
  }

  return (
    <div className="bg-gray-50 min-h-screen">
      <div className="container mx-auto px-6 py-8">
        <h1 className="text-4xl font-bold mb-8 text-gray-800">Welcome back! 👋</h1>

        {/* Progress Stats */}
        {progress && (
          <div className="grid grid-cols-1 md:grid-cols-4 gap-6 mb-8">
            <div className="bg-white rounded-lg shadow p-6">
              <div className="text-3xl font-bold text-blue-500">{progress.total_lessons_completed}</div>
              <div className="text-gray-600">Lessons Completed</div>
            </div>

            <div className="bg-white rounded-lg shadow p-6">
              <div className="text-3xl font-bold text-green-500">{progress.total_vocabulary_learned}</div>
              <div className="text-gray-600">Words Learned</div>
            </div>

            <div className="bg-white rounded-lg shadow p-6">
              <div className="text-3xl font-bold text-orange-500">{progress.current_streak}</div>
              <div className="text-gray-600">Current Streak</div>
            </div>

            <div className="bg-white rounded-lg shadow p-6">
              <div className="text-lg font-semibold text-purple-500">{progress.languages.join(", ")}</div>
              <div className="text-gray-600">Languages</div>
            </div>
          </div>
        )}

        {/* Lessons Section */}
        <div>
          <h2 className="text-2xl font-bold mb-4 text-gray-800">Your Lessons</h2>
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {lessons.map((lesson) => (
              <div key={lesson.id} className="bg-white rounded-lg shadow hover:shadow-lg transition p-6">
                <h3 className="font-bold text-lg mb-2">{lesson.title}</h3>
                <p className="text-gray-600 text-sm mb-4">{lesson.content.substring(0, 100)}...</p>
                <div className="flex justify-between items-center mb-4">
                  <span className="bg-blue-100 text-blue-800 text-xs px-3 py-1 rounded">Difficulty {lesson.difficulty}</span>
                  <span className="text-gray-500 text-sm">{lesson.language}</span>
                </div>
                <button className="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 rounded font-semibold transition">
                  Start Lesson
                </button>
              </div>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
};

export default Dashboard;

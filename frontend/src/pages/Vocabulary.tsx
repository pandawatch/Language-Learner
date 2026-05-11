import React, { useEffect, useState } from "react";
import { vocabularyService } from "../services/api";
import { Vocabulary } from "../types";

const VocabularyPage: React.FC = () => {
  const [vocabulary, setVocabulary] = useState<Vocabulary[]>([]);
  const [userVocabulary, setUserVocabulary] = useState<Vocabulary[]>([]);
  const [loading, setLoading] = useState(true);
  const [tab, setTab] = useState<"all" | "learned">("all");

  useEffect(() => {
    const fetchVocabulary = async () => {
      try {
        const [allRes, userRes] = await Promise.all([
          vocabularyService.getVocabulary(),
          vocabularyService.getUserVocabulary(),
        ]);

        setVocabulary(allRes.data);
        setUserVocabulary(userRes.data);
      } catch (err) {
        console.error("Error fetching vocabulary:", err);
      } finally {
        setLoading(false);
      }
    };

    fetchVocabulary();
  }, []);

  const handleAddVocabulary = async (vocabId: number) => {
    try {
      await vocabularyService.addVocabulary(vocabId);
      const updated = await vocabularyService.getUserVocabulary();
      setUserVocabulary(updated.data);
    } catch (err) {
      console.error("Error adding vocabulary:", err);
    }
  };

  if (loading) {
    return <div className="flex items-center justify-center h-screen">Loading...</div>;
  }

  const displayVocabulary = tab === "all" ? vocabulary : userVocabulary;
  const learned = new Set(userVocabulary.map((v) => v.id));

  return (
    <div className="min-h-screen bg-gray-50">
      <div className="container mx-auto px-6 py-8">
        <h1 className="text-4xl font-bold mb-8 text-gray-800">📖 Vocabulary</h1>

        {/* Tabs */}
        <div className="flex gap-4 mb-8">
          <button
            onClick={() => setTab("all")}
            className={`px-6 py-2 rounded-lg font-semibold transition ${
              tab === "all"
                ? "bg-blue-500 text-white"
                : "bg-white text-gray-700 border border-gray-300 hover:border-blue-500"
            }`}
          >
            All Words ({vocabulary.length})
          </button>
          <button
            onClick={() => setTab("learned")}
            className={`px-6 py-2 rounded-lg font-semibold transition ${
              tab === "learned"
                ? "bg-blue-500 text-white"
                : "bg-white text-gray-700 border border-gray-300 hover:border-blue-500"
            }`}
          >
            My Words ({userVocabulary.length})
          </button>
        </div>

        {/* Vocabulary Grid */}
        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-4">
          {displayVocabulary.map((word) => (
            <div key={word.id} className="bg-white rounded-lg shadow hover:shadow-lg transition p-6">
              <div className="mb-4">
                <p className="text-2xl font-bold text-blue-600">{word.german}</p>
                <p className="text-gray-600">{word.english}</p>
                {word.pronunciation && <p className="text-sm text-gray-500">/{word.pronunciation}/</p>}
              </div>

              <div className="flex justify-between items-center mb-4">
                <span className="bg-gray-100 text-gray-800 text-xs px-3 py-1 rounded font-semibold">
                  {word.part_of_speech}
                </span>
                <span className="text-yellow-500">
                  {"⭐".repeat(word.difficulty)}
                </span>
              </div>

              {learned.has(word.id) ? (
                <button className="w-full bg-green-500 text-white py-2 rounded font-semibold cursor-default">
                  ✓ Added
                </button>
              ) : (
                <button
                  onClick={() => handleAddVocabulary(word.id)}
                  className="w-full bg-blue-500 hover:bg-blue-600 text-white py-2 rounded font-semibold transition"
                >
                  + Add to List
                </button>
              )}
            </div>
          ))}
        </div>
      </div>
    </div>
  );
};

export default VocabularyPage;

import React from "react";
import { Link } from "react-router-dom";

interface NavigationProps {
  user: any;
  onLogout: () => void;
}

const Navigation: React.FC<NavigationProps> = ({ user, onLogout }) => {
  return (
    <nav className="bg-blue-600 text-white shadow-lg">
      <div className="container mx-auto px-6 py-4 flex justify-between items-center">
        <Link to="/" className="text-2xl font-bold">
          🌍 Language Learner
        </Link>

        <div className="flex gap-6 items-center">
          <Link to="/dashboard" className="hover:text-gray-200 transition">
            Dashboard
          </Link>
          <Link to="/tutor" className="hover:text-gray-200 transition">
            Tutor
          </Link>
          <Link to="/lessons" className="hover:text-gray-200 transition">
            Lessons
          </Link>
          <Link to="/vocabulary" className="hover:text-gray-200 transition">
            Vocabulary
          </Link>

          <div className="flex items-center gap-4">
            {user && <span className="text-sm">{user.username}</span>}
            <button
              onClick={onLogout}
              className="bg-red-500 hover:bg-red-600 px-4 py-2 rounded transition"
            >
              Logout
            </button>
          </div>
        </div>
      </div>
    </nav>
  );
};

export default Navigation;

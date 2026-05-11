import React from "react";
import { BrowserRouter, Routes, Route, Navigate } from "react-router-dom";
import { useAuth } from "./hooks/useAuth";
import Navigation from "./components/Navigation";
import Login from "./pages/Login";
import Register from "./pages/Register";
import Dashboard from "./pages/Dashboard";
import Tutor from "./pages/Tutor";
import Lessons from "./pages/Lessons";
import VocabularyPage from "./pages/Vocabulary";

const App: React.FC = () => {
  const { isAuthenticated, user, login, register, logout } = useAuth();

  return (
    <BrowserRouter>
      {isAuthenticated && <Navigation user={user} onLogout={logout} />}
      <Routes>
        {!isAuthenticated ? (
          <>
            <Route
              path="/login"
              element={
                <Login
                  onLogin={(email, password) => {
                    return login(email, password);
                  }}
                />
              }
            />
            <Route
              path="/register"
              element={
                <Register
                  onRegister={(email, password, username) => {
                    return register(email, password, username);
                  }}
                />
              }
            />
            <Route path="*" element={<Navigate to="/login" />} />
          </>
        ) : (
          <>
            <Route path="/dashboard" element={<Dashboard />} />
            <Route path="/tutor" element={<Tutor />} />
            <Route path="/lessons" element={<Lessons />} />
            <Route path="/vocabulary" element={<VocabularyPage />} />
            <Route path="/" element={<Navigate to="/dashboard" />} />
          </>
        )}
      </Routes>
    </BrowserRouter>
  );
};

export default App;

import { useState, useCallback } from "react";
import { authService } from "../services/api";

export interface AuthContextType {
  isAuthenticated: boolean;
  user: any;
  login: (email: string, password: string) => Promise<void>;
  register: (email: string, password: string, username: string) => Promise<void>;
  logout: () => void;
}

export const useAuth = () => {
  const [isAuthenticated, setIsAuthenticated] = useState<boolean>(() => {
    return !!localStorage.getItem("access_token");
  });

  const [user, setUser] = useState<any>(() => {
    const saved = localStorage.getItem("user");
    return saved ? JSON.parse(saved) : null;
  });

  const login = useCallback(async (email: string, password: string) => {
    const response = await authService.login(email, password);
    const { access_token, user: userData } = response.data;

    localStorage.setItem("access_token", access_token);
    localStorage.setItem("user", JSON.stringify(userData));

    setIsAuthenticated(true);
    setUser(userData);
  }, []);

  const register = useCallback(async (email: string, password: string, username: string) => {
    const response = await authService.register(email, password, username);
    const { access_token, user: userData } = response.data;

    localStorage.setItem("access_token", access_token);
    localStorage.setItem("user", JSON.stringify(userData));

    setIsAuthenticated(true);
    setUser(userData);
  }, []);

  const logout = useCallback(() => {
    localStorage.removeItem("access_token");
    localStorage.removeItem("user");
    setIsAuthenticated(false);
    setUser(null);
  }, []);

  return { isAuthenticated, user, login, register, logout };
};

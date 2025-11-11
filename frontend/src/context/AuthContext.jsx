import React, { createContext, useState, useEffect } from 'react';
import axios from 'axios';

export const AuthContext = createContext();

export const AuthProvider = ({ children }) => {
    const [auth, setAuth] = useState({
        token: localStorage.getItem('token'),
        isAuthenticated: null,
        user: null
    });

    useEffect(() => {
        const fetchUser = async () => {
            const token = localStorage.getItem('token');
            if (token) {
                try {
                    const response = await axios.get('http://localhost:8000/auth/me', {
                        headers: { Authorization: `Bearer ${token}` }
                    });
                    setAuth({
                        token: token,
                        isAuthenticated: true,
                        user: response.data
                    });
                } catch (error) {
                    console.error('Error al verificar el token:', error);
                    localStorage.removeItem('token');
                    setAuth({
                        token: null,
                        isAuthenticated: false,
                        user: null
                    });
                }
            } else {
                setAuth({
                    token: null,
                    isAuthenticated: false,
                    user: null
                });
            }
        };
        fetchUser();
    }, []);

    const login = async (email, password) => {
        try {
            const response = await axios.post('http://localhost:8000/auth/login', { email_usuario: email, password });
            const { access_token } = response.data;
            localStorage.setItem('token', access_token);
            
            const userResponse = await axios.get('http://localhost:8000/auth/me', {
                headers: { Authorization: `Bearer ${access_token}` }
            });

            setAuth({
                token: access_token,
                isAuthenticated: true,
                user: userResponse.data
            });
            return { success: true }; // Indicar éxito
        } catch (error) {
            console.error('Error al iniciar sesión:', error);
            localStorage.removeItem('token'); // Asegurarse de que no haya un token inválido
            setAuth({
                token: null,
                isAuthenticated: false,
                user: null
            });
            return { success: false, message: error.response?.data?.detail || 'Credenciales inválidas. Por favor, inténtalo de nuevo.' }; // Indicar fallo y mensaje de error
        }
    };

    const logout = () => {
        localStorage.removeItem('token');
        setAuth({
            token: null,
            isAuthenticated: false,
            user: null
        });
    };

    return (
        <AuthContext.Provider value={{ ...auth, login, logout }}>
            {children}
        </AuthContext.Provider>
    );
};

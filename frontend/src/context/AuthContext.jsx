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
        const token = localStorage.getItem('token');
        if (token) {
            // Aquí podrías agregar una llamada para validar el token con el backend
            // y obtener la información del usuario.
            // Por ahora, simplemente asumimos que si hay un token, el usuario está autenticado.
            setAuth({
                token: token,
                isAuthenticated: true,
                user: null // User data should be fetched from backend, not hardcoded
            });
        } else {
            setAuth({
                token: null,
                isAuthenticated: false,
                user: null
            });
        }
    }, []);

    const login = async (email, password) => {
        try {
            const response = await axios.post('http://localhost:8000/auth/login', { email_usuario: email, password });
            const { access_token } = response.data;
            localStorage.setItem('token', access_token);
            // Aquí también deberías decodificar el token o hacer otra llamada para obtener los datos del usuario
            setAuth({
                token: access_token,
                isAuthenticated: true,
                user: { email }
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

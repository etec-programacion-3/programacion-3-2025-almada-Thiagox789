import React, { useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import { useNavigate } from 'react-router-dom';

const Login = () => {
    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });
    const { login } = useContext(AuthContext);
    const navigate = useNavigate();

    const { email, password } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = async e => {
        e.preventDefault();
        const success = await login(email, password);
        if (success) {
            navigate('/'); // Redirige al usuario a la página de inicio después de iniciar sesión
        } else {
            // Opcional: mostrar un mensaje de error al usuario
            alert('Credenciales inválidas. Por favor, inténtalo de nuevo.');
        }
    };

    return (
        <form onSubmit={onSubmit}>
            <div>
                <input
                    type="email"
                    placeholder="Email"
                    name="email"
                    value={email}
                    onChange={onChange}
                    required
                />
            </div>
            <div>
                <input
                    type="password"
                    placeholder="Password"
                    name="password"
                    value={password}
                    onChange={onChange}
                    minLength="6"
                    required
                />
            </div>
            <input type="submit" value="Login" />
        </form>
    );
};

export default Login;

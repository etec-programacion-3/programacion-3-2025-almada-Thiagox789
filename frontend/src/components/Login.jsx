import React, { useState, useContext } from 'react';
import { AuthContext } from '../context/AuthContext';
import { useNavigate, Link } from 'react-router-dom';
import './AuthForms.css'; // Import the new CSS file

const Login = () => {
    const [formData, setFormData] = useState({
        email: '',
        password: ''
    });
    const { login } = useContext(AuthContext);
    const navigate = useNavigate();
    const [loginError, setLoginError] = useState(null); // State to hold login error message

    const { email, password } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = async e => {
        e.preventDefault();
        setLoginError(null); // Clear previous errors
        const result = await login(email, password);
        if (result.success) {
            navigate('/'); // Redirige al usuario a la página de inicio después de iniciar sesión
        } else {
            setLoginError(result.message); // Display error message from backend or default
        }
    };

    return (
        <div className="container auth-container">
            <form className="auth-form" onSubmit={onSubmit}>
                <h2>Login</h2>
                <div className="form-group">
                    <label htmlFor="email">Email</label>
                    <input
                        type="email"
                        id="email"
                        placeholder="Ingresa tu email"
                        name="email"
                        value={email}
                        onChange={onChange}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="password">Contraseña</label>
                    <input
                        type="password"
                        id="password"
                        placeholder="Ingresa tu contraseña"
                        name="password"
                        value={password}
                        onChange={onChange}
                        minLength="6"
                        required
                    />
                </div>
                <button type="submit">Login</button>
                {loginError && <p className="error-message">{loginError}</p>} {/* Display error message */}
                <Link to="/register" className="switch-link">No tienes una cuenta? Regístrate aquí</Link>
            </form>
        </div>
    );
};

export default Login;

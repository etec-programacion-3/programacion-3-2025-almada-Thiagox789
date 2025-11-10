import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate, Link } from 'react-router-dom';
import './AuthForms.css'; // Import the new CSS file

const Register = () => {
    const [formData, setFormData] = useState({
        email: '',
        password: '',
        nombre_usuario: '',
        apellido_usuario: ''
    });

    const { email, password, nombre_usuario, apellido_usuario } = formData;

    const onChange = e => setFormData({ ...formData, [e.target.name]: e.target.value });

    const onSubmit = async e => {
        e.preventDefault();
        try {
            const newUser = {
                email_usuario: email,
                password,
                nombre_usuario,
                apellido_usuario
            };
            const config = {
                headers: {
                    'Content-Type': 'application/json'
                }
            };
            const body = JSON.stringify(newUser);
            const res = await axios.post('http://localhost:8000/auth/register', body, config);
            console.log(res.data);
            alert('Registro exitoso. Por favor, inicia sesión.');
            navigate('/login');
        } catch (err) {
            console.error(err.response.data);
            alert(err.response.data.detail || 'Error en el registro. Inténtalo de nuevo.');
        }
    };

    return (
        <div className="container auth-container">
            <form className="auth-form" onSubmit={onSubmit}>
                <h2>Registro</h2>
                <div className="form-group">
                    <label htmlFor="nombre_usuario">Nombre</label>
                    <input
                        type="text"
                        id="nombre_usuario"
                        placeholder="Ingresa tu nombre"
                        name="nombre_usuario"
                        value={nombre_usuario}
                        onChange={onChange}
                        required
                    />
                </div>
                <div className="form-group">
                    <label htmlFor="apellido_usuario">Apellido</label>
                    <input
                        type="text"
                        id="apellido_usuario"
                        placeholder="Ingresa tu apellido"
                        name="apellido_usuario"
                        value={apellido_usuario}
                        onChange={onChange}
                        required
                    />
                </div>
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
                        minLength="8"
                        required
                    />
                </div>
                <button type="submit">Registro</button>
                <Link to="/login" className="switch-link">Ya tienes una cuenta? Inicia sesión aquí</Link>
            </form>
        </div>
    );
};

export default Register;

import React, { useState } from 'react';
import axios from 'axios';
import { useNavigate } from 'react-router-dom';

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
        <form onSubmit={onSubmit}>
            <div>
                <input
                    type="text"
                    placeholder="Nombre"
                    name="nombre_usuario"
                    value={nombre_usuario}
                    onChange={onChange}
                    required
                />
            </div>
            <div>
                <input
                    type="text"
                    placeholder="Apellido"
                    name="apellido_usuario"
                    value={apellido_usuario}
                    onChange={onChange}
                    required
                />
            </div>
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
                    minLength="8"
                    required
                />
            </div>
            <input type="submit" value="Register" />
        </form>
    );
};

export default Register;

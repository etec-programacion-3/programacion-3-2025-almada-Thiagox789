import React, { useState } from 'react';
import { useNavigate } from 'react-router-dom';
import { useToast } from '../context/ToastContext.jsx';
import './AuthForms.css';

const CrearProducto = () => {
    const [nombre, setNombre] = useState('');
    const [descripcion, setDescripcion] = useState('');
    const [cantidad, setCantidad] = useState('');
    const [precio, setPrecio] = useState('');
    const [imagen, setImagen] = useState('');

    const navigate = useNavigate();
    const { addToast } = useToast();

    const handleSubmit = async (e) => {
        e.preventDefault();
        const token = localStorage.getItem('token');
        if (!token) {
            addToast('Debes iniciar sesión para crear un producto', 'error');
            navigate('/login');
            return;
        }

        try {
            const response = await fetch(`${import.meta.env.VITE_API_URL}/products/`, {
                method: 'POST',
                headers: {
                    'Content-Type': 'application/json',
                    'Authorization': `Bearer ${token}`
                },
                body: JSON.stringify({
                    nombre_producto: nombre,
                    descripcion_producto: descripcion,
                    cantidad_producto: parseInt(cantidad),
                    precio_producto: parseFloat(precio),
                    image_url: imagen
                })
            });

            if (response.ok) {
                addToast('Producto creado exitosamente', 'success');
                navigate('/');
            } else {
                const errorData = await response.json();
                addToast(`Error al crear el producto: ${errorData.detail}`, 'error');
            }
        } catch (error) {
            console.error('Error al crear el producto:', error);
            addToast('Ocurrió un error al crear el producto', 'error');
        }
    };

    return (
        <div className="container auth-container">
            <form className="auth-form" onSubmit={handleSubmit}>
                <h2>Crear Nuevo Producto</h2>
                <div className="form-group">
                    <label>Nombre:</label>
                    <input type="text" value={nombre} onChange={(e) => setNombre(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Descripción:</label>
                    <textarea value={descripcion} onChange={(e) => setDescripcion(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Cantidad:</label>
                    <input type="number" value={cantidad} onChange={(e) => setCantidad(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>Precio:</label>
                    <input type="number" step="0.01" value={precio} onChange={(e) => setPrecio(e.target.value)} required />
                </div>
                <div className="form-group">
                    <label>URL de la Imagen:</label>
                    <input type="text" value={imagen} onChange={(e) => setImagen(e.target.value)} />
                </div>

                <button type="submit">Crear Producto</button>
            </form>
        </div>
    );
};

export default CrearProducto;

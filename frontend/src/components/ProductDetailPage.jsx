import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';

const ProductDetailPage = () => {
    const { id } = useParams();
    const [product, setProduct] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);

    useEffect(() => {
        const fetchProduct = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/products/${id}`); // Assuming backend runs on port 8000
                setProduct(response.data);
            } catch (err) {
                setError('Error al cargar el producto.');
                console.error(err);
            } finally {
                setLoading(false);
            }
        };

        if (id) {
            fetchProduct();
        }
    }, [id]);

    if (loading) {
        return <div>Cargando producto...</div>;
    }

    if (error) {
        return <div>Error: {error}</div>;
    }

    if (!product) {
        return <div>Producto no encontrado.</div>;
    }

    return (
        <div className="product-detail-container">
            <h1 className="product-detail-title">{product.nombre_producto}</h1>
            <div className="product-detail-info">
                <p><strong>Descripción:</strong> {product.descripcion_producto}</p>
                <p><strong>Precio:</strong> <span className="product-detail-price">${product.precio_producto}</span></p>
                <p><strong>Cantidad disponible:</strong> {product.cantidad_producto}</p>
            </div>
            {/* Add more product details as needed */}
        </div>
    );
};

export default ProductDetailPage;

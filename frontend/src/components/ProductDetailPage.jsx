import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { useCart } from '../context/CartContext.jsx';

const ProductDetailPage = () => {
    const { id } = useParams();
    const { dispatch } = useCart();
    const [product, setProduct] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [quantityToAdd, setQuantityToAdd] = useState(1);

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

    const handleAddToCart = () => {
        if (product && quantityToAdd > 0 && quantityToAdd <= product.cantidad_producto) {
            dispatch({
                type: 'ADD_ITEM',
                payload: { product: product, quantity: quantityToAdd },
            });
            alert(`${quantityToAdd} de ${product.nombre_producto} añadido al carrito!`);
        } else {
            alert('Por favor, introduce una cantidad válida.');
        }
    };

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
            <img src={product.image_url}/>
            <div className="add-to-cart-section">
                <input
                    type="number"
                    min="1"
                    value={quantityToAdd}
                    onChange={(e) => setQuantityToAdd(parseInt(e.target.value))}
                    className="quantity-input"
                />
                <button onClick={handleAddToCart} className="add-to-cart-button">
                    Añadir al Carrito
                </button>
            </div>
        </div>
    );
};

export default ProductDetailPage;

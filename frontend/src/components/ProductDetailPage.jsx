import React, { useState, useEffect } from 'react';
import { useParams } from 'react-router-dom';
import axios from 'axios';
import { useCart } from '../context/CartContext.jsx';
import { useToast } from '../context/ToastContext.jsx';

const ProductDetailPage = () => {
    const { id } = useParams();
    const { dispatch } = useCart();
    const { addToast } = useToast();
    const [product, setProduct] = useState(null);
    const [loading, setLoading] = useState(true);
    const [error, setError] = useState(null);
    const [quantityToAdd, setQuantityToAdd] = useState(1);

    useEffect(() => {
        const fetchProduct = async () => {
            try {
                const response = await axios.get(`http://localhost:8000/products/${id}`);
                setProduct(response.data);
            } catch (err) {
                setError('Error al cargar el producto.');
                addToast('Error al cargar el producto', 'error');
                console.error(err);
            } finally {
                setLoading(false);
            }
        };

        if (id) {
            fetchProduct();
        }
    }, [id, addToast]);

    const handleAddToCart = () => {
        if (product && quantityToAdd > 0 && quantityToAdd <= product.cantidad_producto) {
            dispatch({
                type: 'ADD_ITEM',
                payload: { product: product, quantity: quantityToAdd },
            });
            addToast(`${quantityToAdd} de ${product.nombre_producto} añadido al carrito!`, 'success');
        } else {
            addToast('Por favor, introduce una cantidad válida.', 'error');
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
        <div className="container product-detail-container">
            <div className="product-detail-image-container">
                <img src={product.image_url} alt={product.nombre_producto} />
            </div>
            <div className="product-detail-content">
                <h1 className="product-detail-title">{product.nombre_producto}</h1>
                <div className="product-detail-info">
                    <p><strong>Descripción:</strong> {product.descripcion_producto}</p>
                    {product.usuario && (
                        <p><strong>Subido por:</strong> {product.usuario.nombre_usuario || product.usuario.email_usuario}</p>
                    )}
                    <p><strong>Precio:</strong> <span className="product-detail-price">${product.precio_producto}</span></p>
                    <p><strong>Cantidad disponible:</strong> {product.cantidad_producto}</p>
                </div>
                <div className="add-to-cart-section">
                    {product.cantidad_producto > 0 ? (
                        <>
                            <input
                                type="number"
                                min="1"
                                max={product.cantidad_producto}
                                value={quantityToAdd}
                                onChange={(e) => setQuantityToAdd(parseInt(e.target.value))}
                                className="quantity-input"
                            />
                            <button onClick={handleAddToCart} className="add-to-cart-button">
                                Añadir al Carrito
                            </button>
                        </>
                    ) : (
                        <p className="out-of-stock-message">Sin stock</p>
                    )}
                </div>
            </div>
        </div>
    );
};

export default ProductDetailPage;

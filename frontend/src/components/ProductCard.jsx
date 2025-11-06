import React from 'react';
import { Link } from 'react-router-dom'; // Import Link
import '../App.css'; // Assuming App.css contains some basic styling

const ProductCard = ({ product }) => {
  return (
    <Link to={`/products/${product.id_producto}`} className="product-card-link">
      <div className="product-card">
        <div className="product-image-container">
          <img src={product.image_url} alt={product.nombre_producto} />
        </div>
        <div className="product-info">
          <h3>{product.nombre_producto}</h3>
          <p>{product.descripcion_producto}</p>
          <p className="product-price">${product.precio_producto}</p>
        </div>
      </div>
    </Link>
  );
};

export default ProductCard;

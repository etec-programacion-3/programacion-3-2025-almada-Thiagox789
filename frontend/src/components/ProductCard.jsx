import React from 'react';
import { Link } from 'react-router-dom'; // Import Link
import '../App.css'; // Assuming App.css contains some basic styling

const ProductCard = ({ product }) => {
  return (
    <Link to={`/products/${product.id_producto}`} className="product-card-link"> {/* Wrap with Link */}
      <div className="product-card">
        <h3>{product.nombre_producto}</h3>
        <p>{product.descripcion_producto}</p>
        <p>Price: ${product.precio_producto}</p>
        <img src={product.image_url}/>
      </div>
    </Link>
  );
};

export default ProductCard;

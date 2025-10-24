neimport React from 'react';
import '../App.css'; // Assuming App.css contains some basic styling

const ProductCard = ({ product }) => {
  return (
    <div className="product-card">
      <h3>{product.nombre_producto}</h3>
      <p>{product.descripcion_producto}</p>
      <p>Price: ${product.precio_producto}</p>
      {/* Add more product details as needed */}
    </div>
  );
};

export default ProductCard;

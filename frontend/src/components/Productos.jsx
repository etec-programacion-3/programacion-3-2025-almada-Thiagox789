import React, { useState, useEffect } from 'react';
import ProductCard from './ProductCard';
import '../App.css';

function Productos() {
  const [products, setProducts] = useState([]);

  useEffect(() => {
    // Fetch products from the backend API
    fetch('http://localhost:8000/products') // Assuming the backend is running on port 8000
      .then(response => {
        if (!response.ok) {
          throw new Error('Network response was not ok');
        }
        return response.json();
      })
      .then(data => {
        setProducts(data);
      })
      .catch(error => {
        console.error('Error fetching products:', error);
      });
  }, []); // The empty dependency array ensures this effect runs only once

  return (
    <div>
      <h1>Nuestros Productos</h1>
      <div className="products-container">
        {products.map(product => (
          <ProductCard key={product.id_producto} product={product} />
        ))}
      </div>
    </div>
  );
}

export default Productos;

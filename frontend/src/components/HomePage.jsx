import React, { useEffect, useState } from 'react';
import axios from 'axios';
import ProductCard from './ProductCard';
import '../App.css'; // Assuming App.css contains some basic styling

const HomePage = () => {
  const [products, setProducts] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const [minPrice, setMinPrice] = useState('');
  const [maxPrice, setMaxPrice] = useState('');

  const fetchProducts = async () => {
    setLoading(true);
    try {
      const params = new URLSearchParams();
      if (minPrice) params.append('min_price', minPrice);
      if (maxPrice) params.append('max_price', maxPrice);

      const response = await axios.get(`http://localhost:8000/products/`, { params });
      setProducts(response.data);
    } catch (err) {
      setError(err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchProducts();
    // eslint-disable-next-line react-hooks/exhaustive-deps
  }, []);

  const handleFilter = () => {
    fetchProducts();
  };

  if (error) {
    return <div>Error: {error.message}</div>;
  }

  return (
    <div className="container home-page">
      <div className="page-header">
        <h1>Nuestros Productos</h1>
        <div className="filter-container">
          <input
            type="number"
            value={minPrice}
            onChange={(e) => setMinPrice(e.target.value)}
            placeholder="Precio Mínimo"
            className="filter-input"
          />
          <input
            type="number"
            value={maxPrice}
            onChange={(e) => setMaxPrice(e.target.value)}
            placeholder="Precio Máximo"
            className="filter-input"
          />
          <button className="filter-button" onClick={handleFilter}>Filtrar</button>
        </div>
      </div>

      {loading ? (
        <div>Loading products...</div>
      ) : (
        <div className="product-list">
          {products.map((product) => (
            <ProductCard key={product.id_producto} product={product} />
          ))}
        </div>
      )}
    </div>
  );
};

export default HomePage;

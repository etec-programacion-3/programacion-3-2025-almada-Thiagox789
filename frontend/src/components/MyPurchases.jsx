import React, { useEffect, useState } from 'react';
import axios from 'axios';
import { useToast } from '../context/ToastContext.jsx';

const MyPurchases = () => {
  const [purchases, setPurchases] = useState([]);
  const [loading, setLoading] = useState(true);
  const [error, setError] = useState(null);
  const { addToast } = useToast();

  useEffect(() => {
    const fetchPurchases = async () => {
      setLoading(true);
      const token = localStorage.getItem('token');
      if (!token) {
        setError('No autenticado');
        setLoading(false);
        return;
      }

      try {
        const response = await axios.get('http://localhost:8000/purchases/me', {
          headers: { Authorization: `Bearer ${token}` },
        });
        setPurchases(response.data);
      } catch (err) {
        console.error('Error al cargar compras:', err);
        setError('Error al cargar compras');
        addToast('Error al cargar tus compras', 'error');
      } finally {
        setLoading(false);
      }
    };

    fetchPurchases();
  }, [addToast]);

  if (loading) return <div className="container">Cargando tus compras...</div>;
  if (error) return <div className="container">Error: {error}</div>;

  return (
    <div className="container my-purchases">
      <h1>Mis compras</h1>
      {purchases.length === 0 ? (
        <p>No tienes compras aún.</p>
      ) : (
        <div className="purchases-list">
          {purchases.map((p) => (
            <div key={p.id_compra || `${p.producto_id}-${p.usuario_id}`} className="purchase-card">
              <h3>Compra #{p.id_compra ?? '—'}</h3>
              <p>Cantidad: {p.cantidad}</p>
              {p.producto ? (
                <div className="purchase-product">
                  <img src={p.producto.image_url} alt={p.producto.nombre_producto} style={{width:120}} />
                  <div>
                    <p><strong>{p.producto.nombre_producto}</strong></p>
                    <p>{p.producto.descripcion_producto}</p>
                    <p>Precio: ${p.producto.precio_producto}</p>
                  </div>
                </div>
              ) : (
                <p>Producto ID: {p.producto_id}</p>
              )}
            </div>
          ))}
        </div>
      )}
    </div>
  );
};

export default MyPurchases;

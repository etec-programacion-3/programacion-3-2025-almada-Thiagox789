import React from 'react';
import { useCart } from '../context/CartContext.jsx';
import axios from 'axios';

function Carrito() {
  const { cartState, dispatch } = useCart();

  const handleCheckout = async () => {
    if (window.confirm('¿Estás seguro de que quieres proceder al pago?')) {
      try {
        const promises = cartState.items.map(item =>
          axios.put(`http://localhost:8000/products/${item.product.id_producto}/stock`, {
            quantity: item.quantity
          })
        );
        await Promise.all(promises);
        dispatch({ type: 'CLEAR_CART' });
        alert('¡Pago realizado con éxito!');
      } catch (error) {
        console.error('Error al actualizar el stock:', error);
        alert('Hubo un error al procesar tu pedido. Por favor, inténtalo de nuevo.');
      }
    }
  };

  const handleRemoveItem = (productId) => {
    dispatch({ type: 'REMOVE_ITEM', payload: productId });
  };

  const handleUpdateQuantity = (productId, quantity) => {
    if (quantity > 0) {
      dispatch({ type: 'UPDATE_QUANTITY', payload: { productId, quantity } });
    }
  };

  const calculateTotal = () => {
    return cartState.items.reduce(
      (total, item) => total + item.product.precio_producto * item.quantity,
      0
    ).toFixed(2);
  };

  return (
    <div className="cart-container">
      <h1>Tu Carrito de Compras</h1>
      {cartState.items.length === 0 ? (
        <p>El carrito está vacío.</p>
      ) : (
        <div className="cart-items">
          {cartState.items.map((item) => (
            <div key={item.product.id} className="cart-item">
              <img src={item.product.image_url} alt={item.product.nombre_producto} className="cart-item-image" />
              <div className="cart-item-details">
                <h3>{item.product.nombre_producto}</h3>
                <p>Precio: ${item.product.precio_producto}</p>
                <div className="cart-item-quantity-control">
                  <button onClick={() => handleUpdateQuantity(item.product.id, item.quantity - 1)}>-</button>
                  <input
                    type="number"
                    value={item.quantity}
                    onChange={(e) => handleUpdateQuantity(item.product.id, parseInt(e.target.value))}
                    min="1"
                  />
                  <button onClick={() => handleUpdateQuantity(item.product.id, item.quantity + 1)}>+</button>
                </div>
                <p>Subtotal: ${(item.product.precio_producto * item.quantity).toFixed(2)}</p>
                <button onClick={() => handleRemoveItem(item.product.id)} className="remove-item-button">
                  Eliminar
                </button>
              </div>
            </div>
          ))}
          <div className="cart-summary">
            <h2>Total: ${calculateTotal()}</h2>
            <button className="checkout-button" onClick={handleCheckout}>Proceder al Pago</button>
          </div>
        </div>
      )}
    </div>
  );
}

export default Carrito;

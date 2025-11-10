import './App.css'
import { Routes, Route, Link } from 'react-router-dom';
import { useContext, useState } from 'react';
import { AuthContext } from './context/AuthContext';
import HomePage from './components/HomePage';
import Productos from './components/Productos';
import Login from './components/Login';
import Register from './components/Register';
import Carrito from './components/Carrito';
import ProductDetailPage from './components/ProductDetailPage';
import ProtectedRoute from './components/ProtectedRoute';
import CrearProducto from './components/CrearProducto';
import MyPurchases from './components/MyPurchases';

function App() {
  const { isAuthenticated, user, logout } = useContext(AuthContext);


  return (
    <>
      <nav>
        <div className="container nav-bar">
          <div className="nav-left">
            <Link to="/" className="logo">Mundo Deporte</Link>
          </div>

          <ul className="nav-list">
            {isAuthenticated ? (
              <>
                <li><Link to="/">Inicio</Link></li>
                    <li><Link to="/mis-compras">Mis compras</Link></li>
                <li><Link to="/crear-producto">Crear Producto</Link></li>
                <li><Link to="/Carrito">Carrito</Link></li>
                <li className="nav-user"><span>{user && user.email}</span></li>
                <li><button className="link-button" onClick={logout}>Cerrar Sesión</button></li>
              </>
            ) : (
              <>
                <li><Link to="/login">Inicia Sesión</Link></li>
                <li><Link to="/register">Regístrate</Link></li>
              </>
            )}
          </ul>
        </div>
      </nav>

      <Routes>
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route
          path="/"
          element={
            <ProtectedRoute>
              <HomePage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/Productos"
          element={
            <ProtectedRoute>
              <Productos />
            </ProtectedRoute>
          }
        />
        <Route
          path="/Carrito"
          element={
            <ProtectedRoute>
              <Carrito />
            </ProtectedRoute>
          }
        />
        <Route
          path="/products/:id"
          element={
            <ProtectedRoute>
              <ProductDetailPage />
            </ProtectedRoute>
          }
        />
        <Route
          path="/crear-producto"
          element={
            <ProtectedRoute>
              <CrearProducto />
            </ProtectedRoute>
          }
        />
        <Route
          path="/mis-compras"
          element={
            <ProtectedRoute>
              <MyPurchases />
            </ProtectedRoute>
          }
        />
      </Routes>
    </>
  )
}

export default App

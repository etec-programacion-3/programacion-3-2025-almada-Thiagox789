import './App.css'
import { Routes, Route, Link } from 'react-router-dom';
import { useContext } from 'react';
import { AuthContext } from './context/AuthContext';
import HomePage from './components/HomePage';
import Productos from './components/Productos';
import Login from './components/Login';
import Register from './components/Register';
import Carrito from './components/Carrito';
import ProductDetailPage from './components/ProductDetailPage';
import ProtectedRoute from './components/ProtectedRoute';

function App() {
  const { isAuthenticated, user, logout } = useContext(AuthContext);

  return (
    <>
      <nav>
        <ul>
          {isAuthenticated ? (
            <>
              <li><Link to="/">Inicio</Link></li>
              <li><Link to="/Productos">Productos</Link></li>
              <li><Link to="/Carrito">Carrito</Link></li>
              <li><span>{user && user.email}</span></li>
              <li><button onClick={logout}>Cerrar Sesion</button></li>
            </>
          ) : (
            <>
              <li><Link to="/login">Inicia Sesion</Link></li>
              <li><Link to="/register">Registrate</Link></li>
            </>
          )}
        </ul>
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
      </Routes>
    </>
  )
}

export default App

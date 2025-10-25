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

function App() {
  const { isAuthenticated, user, logout } = useContext(AuthContext);

  return (
    <>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/Productos">Productos</Link></li>
          {isAuthenticated ? (
            <>
              <li><span>{user && user.email}</span></li>
              <li><button onClick={logout}>Logout</button></li>
            </>
          ) : (
            <>
              <li><Link to="/login">Login</Link></li>
              <li><Link to="/register">Register</Link></li>
            </>
          )}
          <li><Link to="/Carrito">Carrito</Link></li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/Productos" element={<Productos />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
        <Route path="/Carrito" element={<Carrito />} />
        <Route path="/products/:id" element={<ProductDetailPage />} />
      </Routes>
    </>
  )
}

export default App

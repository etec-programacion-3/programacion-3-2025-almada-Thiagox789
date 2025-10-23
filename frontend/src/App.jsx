import './App.css'
import { Routes, Route, Link } from 'react-router-dom';
import HomePage from './components/HomePage';
import Productos from './components/Productos';
import Login from './components/Login';
import Carrito from './components/Carrito';

function App() {
  return (
    <>
      <nav>
        <ul>
          <li><Link to="/">Home</Link></li>
          <li><Link to="/Productos">Productos</Link></li>
          <li><Link to="/Login">Login</Link></li>
          <li><Link to="/Carrito">Carrito</Link></li>
        </ul>
      </nav>

      <Routes>
        <Route path="/" element={<HomePage />} />
        <Route path="/Productos" element={<Productos />} />
        <Route path="/Login" element={<Login />} />
        <Route path="/Carrito" element={<Carrito />} />
      </Routes>
    </>
  )
}

export default App

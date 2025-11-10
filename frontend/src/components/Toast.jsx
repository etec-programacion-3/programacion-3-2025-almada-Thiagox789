import React, { useEffect } from 'react';
import '../App.css';

const Toast = ({ message, type, onClose, duration = 3000 }) => {
  useEffect(() => {
    const timer = setTimeout(() => {
      onClose();
    }, duration);

    return () => clearTimeout(timer);
  }, [onClose, duration]);

  return (
    <div className={`toast ${type}`}>
      <span>{message}</span>
      <button onClick={onClose} style={{ marginLeft: '10px', background: 'transparent', border: 'none', color: 'inherit', cursor: 'pointer' }}>
        ×
      </button>
    </div>
  );
};

export default Toast;

# Mundo Deporte E-commerce Application

This repository contains a full-stack e-commerce application named "Mundo Deporte," developed as a project for Programación 3 - 2025. The application features a product catalog, user authentication, a shopping cart, and a payment simulation with stock management.

## Table of Contents

- [Features](#features)
- [Technologies Used](#technologies-used)
- [Project Structure](#project-structure)
- [Setup and Installation](#setup-and-installation)
  - [Backend Setup](#backend-setup)
  - [Frontend Setup](#frontend-setup)
- [Running the Application](#running-the-application)
- [API Endpoints](#api-endpoints)
- [Contributing](#contributing)
- [License](#license)

## Features

- **User Authentication:** Register, login, and logout functionality.
- **Product Catalog:** Browse and view details of various products.
- **Shopping Cart:** Add, remove, and update quantities of products in the cart.
- **Stock Management:** Product quantities are updated upon successful purchase.
- **Payment Simulation:** A confirmation step before finalizing a purchase.
- **Responsive Design:** A modern and clean user interface.

## Technologies Used

### Frontend
- **React:** A JavaScript library for building user interfaces.
- **Vite:** A fast build tool for modern web projects.
- **React Router DOM:** For declarative routing in React applications.
- **Axios:** For making HTTP requests.
- **CSS:** For styling the application.

### Backend
- **FastAPI:** A modern, fast (high-performance) web framework for building APIs with Python 3.7+ based on standard Python type hints.
- **SQLAlchemy:** An SQL toolkit and Object-Relational Mapper (ORM) that gives application developers the full power and flexibility of SQL.
- **SQLite:** A C-language library that implements a small, fast, self-contained, high-reliability, full-featured, SQL database engine.
- **Uvicorn:** An ASGI server for Python.
- **Alembic:** A database migration tool for SQLAlchemy.
- **PyJWT:** For JSON Web Token (JWT) implementation for authentication.
- **Passlib:** For password hashing.

## Project Structure

The project is divided into two main parts: `backend` and `frontend`.

```
.
├── backend/
│   ├── alembic/                  # Database migrations
│   ├── app/                      # FastAPI application
│   │   ├── database/             # Database connection and models
│   │   ├── models/               # SQLAlchemy ORM models
│   │   ├── routes/               # API endpoints
│   │   └── schemas/              # Pydantic schemas for data validation
│   ├── auth.py                   # Authentication logic
│   ├── requirements.txt          # Backend Python dependencies
│   └── README.md                 # Backend specific documentation
├── frontend/
│   ├── public/                   # Static assets
│   ├── src/                      # React application source code
│   │   ├── assets/               # Images and other assets
│   │   ├── components/           # Reusable React components
│   │   ├── context/              # React Context for state management
│   │   ├── App.css               # Global styles
│   │   ├── App.jsx               # Main application component
│   │   ├── index.css             # Base CSS
│   │   └── main.jsx              # Entry point for React app
│   ├── package.json              # Frontend Node.js dependencies
│   └── README.md                 # Frontend specific documentation
└── README.md                     # Main project README
```

## Setup and Installation

Follow these steps to get the project up and running on your local machine.

### Backend Setup

1.  **Navigate to the backend directory:**
    ```bash
    cd backend
    ```

2.  **Create a virtual environment (recommended):**
    ```bash
    python -m venv venv
    ```

3.  **Activate the virtual environment:**
    -
        ```bash
        source venv/bin/activate
        ```

4.  **Install backend dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

5.  **Run database migrations:**
    ```bash
    alembic upgrade head
    ```

6.  **Start the backend server:**
    ```bash
    uvicorn app.main:app --reload --port 8000
    ```
    The backend API will be available at `http://localhost:8000`.

### Frontend Setup

1.  **Navigate to the frontend directory:**
    ```bash
    cd frontend
    ```

2.  **Install frontend dependencies:**
    ```bash
    npm install
    ```

3.  **Start the frontend development server:**
    ```bash
    npm run dev
    ```
    The frontend application will be available at `http://localhost:5173` (or another port if 5173 is in use).

## Running the Application

1.  Ensure both backend and frontend servers are running in separate terminal instances.
2.  Open your web browser and navigate to the frontend URL (e.g., `http://localhost:5173`).

## API Endpoints

The backend provides the following main API endpoints:

-   `/auth/register`: Register a new user.
-   `/auth/login`: Authenticate a user and get a JWT token.
-   `/products/`: Get all products (supports filtering by `min_price` and `max_price`).
-   `/products/{product_id}`: Get a single product by ID.
-   `/products/`: Create a new product (requires authentication).
-   `/products/{product_id}`: Update an existing product (requires authentication).
-   `/products/{product_id}/stock`: Update product stock (used after purchase).
-   `/products/{product_id}`: Delete a product (requires authentication).

## Contributing

Feel free to fork this repository, open issues, and submit pull requests.

## License

This project is licensed under the MIT License.

from logging.config import fileConfig
import sys
import os
from sqlalchemy import engine_from_config, pool
from alembic import context

# --- Rutas ---
sys.path.append(os.path.join(os.path.dirname(__file__), "..", ".."))

# --- Configuración base de Alembic ---
config = context.config

# Logging (para mostrar mensajes de migraciones)
if config.config_file_name is not None:
    fileConfig(config.config_file_name)

# --- Importamos modelos y Base ---
from backend.app.database.db import Base, SQLALCHEMY_DATABASE_URL
from backend.app.models.ORM_User import Usuario
from backend.app.models.ORM_Producto import Producto
from backend.app.models.ORM_Compras import Compra

# 🔹 Usar la misma base de datos que la app
config.set_main_option("sqlalchemy.url", SQLALCHEMY_DATABASE_URL)

# --- Metadata para autogenerate ---
target_metadata = Base.metadata


def run_migrations_offline() -> None:
    """Ejecuta migraciones en modo 'offline' (sin conexión directa)."""
    url = config.get_main_option("sqlalchemy.url")
    context.configure(
        url=url,
        target_metadata=target_metadata,
        literal_binds=True,
        dialect_opts={"paramstyle": "named"},
    )
    with context.begin_transaction():
        context.run_migrations()


def run_migrations_online() -> None:
    """Ejecuta migraciones en modo 'online' (con conexión activa)."""
    connectable = engine_from_config(
        config.get_section(config.config_ini_section, {}),
        prefix="sqlalchemy.",
        poolclass=pool.NullPool,
    )

    with connectable.connect() as connection:
        context.configure(connection=connection, target_metadata=target_metadata)

        with context.begin_transaction():
            context.run_migrations()


if context.is_offline_mode():
    run_migrations_offline()
else:
    run_migrations_online()

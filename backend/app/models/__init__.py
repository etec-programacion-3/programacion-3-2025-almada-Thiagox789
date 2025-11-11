"""Package initializer for app.models.
Import model classes here so SQLAlchemy mappers are registered when
`import app.models` is executed. This helps avoid "failed to locate a name"
errors for relationship string names like 'Compra'.
"""
from .ORM_User import Usuario
from .ORM_Producto import Producto
from .ORM_Compras import Compra

__all__ = ["Usuario", "Producto", "Compra"]

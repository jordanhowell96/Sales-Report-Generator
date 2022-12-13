# Defines custom dataclass models.
# Decimal is used instead of float to represent money in order to avoid
# rounding errors that floats are prone to.

from dataclasses import dataclass
from decimal import Decimal


@dataclass
class Product:
    """Model for product data"""

    name: str
    unit_price: Decimal
    lot_size: int


@dataclass
class ProductSaleData:
    """Model for sales data of a product"""

    gross_rev: Decimal
    total_units: int
    disc_cost: Decimal


@dataclass
class Sale:
    """Model for a sale"""

    prod_id: int
    team_id: int
    lots_sold: int
    discount: Decimal

# Defines custom dataclass models

from dataclasses import dataclass


@dataclass
class Product:
    """Model for product data"""

    name: str
    unit_price: float
    lot_size: int


@dataclass
class ProductSaleData:
    """Model for sales data of a product"""

    gross_rev: float
    total_units: int
    disc_cost: float


@dataclass
class Sale:
    """Model for a sale"""

    prod_id: int
    team_id: int
    lots_sold: int
    discount: float

# Defines function for calculating team and product reports from a team map, sales data, and product master.
# Decimal is used instead of float to represent money in order to avoid
# rounding errors that floats are prone to

from decimal import Decimal
from .update_rpts import update_prod_rpt, update_team_rpt
from .get import get_product, get_team
from ..models import Product, ProductSaleData, Sale


def calc_sales_rpt(*,
                   team_map: dict[int, str],
                   prod_master: dict[int, Product],
                   sales_data: tuple[Sale],
                   hide_exc: bool = False
                   ) -> tuple[dict[str, Decimal],
                              dict[str, ProductSaleData]]:
    """
        Calculates the team report and product report from the team map, product master, and sales data

        :param team_map: dict with key = team id (int), value = team name (str)
        :param prod_master: dict with key = product id (int), value = Product
        :param sales_data: tuple of sales (Sale)
        :param hide_exc: bool to specify if exceptions should be hidden from console

        :returns: tuple of two dicts where the first dict contains team report information with

            key = team name (str)
            value = gross revenue (Decimal)

            and the second dict contains product report information with

            key = product name (str)
            value = ProductSaleData
    """

    # Initialize output dicts
    team_rpt: dict[str, Decimal] = {}
    prod_rpt: dict[str, ProductSaleData] = {}

    # Iterate through sales
    sale: Sale
    for sale in sales_data:
        product: Product = get_product(prod_master, sale.prod_id, hide_exc)
        team_name: str = get_team(team_map, sale.team_id, hide_exc)

        units_sold: int = sale.lots_sold * product.lot_size
        revenue: Decimal = units_sold * product.unit_price
        disc_cost: Decimal = Decimal(revenue * Decimal(sale.discount) / 100)

        update_team_rpt(team_rpt, team_name, revenue)
        update_prod_rpt(prod_rpt, product.name, revenue, units_sold, disc_cost)

    return team_rpt, prod_rpt

# Defines function for calculating team and product reports from a team map, sales data, and product master.

from .exceptions import ProductNotFoundError, TeamNotFoundError
from ..models import Product, ProductSaleData, Sale


def calc_sales_rpt(*,
                   team_map: dict[int, str],
                   prod_master: dict[int, Product],
                   sales_data: tuple[Sale],
                   hide_exc=False
                   ) -> tuple[dict[str, float],
                              dict[str, ProductSaleData]]:
    """
        Calculates the team report and product report from the team map, product master, and sales data

        :param team_map: dict with key = team id (int), value = team name (str)
        :param prod_master: dict with key = product id (int), value = Product
        :param sales_data: tuple of sales (Sale)
        :param hide_exc: bool to specify if exceptions should be hidden from console

        :returns: tuple of two dicts where the first dict contains team report information with

            key = team name (str),
            value = revenue (float)

            and the second dict contains product report information with

            key = product name (str),
            value = ProductSaleData

        :raises ProductNotFoundError if a product id in the sales data does not exist in the product master
        :raises TeamNotFoundError if a team id in the sales data does not exist in the team map
    """

    # Initialize output dicts
    team_rpt: dict[str, float] = {}
    prod_rpt: dict[str, ProductSaleData] = {}

    # Iterate through sales
    sale: Sale
    for sale in sales_data:

        # Get product info
        product: Product = prod_master.get(sale.prod_id)
        if not product:
            if hide_exc:
                print(f"Error: Product ID {sale.prod_id} not found in team map.")
                exit()
            raise ProductNotFoundError(sale.prod_id)

        # Get team name
        team_name: str = team_map.get(sale.team_id)
        if not team_name:
            if hide_exc:
                print(f"Error: Team ID {sale.team_id} not found in product master.")
                exit()
            raise TeamNotFoundError(sale.team_id)

        units_sold: int = sale.lots_sold * product.lot_size
        revenue: float = units_sold * product.unit_price
        disc_cost: float = revenue * sale.discount / 100

        # Update team report =======================================
        if team_name in team_rpt.keys():
            team_rpt[team_name] += revenue
        else:
            team_rpt.update({team_name: revenue})

        # Update product report ====================================
        prod_sale_data: ProductSaleData = prod_rpt.get(product.name)

        if prod_sale_data is not None:
            prod_sale_data.gross_rev += revenue
            prod_sale_data.total_units += units_sold
            prod_sale_data.disc_cost += disc_cost

        else:
            prod_rpt.update(
                {
                    product.name: ProductSaleData(
                        gross_rev=revenue,
                        total_units=units_sold,
                        disc_cost=disc_cost)
                }
            )

    return team_rpt, prod_rpt

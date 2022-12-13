from decimal import Decimal
from ..models import ProductSaleData


def update_prod_rpt(prod_rpt: dict[str, ProductSaleData],
                    prod_name: str,
                    revenue: Decimal,
                    units_sold: int,
                    disc_cost: Decimal
                    ) -> None:
    """
        Updates the ProductSaleData in for a product in the product report

        :param prod_rpt: dict with key = product name (str) value = ProductSaleData
        :param prod_name: name of the product sold (str)
        :param revenue: gross revenue of a sale (Decimal)
        :param units_sold: units sold in a sale (int)
        :param disc_cost: discount cost of a sale (Decimal)
    """

    prod_sale_data: ProductSaleData = prod_rpt.get(prod_name)

    if prod_sale_data is not None:
        prod_sale_data.gross_rev += revenue
        prod_sale_data.total_units += units_sold
        prod_sale_data.disc_cost += disc_cost

    else:
        prod_rpt.update(
            {
                prod_name: ProductSaleData(
                    gross_rev=revenue,
                    total_units=units_sold,
                    disc_cost=disc_cost)
            }
        )


def update_team_rpt(team_rpt: dict[str, Decimal],
                    team_name: str,
                    revenue: Decimal
                    ) -> None:
    """
        Adds to the gross revenue value of a team in the team report

        :param team_rpt: dict with key = team name (str) value = gross revenue (Decimal)
        :param team_name: name of the team that made the sale (str)
        :param revenue: gross revenue of a sale (Decimal)
    """

    if team_name in team_rpt.keys():
        team_rpt[team_name] += revenue
    else:
        team_rpt.update({team_name: revenue})

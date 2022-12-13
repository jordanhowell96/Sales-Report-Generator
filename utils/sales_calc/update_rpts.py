from ..models import ProductSaleData


def update_prod_rpt(prod_rpt, prod_name, revenue, units_sold, disc_cost):
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


def update_team_rpt(team_rpt, team_name, revenue):
    if team_name in team_rpt.keys():
        team_rpt[team_name] += revenue
    else:
        team_rpt.update({team_name: revenue})

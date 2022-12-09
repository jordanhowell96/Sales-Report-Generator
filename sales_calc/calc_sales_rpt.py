# Defines function for calculating team and product reports from a team map, sales data, and product master.

from .exceptions import ProductNotFoundError, TeamNotFoundError


def calc_sales_rpt(*,
                   team_map: dict[int, str],
                   prod_master: dict[int, dict[str, str | float | int]],
                   sales_data: tuple[tuple[int, int, int, int, float]]
                   ) -> tuple[dict[str, float], dict[str, dict[str, float | int]]]:
    """
        Calculates the team report and product report from the team map, product master, and sales data

        :param team_map: dict with key = team id (int), value = team name (str)
        :param prod_master: dict with key = product id,
                                value = dict of product information
                                ("Name": str, "Price": float, "Lot Size": int)
        :param sales_data: tuple of tuples where each is a row of sales data
                                (sale id, product id, team id, quantity, discount)
                                all int except discount

        :returns: tuple of two dicts where the first dict contains team report information with

            key = team name (str),
            value = revenue (float)

            and the second dict contains product report information with

            key = product name (str),
            value = dict of product information
                ("GrossRevenue": float, "TotalUnits": int, "DiscountCost": float)

        :raises ProductNotFoundError if a product id in the sales data does not exist in the product master
        :raises TeamNotFoundError if a team id in the sales data does not exist in the team map
    """

    # Initialize output dicts
    team_rpt: dict[str, float] = {}
    prod_rpt: dict[str, dict[str, float | int]] = {}

    # Iterate through sales
    sale: tuple[int, int, int, int, float]
    for sale in sales_data:

        sale_id: int
        prod_id: int
        team_id: int
        lots_sold: int
        discount: float
        sale_id, prod_id, team_id, lots_sold, discount = sale

        # Get product info
        prod_info: dict[str, str | float | int] = prod_master.get(prod_id)
        if not prod_info:
            raise ProductNotFoundError(prod_id)

        # Get team name
        team_name: str = team_map.get(team_id)
        if not team_name:
            raise TeamNotFoundError(team_id)

        units_sold: int = lots_sold * prod_info["LotSize"]
        revenue: float = units_sold * prod_info["UnitPrice"]
        disc_cost: float = revenue * discount / 100

        # Update team report =======================================
        if team_name in team_rpt.keys():
            team_rpt[team_name] += revenue
        else:
            team_rpt.update({team_name: revenue})

        # Update product report ====================================
        this_prod_rpt: dict[str, float | int] = prod_rpt.get(prod_info["Name"])
        if this_prod_rpt is not None:
            this_prod_rpt["GrossRevenue"] += revenue
            this_prod_rpt["TotalUnits"] += units_sold
            this_prod_rpt["DiscountCost"] += disc_cost
        else:
            prod_rpt.update(
                {prod_info["Name"]: {
                    "GrossRevenue": revenue,
                    "TotalUnits": units_sold,
                    "DiscountCost": disc_cost}})

    return team_rpt, prod_rpt

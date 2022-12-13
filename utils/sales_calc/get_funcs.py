from .exceptions import ProductNotFoundError, TeamNotFoundError
from ..models import Product


def get_product(prod_master: dict[int, Product], prod_id: int, hide_exc: bool) -> Product:
    """
        Gets product information from a product id

        :param prod_master: dict with key = product id (int), value = Product
        :param prod_id: id of a product (int)
        :param hide_exc: bool to specify if exceptions should be hidden from console

        :return: product information dataclass (Product)

        :raises ProductNotFoundError if a product id in the sales data does not exist in the product master
            and hide_exc = False
    """
    product: Product = prod_master.get(prod_id)

    if not product:
        if hide_exc:
            print(f"Error: Product ID {prod_id} not found in team map.")
            exit()
        raise ProductNotFoundError(prod_id)

    return product


def get_team(team_map: dict[int, str], team_id: int, hide_exc: bool) -> str:
    """
        Gets the team name from a team id

        :param team_map: dict with key = team id (int), value = team name (str)
        :param team_id: id of a team (int)
        :param hide_exc: bool to specify if exceptions should be hidden from console

        :return: name of team (str)

        :raises TeamNotFoundError if a team id in the sales data does not exist in the team map
            and hide_exc = False
    """
    team_name: str = team_map.get(team_id)

    if not team_name:
        if hide_exc:
            print(f"Error: Team ID {team_id} not found in product master.")
            exit()
        raise TeamNotFoundError(team_id)

    return team_name

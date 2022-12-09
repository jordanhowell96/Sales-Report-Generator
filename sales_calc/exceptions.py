# Defines exceptions for sales_calc module

class TeamNotFoundError(Exception):
    """Defines exception for when a team ID is not found"""

    def __init__(self, team_id):
        message = f"Team ID {team_id} not found in product master file."
        super().__init__(message)


class ProductNotFoundError(Exception):
    """Defines exception for when a product ID is not found"""

    def __init__(self, product_id):
        message = f"Product ID {product_id} not found in team map file."
        super().__init__(message)

import unittest
from decimal import Decimal
from ..get_funcs import get_product
from ..exceptions import ProductNotFoundError
from ...models import Product


class TestGetTeam(unittest.TestCase):
    """Test case for get_team"""

    @classmethod
    def setUpClass(cls) -> None:
        cls.prod_master: dict[int, Product] = {
            1: Product(
                name="Product A",
                unit_price=Decimal(35.5),
                lot_size=10),
            2: Product(
                name="Product B",
                unit_price=Decimal(45.21),
                lot_size=1),
        }

    def test_get_team(self) -> None:
        """Test with valid product ID"""
        expected_product: Product = get_product(self.prod_master, 1, False)
        self.assertEqual(expected_product.name, "Product A")

    def test_raises_error(self) -> None:
        """Test with invalid product ID"""
        team_map = {1: "Team A", 2: "Team B"}
        self.assertRaises(ProductNotFoundError, get_product, team_map, 3, False)


if __name__ == "__main__":
    unittest.main()

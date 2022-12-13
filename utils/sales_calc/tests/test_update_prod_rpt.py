import unittest
from decimal import Decimal
from ...models import ProductSaleData
from ..update_rpts import update_prod_rpt


class TestUpdateProdRpt(unittest.TestCase):
    """Test case for update_prod_rpt"""

    def setUp(self) -> None:
        """Set up test case with a set of data"""

        self.prod_rpt: dict[str, ProductSaleData] = {
            "Product A": ProductSaleData(gross_rev=Decimal(100), units_sold=10, disc_cost=Decimal(10))
        }

    def test_update_prod_rpt_update_existing(self) -> None:
        """Test updating an existing product in the product report"""

        prod_name: str = "Product A"

        update_prod_rpt(prod_rpt=self.prod_rpt,
                        prod_name=prod_name,
                        gross_rev=Decimal(50),
                        units_sold=5,
                        disc_cost=Decimal(5))

        self.assertEqual(self.prod_rpt[prod_name].gross_rev, Decimal(150))
        self.assertEqual(self.prod_rpt[prod_name].units_sold, 15)
        self.assertEqual(self.prod_rpt[prod_name].disc_cost, Decimal(15))

    def test_update_prod_rpt_add_new(self) -> None:
        """Test adding a new product to the product report"""

        prod_name_a: str = "Product A"
        prod_name_b: str = "Product B"

        update_prod_rpt(prod_rpt=self.prod_rpt,
                        prod_name=prod_name_b,
                        gross_rev=Decimal(75),
                        units_sold=10,
                        disc_cost=Decimal(2))

        self.assertEqual(self.prod_rpt[prod_name_a].gross_rev, Decimal(50))
        self.assertEqual(self.prod_rpt[prod_name_a].units_sold, 5)
        self.assertEqual(self.prod_rpt[prod_name_a].disc_cost, Decimal(5))

        self.assertEqual(self.prod_rpt[prod_name_b].gross_rev, Decimal(75))
        self.assertEqual(self.prod_rpt[prod_name_b].units_sold, 10)
        self.assertEqual(self.prod_rpt[prod_name_b].disc_cost, Decimal(2))


if __name__ == "__main__":
    unittest.main()

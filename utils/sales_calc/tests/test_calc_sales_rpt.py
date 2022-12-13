import unittest
from decimal import Decimal
from ...models import Product, ProductSaleData, Sale
from ..calc_sales_rpt import calc_sales_rpt


class CalcSalesRptGeneralTest(unittest.TestCase):
    """Test case for calc_sales_rpt"""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up test case with a set of data"""

        # Test Values ============================

        team_map: dict[int, str] = {1: "Team A", 2: "Team B", 3: "Team C"}

        prod_master: dict[int, Product] = {
            1: Product(
                name="Product A",
                unit_price=Decimal(35.5),
                lot_size=10),
            2: Product(
                name="Product B",
                unit_price=Decimal(45.21),
                lot_size=1),
            3: Product(
                name="Product C",
                unit_price=Decimal(9.87),
                lot_size=35)
        }

        sales_data: tuple = tuple(
            (Sale(prod_id=1, team_id=2, lots_sold=5, discount=Decimal(0)),
             Sale(prod_id=1, team_id=1, lots_sold=1, discount=Decimal(5)),
             Sale(prod_id=2, team_id=2, lots_sold=20, discount=Decimal(10)),
             Sale(prod_id=3, team_id=1, lots_sold=10, discount=Decimal(100)),
             Sale(prod_id=3, team_id=3, lots_sold=40, discount=Decimal(2))
             ))

        # Expected outputs =======================

        cls.expected_team_rpt: dict[str, Decimal] = {
            "Team A": Decimal(3809.5),
            "Team B": Decimal(2679.2),
            "Team C": Decimal(13818)
        }

        cls.expected_prod_rpt: dict[str, ProductSaleData] = {
            "Product A": ProductSaleData(
                gross_rev=Decimal(2130),
                total_units=60,
                disc_cost=Decimal(17.75)),
            "Product B": ProductSaleData(
                gross_rev=Decimal(904.2),
                total_units=20,
                disc_cost=Decimal(90.42)),
            "Product C": ProductSaleData(
                gross_rev=Decimal(17272.5),
                total_units=1750,
                disc_cost=Decimal(3730.86))
        }

        # Actual Outputs =========================

        cls.actual_team_rpt: dict[str, float]
        cls.actual_prod_rpt: dict[str, ProductSaleData]
        cls.actual_team_rpt, cls.actual_prod_rpt = calc_sales_rpt(team_map=team_map,
                                                                  sales_data=sales_data,
                                                                  prod_master=prod_master)

    def assert_team_rpt_rev_equal(self, team: str) -> None:
        """Tests if a test team gross revenue is as expected"""

        if team not in self.actual_team_rpt.keys():
            raise AssertionError(f"{team} test team not found in Team Report")

        elif round(self.expected_team_rpt[team], 2) != round(self.actual_team_rpt[team], 2):
            raise AssertionError(f"Expected {team} test team revenue "
                                 f"({round(self.expected_team_rpt[team], 2)}) does not equal "
                                 f"actual {team} test team revenue "
                                 f"({round(self.actual_team_rpt[team], 2)}).")

    def assert_prod_rpt_rev_equal(self, product: str) -> None:
        """Tests if a test product gross revenue is as expected"""

        if product not in self.actual_prod_rpt.keys():
            raise AssertionError(f"{product} test product not found in Product Report")

        elif round(self.expected_prod_rpt[product].gross_rev, 2) \
                != round(self.actual_prod_rpt[product].gross_rev, 2):
            raise AssertionError(f"Expected {product} test product revenue "
                                 f"({round(self.expected_prod_rpt[product].gross_rev, 2)}) does not equal "
                                 f"actual {product} test product revenue "
                                 f"({round(self.actual_prod_rpt[product].gross_rev, 2)}).")

    def assert_prod_rpt_units_equal(self, product: str) -> None:
        """Tests if a test product units sold is as expected"""

        if product not in self.actual_prod_rpt.keys():
            raise AssertionError(f"{product} test product not found in Product Report")

        elif self.expected_prod_rpt[product].total_units != self.actual_prod_rpt[product].total_units:
            raise AssertionError(f"Expected {product} test product units sold does not equal "
                                 f"actual {product} test product units sold.")

    def assert_prod_rpt_disc_cost_equal(self, product: str) -> None:
        """Tests if a test product discount cost is as expected"""

        if product not in self.actual_prod_rpt.keys():
            raise AssertionError(f"{product} test product not found in Product Report")

        elif round(self.expected_prod_rpt[product].disc_cost, 2) \
                != round(self.actual_prod_rpt[product].disc_cost, 2):
            raise AssertionError(f"Expected {product} test product discount cost does not equal "
                                 f"actual {product} test product discount cost..")

    def test_team_a_rev(self):
        """Test Team A revenue accuracy"""
        self.assert_team_rpt_rev_equal("Team A")

    def test_team_b_rev(self):
        """Test Team B revenue accuracy"""
        self.assert_team_rpt_rev_equal("Team B")

    def test_team_c_rev(self):
        """Test Team C revenue accuracy"""
        self.assert_team_rpt_rev_equal("Team C")

    def test_prod_a_rev(self):
        """Test Product A gross revenue accuracy"""
        self.assert_prod_rpt_rev_equal("Product A")

    def test_prod_b_rev(self):
        """Test Product B gross revenue accuracy"""
        self.assert_prod_rpt_rev_equal("Product B")

    def test_prod_c_rev(self):
        """Test Product C gross revenue accuracy"""
        self.assert_prod_rpt_rev_equal("Product C")

    def test_prod_a_units(self):
        """Tests Product A units sold accuracy"""
        self.assert_prod_rpt_units_equal("Product A")

    def test_prod_b_units(self):
        """Tests Product B units sold accuracy"""
        self.assert_prod_rpt_units_equal("Product B")

    def test_prod_c_units(self):
        """Tests Product C units sold accuracy"""
        self.assert_prod_rpt_units_equal("Product C")

    def test_prod_a_disc_cost(self):
        """Tests Product A discount cost accuracy"""
        self.assert_prod_rpt_disc_cost_equal("Product A")

    def test_prod_b_disc_cost(self):
        """Tests Product B discount cost accuracy"""
        self.assert_prod_rpt_disc_cost_equal("Product B")

    def test_prod_c_disc_cost(self):
        """Tests Product C discount cost accuracy"""
        self.assert_prod_rpt_disc_cost_equal("Product C")


if __name__ == '__main__':
    unittest.main()

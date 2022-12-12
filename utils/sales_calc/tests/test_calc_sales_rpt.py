import unittest
from ...models import Product, ProductSaleData, Sale
from ..calc_sales_rpt import calc_sales_rpt


class TestCalcSalesRpt(unittest.TestCase):
    def test_1(self):
        team_map: dict[int, str] = {1: "Team A", 2: "Team B", 3: "Team C"}
        prod_master: dict[int, Product] = {
            1: Product(
                name="Product A",
                unit_price=35.5,
                lot_size=10),
            2: Product(
                name="Product B",
                unit_price=45.21,
                lot_size=1),
            3: Product(
                name="Product C",
                unit_price=9.87,
                lot_size=35)
        }
        sales_data: tuple = tuple(
            (Sale(prod_id=1, team_id=2, lots_sold=5, discount=0),
             Sale(prod_id=1, team_id=1, lots_sold=1, discount=5),
             Sale(prod_id=2, team_id=2, lots_sold=20, discount=10),
             Sale(prod_id=3, team_id=1, lots_sold=10, discount=100),
             Sale(prod_id=3, team_id=3, lots_sold=40, discount=2)
             ))

        # expected_team_rpt: dict[str, float] = {"Team A": ,"Team B":, "Team C":}
        # expected_prod_rpt: dict[str, ProductSaleData]

        team_report: dict[str, float]
        prod_report: dict[str, ProductSaleData]
        team_report, prod_report = calc_sales_rpt(team_map=team_map,
                                                  sales_data=sales_data,
                                                  prod_master=prod_master)

        # self.assertEqual(team_report, expected_team_rpt)
        # self.assertEqual(prod_report, expected_prod_rpt)


if __name__ == '__main__':
    unittest.main()

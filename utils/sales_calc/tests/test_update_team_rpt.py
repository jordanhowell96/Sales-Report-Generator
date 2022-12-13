import unittest
from decimal import Decimal
from ..update_rpts import update_team_rpt


class TestUpdateTeamRpt(unittest.TestCase):
    """Test case for update_prod_rpt"""

    def setUp(self) -> None:
        """Set up test case with a set of data"""

        self.team_rpt: dict[str, Decimal] = {
            "Team A": Decimal(100),
        }

    def test_update_prod_rpt_update_existing(self) -> None:
        """Test updating an existing product in the product report"""

        team_name: str = "Team A"

        update_team_rpt(team_rpt=self.team_rpt,
                        team_name=team_name,
                        gross_rev=Decimal(50))

        self.assertEqual(self.team_rpt[team_name], Decimal(150))

    def test_update_prod_rpt_add_new(self) -> None:
        """Test adding a new product to the product report"""

        team_name_a: str = "Team A"
        team_name_b: str = "Team B"

        update_team_rpt(team_rpt=self.team_rpt,
                        team_name=team_name_b,
                        gross_rev=Decimal(50))

        self.assertEqual(self.team_rpt[team_name_a], Decimal(100))
        self.assertEqual(self.team_rpt[team_name_b], Decimal(50))


if __name__ == "__main__":
    unittest.main()

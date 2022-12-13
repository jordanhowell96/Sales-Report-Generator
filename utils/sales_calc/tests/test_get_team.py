import unittest
from ..get_funcs import get_team
from ..exceptions import TeamNotFoundError


class TestGetTeam(unittest.TestCase):
    """Test case for get_team"""

    @classmethod
    def setUpClass(cls) -> None:
        """Set up test case with a set of data"""
        cls.team_map: dict[int, str] = {1: "Team A", 2: "Team B"}

    def test_get_team(self) -> None:
        """Test with valid team ID"""
        expected_team: str = get_team(self.team_map, 1, False)
        self.assertEqual(expected_team, "Team A")

    def test_raises_error(self) -> None:
        """Test with invalid team ID"""
        self.assertRaises(TeamNotFoundError, get_team, self.team_map, 3, False)


if __name__ == "__main__":
    unittest.main()

# Defines functions for writing the team report, and product report csv files.

import csv
from .config import DEFAULT_TEAM_RPT_FILE, DEFAULT_PROD_RPT_FILE, DESTINATION_FOLDER


def write_team_rpt(file_name: str | None, team_rpt: dict[str, float]) -> None:
    """
        Writes a csv file from data in the team report dictionary

        :param file_name: optional name of the file to write
        :param team_rpt: team report dict with key = team name (str), value = revenue (float)

        :return: None

        :raises FileNotFoundError if DESTINATION_FOLDER cannot be found
    """

    if file_name is None:
        # Use default file name from config.py
        file_name = DEFAULT_TEAM_RPT_FILE

        print(f"Sales file not specified. Default used: {file_name}")
        print("To change this, run again with --team-report={name of file}\n")

    # Create list of rows to write to file from the team report
    file_rows: list[tuple[str, str]] = [(team, f"{revenue:.2f}")
                                        for team, revenue in team_rpt.items()]

    # Sort and add header
    file_rows.sort(key=lambda r: float(r[1]), reverse=True)
    file_rows.insert(0, ("Team", "GrossRevenue"))

    with open(f"{DESTINATION_FOLDER}\\{file_name}", 'w', newline='') as outfile:
        file_writer = csv.writer(outfile)

        for row in file_rows:
            file_writer.writerow(row)


def write_prod_rpt(file_name: str | None,
                   prod_rpt: dict[str, dict[str, float | int]]
                   ) -> None:
    """
        Writes a csv file from data in the team report dictionary

        :param file_name: optional name of the file to write
        :param prod_rpt: product report dict with
            key = product name (str),
            value = dictionary of product information
                ("GrossRevenue": float, "TotalUnits": int, "DiscountCost": float)

        :return: None

        :raises FileNotFoundError if DESTINATION_FOLDER cannot be found
    """

    if file_name is None:
        # Use default file name from config.py
        file_name: str = DEFAULT_PROD_RPT_FILE

        print(f"Sales file not specified. Default used: {file_name}")
        print("To change this, run again with --product-report={name of file}\n")

    # Create list of rows to write to file from the product report
    file_rows: list[tuple] = [(
        name,
        f"{data['GrossRevenue']:.2f}",
        data["TotalUnits"],
        f"{data['DiscountCost']:.2f}")
        for name, data in prod_rpt.items()]

    # Sort and add header
    file_rows.sort(key=lambda r: float(r[1]), reverse=True)
    file_rows.insert(0, ("Name", "GrossRevenue", "TotalUnits", "DiscountCost"))

    with open(f"{DESTINATION_FOLDER}\\{file_name}", 'w', newline='') as outfile:
        file_writer = csv.writer(outfile)

        for row in file_rows:
            file_writer.writerow(row)

# Defines functions for writing the team report, and product report csv files.

import csv
from .config import DEFAULT_TEAM_RPT_FILE, DEFAULT_PROD_RPT_FILE, DESTINATION_FOLDER
from ..models import ProductSaleData


def write_outfile(input_path: str, file_rows: list) -> str:

    file_path = input_path
    success: bool = False
    tries = 0
    while success is False:
        try:
            with open(file_path, 'w', newline='') as outfile:
                file_writer = csv.writer(outfile)

                for row in file_rows:
                    file_writer.writerow(row)

            success = True

        except PermissionError:
            tries += 1
            if tries == 1:
                file_path += "(1)"
            else:
                file_path = file_path[:-2] + str(tries) + ")"
    if file_path != input_path:
        print("Warning: File")
    return file_path


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

    # Write file
    file_path = f"{DESTINATION_FOLDER}\\{file_name}"
    write_outfile(file_path, file_rows)

    print(f"Team report file written at {file_path}\n")


def write_prod_rpt(file_name: str | None,
                   prod_rpt: dict[str, ProductSaleData]
                   ) -> None:
    """
        Writes a csv file from data in the team report dictionary

        :param file_name: optional name of the file to write
        :param prod_rpt: product report dict with
            key = product name (str),
            value = ProductSaleData

        :return: None

        :raises FileNotFoundError if DESTINATION_FOLDER cannot be found
    """

    if file_name is None:
        # Use default file name from config.py
        file_name: str = DEFAULT_PROD_RPT_FILE

        print(f"Sales file not specified. Default used: {file_name}")
        print("To change this, run again with --product-report={name of file}\n")

    # Create list of rows to write to file from the product report
    file_rows: list[tuple[str, str, int | str, str]] = [(
        name,
        f"{data.gross_rev:.2f}",
        data.total_units,
        f"{data.disc_cost:.2f}")
        for name, data in prod_rpt.items()]

    # Sort and add header
    file_rows.sort(key=lambda r: float(r[1]), reverse=True)
    file_rows.insert(0, ("Name", "GrossRevenue", "TotalUnits", "DiscountCost"))

    # Write file
    file_path = f"{DESTINATION_FOLDER}\\{file_name}"
    file_path = write_outfile(file_path, file_rows)

    print(f"Product report file written at {file_path}\n")

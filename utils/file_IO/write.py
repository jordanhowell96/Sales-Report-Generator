# Defines functions for writing the team report, and product report csv files.

import csv
from decimal import Decimal
from .config import DEFAULT_TEAM_RPT_FILE, DEFAULT_PROD_RPT_FILE, DESTINATION_FOLDER
from ..models import ProductSaleData


def write_outfile(file_name: str, file_rows: list) -> bool:
    """
        Generic function to write an output file

        :param file_name: name of the file to write (str or None)
        :param file_rows: tuple of rows to write to the file

        :return: bool indicating if file was successfully written
    """

    if file_name[-4:] != ".csv":
        print("Error: Output files must be specified as .csv files\n")
        return False

    success = False
    file_path = f"{DESTINATION_FOLDER}\\{file_name}"

    try:
        with open(file_path, 'w', newline='') as outfile:
            file_writer = csv.writer(outfile)

            # Write rows
            for row in file_rows:
                file_writer.writerow(row)

        success = True

    except PermissionError:
        print(f"Error: Cannot write file at {file_path}. Ensure the file is closed.")

    except FileNotFoundError:
        print(f"Error: Output folder ({DESTINATION_FOLDER}) not found.\n")

    return success


def write_team_rpt(file_name: str | None, team_rpt: dict[str, Decimal]) -> None:
    """
        Writes a csv file from data in the team report dictionary

        :param file_name: optional name of the file to write (str or None)
        :param team_rpt: team report dict with
            key = team name (str),
            value = revenue (Decimal)

        :return: None
    """

    if file_name is None:
        # Use default file name from config.py
        file_name = DEFAULT_TEAM_RPT_FILE

        print(f"Sales file not specified. Default used: {file_name}")
        print("To change this, run again with --team-report={name of file}\n")

    # Create list of rows to write to file from the team report
    file_rows: list[tuple[str, str]] = [(team, f"{round(revenue, 2):.2f}")
                                        for team, revenue in team_rpt.items()]

    # Sort and add header
    file_rows.sort(key=lambda r: float(r[1]), reverse=True)
    file_rows.insert(0, ("Team", "GrossRevenue"))

    # Write file
    success = write_outfile(file_name, file_rows)

    if success:
        print(f"Success: Team report file written at {DESTINATION_FOLDER}\\{file_name}\n")


def write_prod_rpt(file_name: str | None,
                   prod_rpt: dict[str, ProductSaleData]
                   ) -> None:
    """
        Writes a csv file from data in the team report dictionary

        :param file_name: optional name of the file to write (str or None)
        :param prod_rpt: product report dict with
            key = product name (str),
            value = ProductSaleData

        :return: None
    """

    if file_name is None:
        # Use default file name from config.py
        file_name: str = DEFAULT_PROD_RPT_FILE

        print(f"Sales file not specified. Default used: {file_name}")
        print("To change this, run again with --product-report={name of file}\n")

    # Create list of rows to write to file from the product report
    file_rows: list[tuple[str, str, int | str, str]] = [(
        name,
        f"{round(data.gross_rev, 2):.2f}",
        data.units_sold,
        f"{round(data.disc_cost, 2):.2f}")
        for name, data in prod_rpt.items()]

    # Sort and add header
    file_rows.sort(key=lambda r: float(r[1]), reverse=True)
    file_rows.insert(0, ("Name", "GrossRevenue", "TotalUnits", "DiscountCost"))

    # Write file
    success = write_outfile(file_name, file_rows)

    if success:
        print(f"Success: Product report file written at {DESTINATION_FOLDER}\\{file_name}\n")

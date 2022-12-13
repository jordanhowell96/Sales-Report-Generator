# Defines functions for reading the team map, product master, and sales csv files.

import csv
from decimal import Decimal
from ..models import Product, Sale
from .config import DEFAULT_PROD_MASTER_FILE, DEFAULT_SALES_FILE, \
    DEFAULT_TEAM_MAP_FILE, SOURCE_FOLDER


def read_infile(file_name: str) -> tuple[list[str]]:
    """
        Generic read function for an input file

        :param file_name: name of source file (str)

        :returns: tuple of file contents
    """

    if file_name[-4:] != ".csv":
        print("Error: Input files must be specified as .csv files")
        exit()

    file_path = f"{SOURCE_FOLDER}\\{file_name}"

    try:
        with open(file_path, 'r', encoding="utf-8") as infile:
            csv_rows: tuple[list[str]] = tuple(csv.reader(infile))

    except FileNotFoundError:
        print(f"Error: Input file not found at {file_path}\n")
        exit()

    return csv_rows


def read_prod_master(file_name: str | None = None) -> dict[int, Product]:
    """
        Reads product master file and returns a dictionary of product information from data in the file

        :param file_name: optional name of the file to be read (str or None)

        :returns: dictionary with key = product id (int), value = product info (Product)
    """

    if file_name is None:
        # Use default file name from config.py
        file_name = DEFAULT_PROD_MASTER_FILE

        print(f"Product Master file not specified. Default used: {file_name}")
        print("To change this, run again with --product-master={name of file} or -p {name of file}\n")

    csv_rows = read_infile(file_name)

    # Create product master output dict
    prod_master: dict[int, Product] = {}

    try:

        for row in csv_rows:

            prod_master.update({
                int(row[0]):
                    Product(name=row[1],
                            unit_price=Decimal(row[2]),
                            lot_size=int(row[3]))
            })

        return prod_master

    except (ValueError, IndexError):

        print(f"Error: Product Master input file ({SOURCE_FOLDER}\\{file_name}) is invalid.")
        print("Ensure the the data in the file is as follows:")
        print("     Column 1: int (Product ID)")
        print("     Column 2: string (Name)")
        print("     Column 3: float (Price)")
        print("     Column 4: int (Lot Size)")
        exit()


def read_sales(file_name: str | None = None) -> tuple[Sale]:
    """
        Reads sales file and returns a tuple of sales data from data in the file

        :param file_name: optional name of the file to be read (str or None)

        :returns: tuple of sales data (Sale)
    """

    if file_name is None:
        # Use default file name from config.py
        file_name = DEFAULT_SALES_FILE

        print(f"Sales file not specified. Default used: {file_name}")
        print("To change this, run again with --sales={name of file} or -s {name of file}\n")

    csv_rows: tuple[list[str]] = read_infile(file_name)

    # Create sales data output tuple
    try:

        sales_data: tuple[Sale] = tuple(
            Sale(
                prod_id=int(sale[1]),
                team_id=int(sale[2]),
                lots_sold=int(sale[3]),
                discount=Decimal(sale[4])
            )
            for sale in csv_rows)

        return sales_data

    except (ValueError, IndexError):

        print(f"Error: Sales Data input file ({SOURCE_FOLDER}\\{file_name}) is invalid.")
        print("Ensure the the data in the file is as follows:")
        print("     Column 1: int (Sale ID)")
        print("     Column 2: int (Product ID)")
        print("     Column 3: int (Team ID)")
        print("     Column 4: int (Lots Sold)")
        print("     Column 4: float (Discount)")
        exit()


def read_team_map(file_name: str | None = None) -> dict[int, str]:
    """
        Reads team map file and returns a dictionary of the team names from data in the file

        :param file_name: optional name of the file to be read (str or None)

        :returns: dictionary with key = team id (int), value = team name (str)
    """

    if file_name is None:
        # Use default file name from config.py
        file_name: str = DEFAULT_TEAM_MAP_FILE

        print(f"Team Map file not specified. Default used: {file_name}")
        print("To change this, run again with --team-map={name of file} or -t {name of file}\n")

    csv_rows: tuple[list[str]] = read_infile(file_name)

    # Create team map output dict
    try:
        team_map: dict[int, str] = {int(row[0]): row[1] for row in csv_rows[1:]}

        return team_map

    except (ValueError, IndexError):

        print(f"Error: Team Map input file ({SOURCE_FOLDER}\\{file_name}) is invalid.")
        print("Ensure the the data in the file is as follows:")
        print("     Column 1: int (Team ID)")
        print("     Column 2: string (Name)")
        exit()

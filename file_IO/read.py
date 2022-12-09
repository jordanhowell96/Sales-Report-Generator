# Defines functions for reading the team map, product master, and sales csv files.

import csv
from .config import DEFAULT_TEAM_MAP_FILE, DEFAULT_PROD_MASTER_FILE, \
    DEFAULT_SALES_FILE, SOURCE_FOLDER


def read_team_map(file_name: str | None = None) -> dict[int, str]:
    """
        Reads team map file and returns a dictionary of the team names from data in the file

        :param file_name: optional name of the file to be read (str or None)

        :returns: dictionary with key = team id (int), value = team name (str)

        :raises FileNotFoundError if the sales file cannot be found at {SOURCE_FOLDER}/{file_name}
    """

    if file_name is None:
        # Use default file name from config.py
        file_name = DEFAULT_TEAM_MAP_FILE

        print(f"Team Map file not specified. Default used: {file_name}")
        print("To change this, run again with --team-map={name of file} or -t {name of file}\n")

    file_location: str = f"{SOURCE_FOLDER}\\{file_name}"

    with open(file_location, 'r', encoding="utf-8") as infile:
        csv_rows: tuple = tuple(csv.reader(infile))

    team_map: dict[int, str] = {int(row[0]): row[1] for row in csv_rows[1:]}

    return team_map


def read_prod_master(file_name: str | None = None) -> dict[int, dict[str, str | float | int]]:
    """
        Reads product master file and returns a dictionary of product information from data in the file

        :param file_name: optional name of the file to be read (str or None)

        :returns: dictionary with key = product id (int),
                    value = dictionary of product information ("Name": str, "Price": float, "Lot Size": int)

        :raises FileNotFoundError if the sales file cannot be found at {SOURCE_FOLDER}/{file_name}
    """

    if file_name is None:
        # Use default file name from config.py
        file_name = DEFAULT_PROD_MASTER_FILE

        print(f"Product Master file not specified. Default used: {file_name}")
        print("To change this, run again with --product-master={name of file} or -p {name of file}\n")

    with open(f"{SOURCE_FOLDER}\\{file_name}", 'r', encoding="utf-8") as infile:
        csv_rows: tuple = tuple(csv.reader(infile))

    prod_master: dict[int, dict[str, str | float | int]] = {}

    # Create output dict
    for row in csv_rows:
        prod_master.update({
            int(row[0]): {
                "Name": row[1],
                "UnitPrice": float(row[2]),
                "LotSize": int(row[3])
            }
        })

    return prod_master


def read_sales(file_name: str | None = None) -> tuple[tuple[int, int, int, int, float]]:
    """
        Reads sales file and returns a tuple of sales data from data in the file

        :param file_name: optional name of the file to be read (str or None)

        :returns: tuple of tuples where each is a row of sales data
                    (sale id (int), product id (int), team id (int), quantity (int), discount (float))

        :raises FileNotFoundError if the sales file cannot be found at {SOURCE_FOLDER}/{file_name}
    """

    if file_name is None:
        # Use default file name from config.py
        file_name = DEFAULT_SALES_FILE

        print(f"Sales file not specified. Default used: {file_name}")
        print("To change this, run again with --sales={name of file} or -s {name of file}\n")

    with open(f"{SOURCE_FOLDER}\\{file_name}", 'r', encoding="utf-8") as infile:
        csv_rows: tuple = tuple(csv.reader(infile))

    # Save csv rows as tuple of tuples and convert first 4 columns to ints and last column to float
    sales_data: tuple = tuple(
        map(lambda sale:
            tuple(map(int, sale[:4]))
            + (float(sale[4]),),
            csv_rows))

    return sales_data

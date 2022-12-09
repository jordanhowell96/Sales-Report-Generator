# Defines function for parsing user command line arguments for file locations

import argparse


def parse_input() -> argparse.Namespace:
    """
        Parses user arguments in command line to get input and output file names

        :returns: Namespace of command line args
    """

    parser = argparse.ArgumentParser(description="place holder")

    parser.add_argument("-t", "--team-map",
                        type=str,
                        dest="team_map_fn",
                        help="place holder")

    parser.add_argument("-p", "--product-master",
                        type=str,
                        dest="prod_master_fn",
                        help="place holder")

    parser.add_argument("-s", "--sales",
                        type=str,
                        dest="sales_fn",
                        help="place holder")

    parser.add_argument("--team-report",
                        type=str,
                        dest="team_report_fn",
                        help="place holder")

    parser.add_argument("--product-report",
                        type=str,
                        dest="prod_report_fn",
                        help="place holder")

    return parser.parse_args()

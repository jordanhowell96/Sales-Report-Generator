# Defines function for parsing user command line arguments for file locations

import argparse


def parse_input() -> argparse.Namespace:
    """
        Parses user arguments in command line to get input and output file names

        :returns: Namespace of command line args
    """

    parser = argparse.ArgumentParser(description=
                                     "Reads data from a team map file, a product master file, and a sales file "
                                     "then calculates team reports and product reports, "
                                     "and finally writes these reports to output files. "
                                     "The file names and locations have defaults set in utils/file_IO/config.py, "
                                     "but may be overwritten by command line arguments specified below. "
                                     "See README for more information.")

    parser.add_argument("-t", "--team-map",
                        type=str,
                        dest="team_map_fn",
                        help="Name of the team map .csv input file")

    parser.add_argument("-p", "--product-master",
                        type=str,
                        dest="prod_master_fn",
                        help="Name of the product master .csv input file")

    parser.add_argument("-s", "--sales",
                        type=str,
                        dest="sales_fn",
                        help="Name of the sales .csv input file")

    parser.add_argument("--team-report",
                        type=str,
                        dest="team_report_fn",
                        help="Name of the team report .csv output file")

    parser.add_argument("--product-report",
                        type=str,
                        dest="prod_report_fn",
                        help="Name of the product report .csv output file")

    return parser.parse_args()

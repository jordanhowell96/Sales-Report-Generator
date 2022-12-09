# This program reads data from a team map file, a product master file, and a sales file
# then calculates team reports and product reports,
# and finally writes these reports to output files.
# The file names and locations have defaults set in file_IO/config.py, but may be overwritten by
# command line arguments. See README for more information.

import parser
import file_IO
import sales_calc
from argparse import Namespace


# TODO: Test cases (non-csv, empty files, etc)
# TODO: Write tests
# TODO: Documentation (readme and cl hints)

def main() -> None:
    # Parse command line arguments
    cl_args: Namespace = parser.parse_input()

    # Read input files
    team_map: dict[int, str] = file_IO.read_team_map(cl_args.team_map_fn)
    prod_master: dict[int, dict[str, str | float | int]] = file_IO.read_prod_master(cl_args.prod_master_fn)
    sales_data: tuple[tuple[int, int, int, int, float]] = file_IO.read_sales(cl_args.sales_fn)

    # Calculate report data
    team_report: dict[str, float]
    prod_report: dict[str, dict[str, float | int]]
    team_report, prod_report = sales_calc.calc_sales_rpt(team_map=team_map,
                                                         sales_data=sales_data,
                                                         prod_master=prod_master)

    # Write output files
    file_IO.write_team_rpt(cl_args.team_report_fn, team_report)
    file_IO.write_prod_rpt(cl_args.prod_report_fn, prod_report)


if __name__ == "__main__":
    main()

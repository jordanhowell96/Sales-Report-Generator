# This program reads data from a team map file, a product master file, and a sales file
# then calculates team reports and product reports,
# and finally writes these reports to output files.
# The file names and locations have defaults set in utils/file_IO/config.py, but may be overwritten by
# command line arguments. See README for more information.

from utils import parser, sales_calc, file_IO
from utils.models import Product, ProductSaleData, Sale
from argparse import Namespace


def main() -> None:
    """
        Main function for generating team and product reports
        using files specified by command line arguments
    """

    # Parse command line arguments
    cl_args: Namespace = parser.parse_input()

    # Read input files
    team_map: dict[int, str] = file_IO.read_team_map(cl_args.team_map_fn)
    prod_master: dict[int, Product] = file_IO.read_prod_master(cl_args.prod_master_fn)
    sales_data: tuple[Sale] = file_IO.read_sales(cl_args.sales_fn)

    # Calculate report data
    team_report: dict[str, float]
    prod_report: dict[str, ProductSaleData]

    team_report, prod_report = sales_calc.calc_sales_rpt(team_map=team_map,
                                                         sales_data=sales_data,
                                                         prod_master=prod_master,
                                                         hide_exc=True)

    # Write output files
    file_IO.write_team_rpt(cl_args.team_report_fn, team_report)
    file_IO.write_prod_rpt(cl_args.prod_report_fn, prod_report)


if __name__ == "__main__":
    main()

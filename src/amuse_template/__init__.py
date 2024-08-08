"""
Script to run this module. Needs to be modified before it can be used.
"""

import sys
import argparse
from amuse.units import units


def new_argument_parser(args):
    """
    Creates a command line argument parser. Call the script with "-h" to show options and default values.
    """
    parser = argparse.ArgumentParser(
        args,  # defaults to sys.argv[1:], but can be any list.
        # The 'argparse.ArgumentDefaultsHelpFormatter' fomatter_class whill show the default value in the help.
        formatter_class=argparse.ArgumentDefaultsHelpFormatter,
    )
    parser.add_argument(
        "-M",
        "--mass",  # optional longer argument name.
        dest="mass",  # name of the argument.
        type=units.MSun,  # any dtype (int, float, str, bool) or AMUSE unit can be used here.
        default=1.0 | units.MSun,  # default value, don't forget the unit when the type is a unit.
        help="Mass of the star",  # Help string, don't repeat the default value here.
    )
    parser.add_argument(
        "-n",
        "--number_of_stars",
        dest="number_of_stars",
        type=int,
        default=1000,
        help="Number of stars",
    )
    return parser.parse_args()


def main():
    args = new_argument_parser(sys.argv[1:])
    print(args.mass, args.number_of_stars)

#!/usr/bin/env python3
"""
    Purpose:
        Profile Some Functions

    Steps:
        - Define two Functions
        - Profile Them
        - Compare Them

    function call: python3.6 profile_functions.py
"""

# Python Library Imports
import logging
import os
import sys
from argparse import ArgumentParser

# Local Library Imports
from profiler_helpers import profiler_decorator


def main():
    """
    Purpose:
        Read an .avro File
    """
    logging.info("Starting The Profiling Process")

    opts = get_options()

    x = 1

    import pdb; pdb.set_trace()

    x_or = or_conditional(x)

    import pdb; pdb.set_trace()

    x_in = in_conditional(x)

    import pdb; pdb.set_trace()

    logging.info("The Profiling Process Complete")


###
#
###


@profiler_decorator()
def or_conditional(x):
    """
    Purpose:
        Test if x is == 1 or 2 or 3 or 4
    Args:
        x (Int): A number to check
    Returns:
        x_found (Boolean): Whether or not X was found
    """

    if x == 1 or x == 2 or x == 3 or x == 4:
        logging.info(f"{x} == 1 or 2 or 3 or 4")
        return True

    return False


@profiler_decorator()
def in_conditional(x):
    """
    Purpose:
        Test if x is in (1, 2, 3, 4)
    Args:
        x (Int): A number to check
    Returns:
        x_found (Boolean): Whether or not X was found
    """

    if x in (1, 2, 3, 4):
        logging.info(f"{x} in (1, 2, 3, 4)")
        return True

    return False


###
# General/Helper Methods
###


def get_options():
    """
    Purpose:
        Parse CLI arguments for script
    Args:
        N/A
    Return:
        N/A
    """

    parser = ArgumentParser(description="Profile Functions")
    required = parser.add_argument_group('Required Arguments')
    optional = parser.add_argument_group('Optional Arguments')

    # Optional Arguments
    # N/A

    # Required Arguments
    # N/A

    return parser.parse_args()


if __name__ == "__main__":

    log_level = logging.INFO
    logging.getLogger().setLevel(log_level)
    logging.basicConfig(
        stream=sys.stdout,
        level=log_level,
        format="[profile_functions] %(asctime)s %(levelname)s %(message)s",
        datefmt="%a, %d %b %Y %H:%M:%S"
    )

    try:
        main()
    except Exception as err:
        print(
            "{0} failed due to error: {1}".format(os.path.basename(__file__), err)
        )
        raise err

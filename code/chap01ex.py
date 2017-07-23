"""This file contains code for use with "Think Stats",
by Allen B. Downey, available from greenteapress.com

Copyright 2014 Allen B. Downey
License: GNU GPLv3 http://www.gnu.org/licenses/gpl.html
"""

from __future__ import print_function

import numpy as np
import sys

import nsfg
import thinkstats2


def main(script):
    """Tests the functions in this module.

    script: string script name
    """
    # print('%s: All tests passed.' % script)
    df = read_fem_resp()

    print("No pregnancies:\t {}".format(get_pregnum_recode(df, 0)))
    print("1 pregnancy:\t {}".format(get_pregnum_recode(df, 1)))
    print("2 pregnancies:\t {}".format(get_pregnum_recode(df, 2)))
    print("3 pregnancies:\t {}".format(get_pregnum_recode(df, 3)))
    print("4 pregnancies:\t {}".format(get_pregnum_recode(df, 4)))
    print("5 pregnancies:\t {}".format(get_pregnum_recode(df, 5)))
    print("6 pregnancies:\t {}".format(get_pregnum_recode(df, 6)))
    print("7 or more preg:\t {}".format(get_pregnum_recode(df, 7)))
    print(get_pregnum_recode(read_fem_resp()))

          
def get_pregnum_recode(fem_resp_df=None, value=0):
    if (value == 7):
        return fem_resp_df[fem_resp_df.pregnum>=value].pregnum.count()
    return fem_resp_df[fem_resp_df.pregnum==value].pregnum.count()


def read_fem_resp(dct_file='2002FemResp.dct',
                  dat_file='2002FemResp.dat.gz',
                  nrows=None):
    """Reads the NSFG respondent data.

    dct_file: string file name
    dat_file: string file name

    returns: DataFrame
    """
    dct = thinkstats2.ReadStataDct(dct_file)
    df = dct.ReadFixedWidth(dat_file, compression='gzip', norws=nrows)
    return df


if __name__ == '__main__':
    main(*sys.argv)

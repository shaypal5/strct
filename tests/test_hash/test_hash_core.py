"""Test hash functions."""

import sys
import pickle

from scipy import sparse

from strct.hash import stable_hash

from .gen_hasg_xgb import get_xgb_kwargs


def test_stable_hash():
    if sys.version_info.major == 3:
        if sys.version_info.minor >= 6:
            expected_val = 5461671350068481966
        else:
            expected_val = -8814990287216496045
    else:
        raise Exception("This test is meant for Python 3!")
    listi = [3, 23.2, '23']
    assert stable_hash(listi) == expected_val

    if sys.version_info.major == 3:
        if sys.version_info.minor >= 6:
            expected_val2 = -7233202952208267009
        else:
            expected_val2 = 4894511948741237771
    else:
        raise Exception("This test is meant for Python 3!")
    listi2 = [34, {'a': 23, 'g': [1, '43']}]
    assert stable_hash(listi2) == expected_val2

    if sys.version_info.major == 3:
        if sys.version_info.minor >= 6:
            expected_val3 = -1643351000552175288
        else:
            expected_val3 = -4531592806763782902
    else:
        raise Exception("This test is meant for Python 3!")
    dicti = {'a': 23, 'b': [234, 'g'], 'c': {4: 'go'}}
    assert stable_hash(dicti) == expected_val3


def test_xgb_kwargs_hashing():
    if sys.version_info.major == 3:
        if sys.version_info.minor >= 6:
            expected_val = 5461671350068481966
        else:
            expected_val = -8814990287216496045
    else:
        raise Exception("This test is meant for Python 3!")
    xgb_kwargs = get_xgb_kwargs()
    hashval = stable_hash(xgb_kwargs)
    assert hashval == expected_val


"""Generating what we'll test for in the hash xgb kwargs test."""

import os
import pickle
import pathlib

import numpy as np
from scipy import sparse

from strct.hash import stable_hash


M = 100
N = 50

DPATH = pathlib.Path(__file__).parent.absolute()
X_FPATH = os.path.join(DPATH, 'xgb_x.pkl')
Y_FPATH = os.path.join(DPATH, 'xgb_y.pkl')


def get_xgb_kwargs():
    with open(X_FPATH, 'rb') as f:
        X = pickle.load(f)
    with open(Y_FPATH, 'rb') as f:
        y = pickle.load(f)
    return {
        'X': X,
        'y': y,
        'base_score': 0.5,
        'booster': 'gbtree',
        'colsample_bylevel': 1,
        'learning_rate': 0.3,
        'max_delta_step': 0,
        'max_depth': 12,
        'min_child_weight': 1,
        'missing': None,
    }


if __name__ == '__main__':
    X = sparse.random(
        m=M,
        n=N,
        format='csr',
    )
    y = np.random.rand(M)
    with open(X_FPATH, 'wb+') as f:
        pickle.dump(X, f)
    with open(Y_FPATH, 'wb+') as f:
        pickle.dump(y, f)
    xgb_kwargs = get_xgb_kwargs()
    hashval = stable_hash(xgb_kwargs)
    print(hashval)

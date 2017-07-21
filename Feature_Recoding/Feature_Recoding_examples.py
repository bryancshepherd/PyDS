# If using Python 2.X don't forget:
# from __future__ import division

# Bring in some toy data.
# Scikit-learn has a nice little
# collection of toy datasets, we'll
# make use of.

from sklearn import datasets
import pandas as pd
import numpy as np

iris = datasets.load_iris()

data1 = pd.DataFrame(data= np.c_[iris['data'], iris['target']],
                     columns= iris['feature_names'] + ['target'])


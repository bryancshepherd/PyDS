# If using Python 2.X don't forget:
# from __future__ import division

# Bring in some toy data.
# Scikit-learn has a nice little
# collection of toy datasets, we'll
# make use of.

import pandas as pd
import numpy as np

# Bring in some toy data from the UCI
# Machine Learning Repository. We'll use
# flag data from Collins Gem Guide to Flags, 1986:
# https://archive.ics.uci.edu/ml/datasets/Flags

# Pandas makes it easy to pull the data from an
# online source:

flags = pd.read_csv('https://archive.ics.uci.edu/ml/'
                    'machine-learning-databases/flags/flag.data',
                    header=None,
                    names = ['name','landmass','zone','area',
                             'population','language','religion',
                             'bars','stripes','colours','red',
                             'green','blue','gold','white','black',
                             'orange','mainhue','circles','crosses',
                             'saltires','quarters','sunstars','crescent',
                             'triangle','icon','animate','text',
                             'topleft','botright'])

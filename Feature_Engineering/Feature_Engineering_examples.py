# If using Python 2.X don't forget:
# from __future__ import division

# Bring in some toy data.
# Scikit-learn has a nice little
# collection of toy datasets, we'll
# make use of.

import pandas as pd

# Bring in some toy data from the UCI
# Machine Learning Repository:
# http://archive.ics.uci.edu/ml/index.php
# We'll use
# Abalone data from here:
# https://archive.ics.uci.edu/ml/datasets/Abalone

# Pandas makes it easy to pull the data from an
# online source:
snails = pd.read_csv('https://archive.ics.uci.edu/ml/'
                     'machine-learning-databases/abalone/abalone.data',
                     header=None,
                     names = ['Sex', 'Length', 'Diameter',
                              'Height', 'Whole_weight', 'Shucked_weight',
                              'Viscera_weight', 'Shell_weight', 'Rings'])

snails.to_csv('./Feature_Engineering/Data/snails.csv', index=False)

# First we get to know the data a little.
snails.head()
snails.describe()

# Basic feature creation. Create an `age` feature
# based on the number of rings.
snails['age'] = snails.Rings + 1.5

# But that's about as easy as it gets
# for feature engineering. Let's say we wanted
# to do something more complicated, like create
# a categorical representation of age.

snails.age.describe()

# Let's call the snails younger than
# 9.5 years `young`, the snails older than
# 12.5 `old`, and anything in between
# `middle-aged`.

# A large percent of feature creation tasks will
# require a task specific function that gets applied
# using the pandas `apply` method.

def create_age_categories(x):
    '''
    Groups Abalone ages into 'Young', 'Middle-aged',
    and 'Old'
    :param x: Numeric series
    :return: String series
    '''

    if x<9.5:
        return 'Young'

    elif x>12.5:
        return 'Old'

    else:
        return 'Middle-aged'

snails['categorical_age'] = snails.age.apply(create_age_categories)
snails.head()

# Turns out our algorithm needs categories expressed
# as integers.
# Simple mappings of a few categories
# are often best done with `map`.

age_to_int = {'Young':1,
              'Middle-aged':2,
              'Old':3}

snails['categorical_age_int'] = snails.categorical_age.map(age_to_int)
snails.head()

# We could have also done this all at once by
# using `apply` on the entire dataset.
# We need to first update our function to
# work on the dataset instead of a single
# series.

snails_method_2 = pd.read_csv('./Feature_Engineering/Data/snails.csv')

def create_both_age_categories(df):
    '''
    Add age classifications to the Abalone dataset.

    :param df: Dataframe with ring count series labelled 'Rings'
    :return: Dataframe with categorical age features added
    '''

    df['age']=df.Rings + 1.5

    if df.age<9.5:
        df['categorical_age']='Young'
        df['categorical_age_int']=1

    elif df.age>12.5:
        df['categorical_age']='Old'
        df['categorical_age_int']=3

    else:
        df['categorical_age']='Middle-aged'
        df['categorical_age_int']=2

    return df

snails_method_2 = snails.apply(create_both_age_categories, axis=1)
snails_method_2.head()

# Prove to ourselves the two methods do
# the same thing
snails.equals(snails_method_2)

# Something you may be tempted to do is use a for loop.
# Don't. It's usually a terrible way to generate features.
# However, a list comprehension is conceptually similar
# and is generally a good solution.
snails['Old'] = [1 if x>12.5 else 0 for x in snails.age]
snails.head()

### Performance considerations
import timeit

setup = '''
import pandas as pd
snails = pd.read_csv('./Feature_Engineering/Data/snails.csv')
                              
snails['age'] = snails.Rings + 1.5

def create_old_indicator(x):
    if x>12.5:
        return 1
    else:
        return 0
'''

# Using apply on a series
timeit.timeit('snails.age.apply(create_old_indicator)',
              setup = setup,
              number=500)

# Using a list comprehension on a series
timeit.timeit('[1 if x>12.5 else 0 for x in snails.age]',
              setup = setup,
              number=500)


## What about apply vs. map?
setup = '''
import pandas as pd
snails = pd.read_csv('./Feature_Engineering/Data/snails.csv')

snails['age'] = snails.Rings + 1.5

snails['cat_age_desc'] = ['Old' if x>12.5 else 'Not-old' for x in snails.age]

def create_age_categories_int(x):

    if x=='Old':
        return 1

    else:
        return 0
        
age_to_int = {'Old':1,
              'Not-old':0}
'''

# Using apply on a series
timeit.timeit('snails.cat_age_desc.apply(create_age_categories_int)',
              setup = setup,
              number=500)

# Using a list comprehension on a series
timeit.timeit('snails.cat_age_desc.map(age_to_int)',
              setup = setup,
              number=500)

# Numpy arrays almost always beat pandas performance,
# but aren't always necessary.
setup = '''
import pandas as pd
import numpy as np
df = pd.DataFrame(np.random.randn(1000, 10000))
df.columns = ['var_' + str(x) for x in df.columns]

df_array = np.array(df)
'''

timeit.timeit('(df.var_101 + df.var_102)/df.var_103',
              setup=setup,
              number=5000)

timeit.timeit('(df_array[:,101]+df_array[:,102])/df_array[:,103]',
              setup=setup,
              number=5000)
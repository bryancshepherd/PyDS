import sklearn.datasets as datasets

# Option 1. Pick a dataset from Scikit's dataset library
# https://scikit-learn.org/stable/datasets/index.html#toy-datasets
# By default data is returned as a 'Bunch' and can be accessed
# via 'data' and 'target' attributes
iris = datasets.load_iris()
iris.feature_names

# Option 2. Download a larger dataset from the sklearn online datasets collection.
housing = datasets.fetch_california_housing()
housing.data

# Option 3. Create your own data with sklearn's helpers
multilabel_data = datasets.make_multilabel_classification(n_samples=1000,
                                                          n_features=10,
                                                          random_state=1234)

# Option 4. OpenML database 
from sklearn.datasets import fetch_openml
ozone = fetch_openml(name='ozone-level-8hr')  # see openml.org to get data details
ozone.data
                                                      
# More information and details on the datasets can be found here:
# https://scikit-learn.org/stable/datasets/index.html
# https://scikit-learn.org/stable/modules/generated/sklearn.datasets.load_iris.html#sklearn.datasets.load_iris

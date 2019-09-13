import pandas as pd 

# Step 1. Visit UCI Machine Learning Repository
# https://archive.ics.uci.edu/ml/datasets.php

# Step 2. Choose a data set. Click on the link 
# to the data set's detailed information.

# Step 3. Click on the 'Data Folder' to be taken to the download location

# Step 4. Right-click on the link to the data file (usually the file ending in .data)

# Step 5. Use the link as the first parameter in pd.read_csv
url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'

df = pd.read_csv(url)
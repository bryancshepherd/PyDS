import pandas as pd 

# Step 1. Find a webpage with tabular data. 
# E.g., RealClearPolitics 2020 polling data
url = "https://www.realclearpolitics.com/epolls/" \
      "2020/president/us/2020_democratic_presidential_nomination-6730.html"
data = pd.read_html(url)

# Each table is pulled down as a different dataframe in the data object
data[0]
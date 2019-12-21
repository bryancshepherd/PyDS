import sqlite3
import pandas as pd 

# Setup: Create a dataframe
names = ['sex', 'length', 'diameter',
         'height', 'wholewgt', 'shuckedwgt',
         'viscerawgt', 'shellwgt', 'rings']

url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'

df = pd.read_csv(url, names=names)

# Step 1. Create a connection to the database. If 
# the database doesn't exist, this creates it.
conn = sqlite3.connect('abalonedb.db')

# Step 2. Write the dataframe to a database
df.to_sql('snails', conn)

# Step 3. Treat the connection just like you would any other
qry = """SELECT * FROM snails WHERE sex = 'M' LIMIT 5"""
dfsubset = pd.read_sql(qry,conn)

# For cleanliness, close the connection
conn.close()


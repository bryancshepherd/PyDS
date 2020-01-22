"""Keep your data science code classy"""

import sqlite3
import pandas as pd
import numpy as np


class SnailData:
    """Class for manipulating and storing snail data"""

    def __init__(self,
                 data_source,
                 project_name,
                 sample_location):
        self.data_source = data_source
        self.project_name = project_name
        self.sample_location = sample_location
        self.df = None

    def import_data(self):
        names = ['sex', 'length', 'diameter',
                 'height', 'wholewgt', 'shuckedwgt',
                 'viscerawgt', 'shellwgt', 'rings']

        self.df = pd.read_csv(self.data_source, names=names)

    def recode(self):
        self.df['wholewgt_sqr'] = self.df['wholewgt']**2
        self.df['length_log'] = np.log(self.df['length'])
        self.df['project_name'] = self.project_name
        self.df['sample_location'] = self.sample_location

    def export_data(self):
        # Create a connection to the database. If
        # the database doesn't exist, this creates it.
        conn = sqlite3.connect('abalonedb_class.db')

        # Write the dataframe to a database
        self.df.to_sql('snails', conn)

        # Housekeeping
        conn.close()


url = 'https://archive.ics.uci.edu/ml/machine-learning-databases/abalone/abalone.data'

snail_data = SnailData(url, 'AstroSnail Project 1', 'Mars')

snail_data.import_data()
snail_data.recode()
snail_data.export_data()

db_conn = sqlite3.connect('abalonedb_class.db')
pd.read_sql("select * from snails", db_conn)

# More Information
# Python Classes Documentation
# https://docs.python.org/3/tutorial/classes.html

# Python Classes w3schools Intro
# https://www.w3schools.com/python/python_classes.asp

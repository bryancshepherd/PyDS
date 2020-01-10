"""Geocoding with Census API"""

import io
import requests

import pandas as pd

# Pull in address data
address_data_org = pd.read_csv('./HotTakes/data/census_geocoding/Addresses.csv', dtype = 'str', header=None)

address_data = pd.DataFrame()

# We only have 3 cases in our sample data. Embiggen it to make it
# look a little more realistic.
for i in range(100):
    address_data = pd.concat([address_data, address_data_org])

# Just a little housecleaning
address_data.reset_index(inplace=True, drop=True)

# The Census API expects data in a certain format. The column names
# aren't really needed, but they're helpful for us humans.
address_cols = ['unique_id', 'street', 'city', 'state', 'zip']
address_data.columns = address_cols

# The Census API requires a unique identifier,
# it's also good practice to have one in general, so we add it here.
address_data['unique_id'] = range(1, len(address_data)+1)

# The Census API requires that any fields with commas be double quoted.
# The test data has no issues, but this is an example of how we
# could just remove all the commas.
address_data[address_cols] = address_data[address_cols].replace({',': ' '},
                                                                regex=True)

# Here we write a csv file that our POST request will include.
# The Census API has a batch-size limit of 10k, so if the data
# is larger than that it needs to be broken into 10k batches.
# You may also want to use a smaller subset of your data for testing
# until you have everything working.
address_data.loc[0:10, :].to_csv('./HotTakes//data/census_geocoding/new_addresses_0_10.csv',
                                 header=False, index=False)

# A string that identifies the location of the file we just created
file_name = './HotTakes/data/new_addresses_0_10.csv'

class CensusData:
    """Class to get and hold census geocoding data"""

    def __init__(self, file_name):
        self.url = 'https://geocoding.geo.census.gov/geocoder/geographies/addressbatch/'
        self.payload = {'benchmark': 'Public_AR_Current',
                        'vintage': 'Current_Current'}
        self.file_name = file_name
        self.output_col_names = ['unique_id',
                                 'input_address',
                                 'match_indicator',
                                 'match_type',
                                 'matched_to_address',
                                 'long_lat',
                                 'tiger_line_id',
                                 'tiger_line_side',
                                 'state_fips',
                                 'county_fips',
                                 'tract_code',
                                 'block_code']

    # Mostly needed for merging demographics on later
    def _add_pretty_state_names(self):
        # Bring in state identifier cross walk
        state_abbrevs = pd.read_table(
            './HotTakes/data/census_geocoding/acs/state_abbrevs.txt',
            sep='|',
            dtype='str')

        state_abbrevs['STATE'] = state_abbrevs['STATE'].astype(int)

        # Add state crosswalk data
        self.df = self.df.merge(state_abbrevs,
                                how='left',
                                left_on='state_fips',
                                right_on='STATE')

    # Comment for what the request will look like
    def geocode(self):
        self.files = {'addressFile': open(self.file_name, 'rb')}
        r = requests.post(self.url, data=self.payload, files=self.files)

        # Get the data from the request result
        self.df = pd.read_csv(io.StringIO(r.text),
                              header=None,
                              names=self.output_col_names)
        self._add_pretty_state_names()
        return self.df

census_data = CensusData(file_name)

census_data.geocode()

census_data.df.to_csv('/Users/bryanshepherd/Projects/CensusBrownBag/'
                      'data/census_geocoding/prepped_data/new_geocoderesult.csv')

# Additional Information:
# Geocoding steps
# Go here: https://geocoding.geo.census.gov/

# Technical Documentation
# https://www.census.gov/data/developers/data-sets/Geocoding-services.html

# https://www.census.gov/programs-surveys/geography/technical-documentation
# /complete-technical-documentation/census-geocoder.html

# Other Census APIs
# https://www.census.gov/data/developers/data-sets.html



                                 





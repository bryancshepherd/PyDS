from __future__ import division

## Importing modules/packages:
import pandas
import pandas as pd
from pandas import DataFrame


## Data types:

### Values:
boolean_thing = True
numeric_thing = 25
string_thing = 'Call me Ishmael'


type(boolean_thing)

[type(x) for x in [boolean_thing, numeric_thing, string_thing]]


### Containers:

# Unordered, WYSIWYG
list_thing = ['thing_1', 2, 'thing 3']

# Ordered, unique values. Not indexable
set_thing = {'thing_A', 'thing_B', 'thing_C', 'thing_C', 'zee other thing'}

# Key/value pairs, indexable by key
dict_thing = {'favorite color':'blue', 
              'favorite number':17,
              'favorite orange': 'Valencia'}

set_thing

dict_thing

### Control flow:
for i in range(5):
    print('i is {}'.format(i))

# If/elif/else
x = 1

if (x == 1):
    print ('x is 1')
elif (x == 2):
    print ('x is 2')
else:
    print ('These are not the droids you\'re looking for.')


### Defining functions:
def fizz_buzz(fizz=2, buzz=5, range_min=5, range_max=25):
    for x in range(range_min, range_max+1):
        text = ''
        if x % fizz == 0:
            text = text + 'Fizz' # Or text += 'Fizz'
        
        if x % buzz == 0:
            text = text + 'Buzz' # Or text += 'Buzz'
        
        if text == '':
            text = x
        
        print(text)

fizz_buzz()


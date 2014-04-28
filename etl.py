'''Helper functions related to data acquisition and conversion'''

import re

def get_inches(ft_in):
    '''Get inches from str formatted ft' in" as float.'''
    ft_in = str(ft_in)
    inches_re = re.compile(r'[0-9]\' (.*)\"')
    if re.search(inches_re, ft_in):
        return float(re.search(inches_re, ft_in).groups(0)[0].strip())
    else:
        return 0.0

def get_feet(ft_in):
    '''Get feet from str formatted ft' in" as int.'''
    ft_in = str(ft_in)
    feet_re = re.compile(r'(^[0-9]{1,2})')
    if re.search(feet_re, ft_in):
        return int(re.search(feet_re, x).groups(0)[0])
    else:
        return 0

def total_inches(str_series):
    '''Takes a pandas Series of str formatted ft' in" i.e. 6' 8.5" and returns float Series of total inches.''' 
    inches = str_series.apply(get_inches)
    feet = str_series.apply(get_feet)
    return feet*12 + inches
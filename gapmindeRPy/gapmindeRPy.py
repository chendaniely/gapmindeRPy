import pkg_resources
from io import StringIO

import pandas as pd

def gapminder():
    content = pkg_resources.resource_string('gapmindeRPy', 'gapminder.tsv').decode()
    return pd.read_csv(StringIO(content), sep='\t')

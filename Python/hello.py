import sys
import csv
from turtle import update
import pandas as pd
import re
import numpy as np
if sys.version_info[0] < 3: 
    from StringIO import StringIO
else:
    from io import StringIO

with open(sys.argv[1], 'r') as f:
    contents = f.read()
 
print(contents)
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


rule_list = []
r = re.compile('')
rule_list += r.sub("", contents).split("\n")

rules_columns = []

for rule in rule_list:
    boken_rule = []
    boken_rule += r.sub("", rule).split(" ")
    
    for field in boken_rule:
        s = field.find('-')
        c = field in rules_columns
        if ((s!=-1) and (c == False)):
            rules_columns.append(field)
            continue

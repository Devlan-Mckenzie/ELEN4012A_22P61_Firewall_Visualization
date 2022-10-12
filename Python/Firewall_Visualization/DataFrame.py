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


def generateDataFrame(fileName):
    filePath = "Python\\Firewall_Visualization\\" + fileName
    try:
        with open(filePath, 'r') as f:
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

        for col in rules_columns:
            p=0
            for rule_ in rule_list:
                b = rule_.find(col)
                if b == -1:
                    rule_list[p] = rule_list[p] + col + " $ "
                p+=1
        #print(len(col))
        updated_content =' '.join(map(str,rule_list))

        rules = []
        clean_rules = []
        rr = re.compile('\n')
        clean_rules += rr.sub("", updated_content).split(" ")      


        for q in rules_columns:
            fields = []
            i=1
            add = False
            for x in clean_rules:
                if x == q:
                    fields.append(clean_rules[i])
                    add = True
                i+=1
            rules.append(fields)

        a=0
        dict = {}
        while a < len(rules_columns):
            dict[rules_columns[a]]=rules[a]
            a+=1
        #print(col)
        df = pd.DataFrame(dict)
        print(df)   
        return df
    except:
        print("An error occured when trying to create the dataframe using that filename")
    
    
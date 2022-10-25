import sys
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
contents = contents.replace('-','')
# contents = contents.replace('.','P')
# contents = contents.replace('/','R')

#import dd.autoref as _bdd
from dd import autoref as _bdd

rule_list = []
r = re.compile('')
rule_list += r.sub("", contents).split("\n")

play_rules = []
rules_columns = []

for rule in rule_list:
    broken_rule = []
    broken_rule += r.sub("", rule).split(" ")
    
    for field in broken_rule:
        s = field.find('-')
        c = field in rules_columns
        if ((s!=-1) and (c == False)):
            rules_columns.append(field)
            continue
    play_rules.append(broken_rule)
print(play_rules)

bdd = _bdd.BDD()

IP_list =[]
for RULE in play_rules:
    IP_addr = []
    for FIELD in RULE:
        s = FIELD.find('.')
        if s!=-1 : 
            IP_addr +=  r.sub("", FIELD).split(".")
            IP_list.append(IP_addr)
            for o in IP_addr:
                bdd.declare(o)
                #print(o)
                continue
        bdd.declare(FIELD)
        #print(FIELD)
        #print(FIELD)

for run in play_rules:
    i = 0
    rule_exp =[]
    
    while i < len(run):
        a = run[i]
        b = run[i+1]
        s= r'{a}/\{b}'.format(b=b,a=a)
        print(s)
       # c = bdd.add_expr(s)
        # print(c)
        # print(s)
        i+=2
        if a == "j":
            state_ = c
            continue
        rule_exp.append(c)

    # n = rule_exp[0]    
    # rule_bdd = r'{state_} <=> {n}'.format(state_=state_,n=n)
    # o=bdd.to_expr(rule_bdd)
#print(play_rules)
# for col in rules_columns:
#     p=0
#     for rule_ in rule_list:
#         b = rule_.find(col)
#         if b == -1:
#             rule_list[p] = rule_list[p] + col + " $ "
#         p+=1

# updated_content =' '.join(map(str,rule_list))

# rules = []
# clean_rules = []
# rr = re.compile('\n')
# clean_rules += rr.sub("", updated_content).split(" ")      


# for q in rules_columns:
#     fields = []
#     i=1
#     add = False
#     for x in clean_rules:
#         if x == q:
#             fields.append(clean_rules[i])
#             add = True
#         i+=1
#     rules.append(fields)


# a=0
# dict = {}
# while a < len(rules_columns):
#     dict[rules_columns[a]]=rules[a]
#     a+=1
# #print(col)
# df = pd.DataFrame(dict)


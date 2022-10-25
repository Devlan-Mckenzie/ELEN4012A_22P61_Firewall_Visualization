from pyeda.inter import *

import Rule
f = expr("a & b | a & c | b & c")
print(f)
f = expr2bdd(f)
print(f)
# a,b,c = map(bddvar,'abc')
# type(a)
# isinstance(a,BinaryDecisionDiagram)
# a0 = bddvar('a',0)
# print(a0)
# b_a_0_1 = bddvar(('a','b'), (0,1))
# #b.a[0,1] not working 
# X = bddvars('x',4,4)
# print(X)
# f = a & b | a & c | b & c
# print(f)
# f.restrict({a: 0})
# print(f)
# f.restrict({a:1, b:0})
# print(f)
# f.restrict({a:1,b:1})
# print(f)
# print(list(f.satisfy_all()))

# lets try make a rule as a boolean expression 
a = 1
b = 2
c = 1
boolean_Rule = expr((a > b)|(a < c)|('test' == "test"))
print(boolean_Rule)
boolean_Rule = expr2bdd(boolean_Rule)
print(boolean_Rule)
# this shows that numbers and string can be used together 
# This equates to direct boolean equations and thus allows for direct comparison of a request packet and a rule 

def generateBoolExpression(packet:Rule,rule:Rule):
    # This function should take in a rule and convert it into a boolean expression 
    # For now its assumed that the test packet takes the same form as a rule and can be used to compare the two 

    # Going to test if an exact copy of the rule is tested, will it pass through 
    boolean_Rule = expr((packet.A_Flag == rule.A_Flag) & (packet.S_Flag == rule.S_Flag) & (packet.J_Flag == rule.J_Flag) & (packet.P_Flag == rule.P_Flag) & (packet.M_Flag == rule.M_Flag) & (packet.State_Flag == rule.State_Flag) & (packet.Dport_Flag == rule.Dport_Flag))
    print(boolean_Rule)
    return(boolean_Rule)

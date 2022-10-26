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

def generateFieldBoolExpressions(rule:Rule):
    # This function will take  in a rule and convert each field into a variabvle for the BDD in this way each node is a single field
    # This will result in a BDD for the entire rule with each node representing a field in a rule 

    # Going to have each field as an expression and then use the and operator to make them all link
    # For now this is simple logic and more advanced logic should check if the fields exist and go from there
    # Currently cannot simply add the fields and will likely need to add a variable to the BDD to represent them
    # Going to create a set of expression variable to represent each field possible in a rule
    A_Flag_Bool = exprvar("A_Flag_Bool")
    S_Flag_Bool = exprvar("S_Flag_Bool")
    J_Flag_Bool = exprvar("J_Flag_Bool")
    P_Flag_Bool = exprvar("P_Flag_Bool")
    M_Flag_Bool = exprvar("M_Flag_Bool")
    State_Flag_Bool = exprvar("State_Flag_Bool")
    Dport_Flag_Bool = exprvar("Dport_Flag_Bool")

    # can now implement some logic to check the passed rule fields exist etc and based on that create a more refined boolean rule
    # Using the truth table will allow for simple evaluation of rules 
    # then once a single rule has been converted into an expression correctly I believe they can be stored in either an farray (function array) or one can potentially 
    # store the expression variables in an array using A = exprvars('a',4,4). Ideally the expression will be stored and then added together at the end to create the 
    # entire ruleset as a BDD
    
    #By using logic one can set the variables as well to limit the truth table size 
    # This has been tested and seen to work with the below code
    A_Flag_Bool = expr(1)
    S_Flag_Bool = expr(1)
    J_Flag_Bool = expr(0)

    boolean_Rule = expr((A_Flag_Bool) & (S_Flag_Bool) & (J_Flag_Bool) & (P_Flag_Bool) & (M_Flag_Bool) & (State_Flag_Bool) & (Dport_Flag_Bool))
    print(boolean_Rule)
    print('This is the truth table for a rule \n')
    print(expr2truthtable(boolean_Rule))
    return(boolean_Rule)
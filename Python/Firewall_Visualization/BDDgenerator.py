from ast import If
from pickle import TRUE
from pyeda.inter import *

import Rule
import Ruleset

#f = expr("a & b | a & c | b & c")
#print(f)
#f = expr2bdd(f)
#print(f)
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
# a = 1
# b = 2
# c = 1
# boolean_Rule = expr((a > b)|(a < c)|('test' == "test"))
# #print(boolean_Rule)
# boolean_Rule = expr2bdd(boolean_Rule)
#print(boolean_Rule)
# this shows that numbers and string can be used together 
# This equates to direct boolean equations and thus allows for direct comparison of a request packet and a rule 



# def generateBoolExpression(packet:Rule,rule:Rule):
# def generateBoolExpression(rule:Rule):
#     # This function should take in a rule and convert it into a boolean expression 
#     # For now its assumed that the test packet takes the same form as a rule and can be used to compare the two 

#     # Going to test if an exact copy of the rule is tested, will it pass through 
#     boolean_Rule = expr((packet.A_Flag == rule.A_Flag) & (packet.S_Flag == rule.S_Flag) & (packet.J_Flag == rule.J_Flag) & (packet.P_Flag == rule.P_Flag) & (packet.M_Flag == rule.M_Flag) & (packet.State_Flag == rule.State_Flag) & (packet.Dport_Flag == rule.Dport_Flag))
#     #print(boolean_Rule)

#     return(boolean_Rule)

def generateBoolExpression(ruleCode,fieldCode):
    # size = len(ruleCode)
    # k = 2**size
    # val =''
    # while k>0:
    #     if k==1:
    #         val+='1'
    #         k-=1
    #         continue
    #     val+='0'
    #     k-=1
    # # for code in ruleCode:
    # #     if ruleCode[code] == 'ACCEPT':
    # #         val+="1"
    # #         continue
    # #     val +="0"
   
    # print(ruleCode)
    # X = exprvars('x', size)
    # f = truthtable(X, val)
    
    # print(f)

    ruleBool=''
    for tag in fieldCode:
        #To check if this is the first iteration of the loop, which errored before as the ruleBool was '' which was not an expression term
        if ruleBool == '':
            ruleBool = makeExpression(tag,ruleCode[tag])
        else:
            ruleBool = (ruleBool & makeExpression(tag,ruleCode[tag])) 
        #print("rule = ",ruleBool)
        # print("val = ",ruleCode[tag])  
        # print(makeExpression(tag,ruleCode[tag])) 
    
    # Functionality has changed and no longer only checks for the accept value
    op=getRuleStatus(ruleCode)
    # stat = expr(1)
    # if op == "ACCEPT":
    #     ruleBool=expr(1)
    # else:
    #     ruleBool=expr(0)
    
    return ruleBool

def makeExpression(tag,flag):
    tag = exprvar( r'{a}'.format(a=tag))
    flag = exprvar( r'{b}'.format(b=flag))
    s = tag & flag
    f = expr2truthtable(s)
    # print(truthtable2expr(f))
    return expr(flag)

def getRuleStatus(rule:Rule):
    # It appears that the rule flags property is not set or detected as a parameter however the '-j' flag is set as a property which I have called here
    # The functionality should remain the same as before
    #return rule.ruleFlags['-j']
    try:
        return rule['-j']
    except:
        return 'NULL'

    

def generateBDDBoolExpression(ruleset:Ruleset,fields:Ruleset): 
    if len(ruleset)==0:
        print("Cannot generate boolean expression")
    else:
        ruleBook = ''
        i=0
        while i<len(ruleset):
            # Need to check if the rule contains a j flag so moving the getRuleStatus to the start of the loop which can check before any actions are taken
            if getRuleStatus(ruleset[i]) == 'NULL':
                # The rule has no j flag or the j flag is drop 
                i+=1
                continue 
            else:
                print("Rule has a flag status")

            # Added an if statement to check if this is the first iteration of the loop, which errored before as the ruleBool was '' which was not an expression term
            if ruleBook == '':
                ruleBook = (generateBoolExpression(ruleset[i],fields[i]))
            else:
                ruleBook = (ruleBook | (generateBoolExpression(ruleset[i],fields[i])))
            
            print(ruleBook)
            
            i+=1
        return ruleBook



def generateBDDfromExpr(exprRules:Expression):
    # Take in an expression and return a bdd
    # It might be possible to reorder the bdd in a more optimized way using the following line of code
    # However in order to use this method one would need to rename the variables which may prove difficult due to the dynamic nature of the bdd variables
    #composedOutputBDD = outputBDD.compose()
    #print(len(_NODES))
    #for x in list(outputBDD.satisfy_all()):
        #print(x)
    #####################################################################
    # This errors out as the nonetype  has no properties called names 
    # To get around this fact I have used the simplify command on the expressions which has resolved the issue 
    # The exact origin of the issue remains unknown at this time however
    
    simplifiedExprRules = exprRules.simplify()
    outputBDD = expr2bdd(simplifiedExprRules)
    
    #####################################################################
    from pyeda.boolalg.bdd import _NODES
    print('The number of nodes required to implement the BDD is ' + str(len(_NODES)))
    return outputBDD

# This function will take in 2 bdds and compare them for functional equivalence and return an answer 
def compareBDDs(firstBDD:BinaryDecisionDiagram, secondBDD:BinaryDecisionDiagram):
    try:
        if(firstBDD.equivalent(secondBDD)):
            print("The BDDs are equivalent")
        else:
            print("The BDDs are not equivalent with one another")
        return
    except:
        print("An error occured, please ensure that you have loaded both ruleset 1 and ruleset 2 prior to using this function")
        return

# This function checks to see if a packet would pass through the bdd
def passPacket(packet:Rule, BDD:BinaryDecisionDiagram):
    # checks to see if the packet would pass through the bdd 
    # packetString = ''
    # for tag in packet.flagTags:
    #     #print(tag)
    #     # f.restrict({a: 1, b: 0})
        
    #     if (len(packetString) < 1):
    #         packetString = str(packet.ruleFlags[tag]) + ': 1'
    #     else:
    #         packetString = packetString + ', ' + str(packet.ruleFlags[tag]) + ': 1'
    # packetString = '{' + packetString + '}'

    # try create a dictionary to pass it
    # packetDict = {}
    # for tag in packet.flagTags:
    #     packetDict[packet.ruleFlags[tag]] = 1
    
    # print(packetDict)
    
    #########################################
    # Note that it appears that the bdd vars arent declared and thus cant be used in a restriction 
    # This might be fixable with an update to the variables during creation

    ########################################
    #BDD.restrict({INPUT:1,tcp:1})
    # BDD.restrict(packetDict)

    return


# This function will take  in a rule and convert each field into a variabvle for the BDD in this way each node is a single field
# This will result in a BDD for the entire rule with each node representing a field in a rule 

# Going to have each field as an expression and then use the and operator to make them all link
# For now this is simple logic and more advanced logic should check if the fields exist and go from there
# Currently cannot simply add the fields and will likely need to add a variable to the BDD to represent them
# Going to create a set of expression variable to represent each field possible in a rule

# A_Flag_Bool = exprvar("A_Flag_Bool")
# S_Flag_Bool = exprvar("S_Flag_Bool")
# J_Flag_Bool = exprvar("J_Flag_Bool")
# P_Flag_Bool = exprvar("P_Flag_Bool")
# M_Flag_Bool = exprvar("M_Flag_Bool")
# State_Flag_Bool = exprvar("State_Flag_Bool")
# Dport_Flag_Bool = exprvar("Dport_Flag_Bool")

# Changing the generic names of the variables to match the rule field values 
# The following shows the expected flag values for the various fields
    # A_Flag shows direction like input or output
    # S_Flag shows Ip 
    # J_Flag shows status like Accept or Drop
    # P_Flag shows protocol like tcp
    # M_Flag shows state or multiport 
    # State_Flag shows if a connection has been established 
    # Dport_Flag shows which port is the destination port like 25 etc 
# Additionally if the field is empty then a "$" is the field value and if that field does not 'exist' then just make it true and the truth table will ommit it 
# So A_Flag_Bool will be something like 'INPUT'
# A_Flag_Bool = exprvar('A: ' + str(rule.A_Flag))
# S_Flag_Bool = exprvar('S: ' + str(rule.S_Flag))
# J_Flag_Bool = exprvar('J: ' + str(rule.J_Flag))
# P_Flag_Bool = exprvar('P: ' + str(rule.P_Flag))
# M_Flag_Bool = exprvar('M: ' + str(rule.M_Flag))
# State_Flag_Bool = exprvar('State: ' + str(rule.State_Flag))
# Dport_Flag_Bool = exprvar('Dport: ' + str(rule.Dport_Flag))



# If the BDD wre made from the rule class and not the dataFrame, the following part would not be necessary
        
# Going to try and make the '$' value true and ommit it from the truth table 
# Only issue is that the name is lost but the name was $ so nothing is lost 
# if(A_Flag_Bool.name == 'A: $'):
#     A_Flag_Bool = expr(1)
# if(S_Flag_Bool.name == 'S: $'):
#     S_Flag_Bool = expr(1)
# if(J_Flag_Bool.name == 'J: $'):
#     J_Flag_Bool = expr(1)
# if(P_Flag_Bool.name == 'P: $'):
#     P_Flag_Bool = expr(1)
# if(M_Flag_Bool.name == 'M: $'):
#     M_Flag_Bool = expr(1)
# if(State_Flag_Bool.name == 'State: $'):
#     State_Flag_Bool = expr(1)
# if(Dport_Flag_Bool.name == 'Dport: $'):
#     Dport_Flag_Bool = expr(1)
# can now implement some logic to check the passed rule fields exist etc and based on that create a more refined boolean rule
# Using the truth table will allow for simple evaluation of rules 
# then once a single rule has been converted into an expression correctly I believe they can be stored in either an farray (function array) or one can potentially 
# store the expression variables in an array using A = exprvars('a',4,4). Ideally the expression will be stored and then added together at the end to create the 
# entire ruleset as a BDD

#By using logic one can set the variables as well to limit the truth table size 
# This has been tested and seen to work with the below code
# A_Flag_Bool = expr(1)
# S_Flag_Bool = expr(1)
# J_Flag_Bool = expr(0)

# boolean_Rule = expr((A_Flag_Bool) & (S_Flag_Bool) & (J_Flag_Bool) & (P_Flag_Bool) & (M_Flag_Bool) & (State_Flag_Bool) & (Dport_Flag_Bool))
#print(boolean_Rule)
#print("This is the simplified boolean rule")

# simplified_Boolean_Rule = boolean_Rule.simplify()
#print(simplified_Boolean_Rule)
#print('This is the truth table for a rule \n')
#print(expr2truthtable(simplified_Boolean_Rule))

#test_Bool_Expression = expr(simplified_Boolean_Rule | simplified_Boolean_Rule)
#print('This is the test boolean expression')
# should be Or(And(A: INPUT, S: 169.213.14.0/16, J: ACCEPT), And(A: INPUT, S: 169.213.14.0/16, J: ACCEPT))
#print(test_Bool_Expression)

# IMPORTANT
# After printing out the expressions versus the simplified expressions
# It became apparent that there is no need to further complicate the expression creation as the simplify function removed the '1' variables which were the '$'
# An example would be this 
# Original: And(And(And(And(And(And(A: INPUT, S: 169.213.14.0/16), J: ACCEPT), 1), 1), 1), 1)
# Simplified: And(A: INPUT, S: 169.213.14.0/16, J: ACCEPT)
# return(simplified_Boolean_Rule)

# Create a function which will take in an entire rule set and then pass each rule to the generateFieldBoolExpressions() function 
# After the function returns an expression it will be stored in an array/list of type Expression
# then after some intialisation it will be summed together in the following way 
# tempExpr = expr(tempExpr | arr[i])
#  def generateBDDBoolExpression(ruleset:Ruleset):
    BDDExpressionArray = []
    for x in ruleset.Rules:
        fieldBoolExpr = generateFieldBoolExpressions(x)
        #print(fieldBoolExpr)
        # This print confirms that the BDD never sees the '$' variables or the '1' variables
        BDDExpressionArray.append(fieldBoolExpr)
    
    # Check to see if the array has atleast 2 elements in it
    if(len(BDDExpressionArray) < 2 ):
        # if the array has less than 2 elements it assings only 1 element
        tempExpr = BDDExpressionArray[0]
    else:
        # if the array has 2 or more elements then it creates an expression using the first 2 
        tempExpr = expr((BDDExpressionArray[0]) | (BDDExpressionArray[1]))
    
    # if the array has 2 elements or less then this for loop wont trigger
    for i in range(2,len(BDDExpressionArray)):
        tempExpr = expr(tempExpr | (BDDExpressionArray[i]))
    #print('\n')
    #print(expr2truthtable(tempExpr))

    # This simplify function should remove any redundancy and lower the depth of the expression  
    #print('Before Simplify')
    #print(tempExpr.depth)
    tempExpr = tempExpr.simplify()
    #print('After Simplify')
    #print(tempExpr.depth)
    return tempExpr

# def generateBDDfromExpr():
#     # Take in an expression and return a bdd
#     # It might be possible to reorder the bdd in a more optimized way using the following line of code
#     # However in order to use this method one would need to rename the variables which may prove difficult due to the dynamic nature of the bdd variables
#     #composedOutputBDD = outputBDD.compose()
#     #print(len(_NODES))
#     #for x in list(outputBDD.satisfy_all()):
#         #print(x)
#     outputBDD = expr2bdd(expr(exprRules))
#     from pyeda.boolalg.bdd import _NODES
#     print('The number of nodes required to implement the BDD is ' + str(len(_NODES)))
#     return outputBDD
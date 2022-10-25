import Ruleset
import DataFrame
import BDD

def main():
    print("Main Starts Here")
    fileName = input("Enter fileName with extension:")
    myRuleSet = Ruleset.RuleSet(fileName)
    #myRuleSet.importRules()
    myDF = DataFrame.generateDataFrame(fileName)
    #Take the DataFrame and pass it to a ruleset function which will allow for the rule generation
    # can index individual fields by using myDF.iloc[0,0] etc 
    myRuleSet.importFromDataFrame(myDF) 
    testRule = myRuleSet.Rules[0]

    print(testRule.getS_Flag())

    print(testRule.getIPBreakDownByPart(0))
    print(testRule.getIPBreakDownByPart(1))
    print(testRule.getIPBreakDownByPart(2))
    print(testRule.getIPBreakDownByPart(3))
    print(testRule.getIPBreakDownByPart(4))
    print(testRule.getIPBreakDownByPart(5))
    print(testRule.getIPNetworkID())
    print(testRule.getIPHostID())
    testRule2 = myRuleSet.Rules[1]
    print(testRule.S_Flag)


    output = BDD.generateBoolExpression(testRule,testRule2)
    print(output)
main()
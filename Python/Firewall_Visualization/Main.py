import Ruleset
import DataFrame
import BDDgenerator

def main():

    # Creating a function to serve as a switch statement 
    def welcomeSwitch(selectedOption):
        if int(selectedOption) > 5:
            print("The option selected does not exist. Please select an option from those listed.")
            welcomePrints()
            return
        elif int(selectedOption) == 1:
            print("The selected option is 1")
            fileName_1 = input("Enter file path with it`s extension for profile 1:")
            myRuleSet_1 = Ruleset.RuleSet(fileName_1)
            myRuleSet_1.importRules()
            myExpr_1 = BDDgenerator.generateBDDBoolExpression(myRuleSet_1.Rules,myRuleSet_1.ruleFields)
            myBDD_1 = BDDgenerator.generateBDDfromExpr(myExpr_1)
            welcomePrints()
            return 
        elif int(selectedOption) == 2:
            print("The selected option is 2")
            fileName_2 = input("Enter file path with it`s extension for profile 2:")
            myRuleSet_2 = Ruleset.RuleSet(fileName_2)
            myRuleSet_2.importRules()
            myExpr_2 = BDDgenerator.generateBDDBoolExpression(myRuleSet_2.Rules,myRuleSet_2.ruleFields)
            myBDD_2 = BDDgenerator.generateBDDfromExpr(myExpr_2)
            welcomePrints()
            return 
        elif int(selectedOption) == 3:
            print("The selected option is 3")
            welcomePrints()
            return 
        elif int(selectedOption) == 4:
            print("The selected option is 4")
            welcomePrints()
            return
        elif int(selectedOption) == 5:
            print("The selected option is 5")
            welcomePrints()
            return 
    
    def welcomePrints():
        print("\n Welcome, Please select an option from the following:\n")
        print("1. Load a ruleset file for ruleset 1\n")
        print("2. Load a ruleset file for ruleset 2\n")
        print("3. Check if a packet would pass ruleset 1\n")
        print("4. Check if a packet would pass ruleset 2\n")
        print("5. Check if ruleset 1 is functionally equivalent to ruleset 2\n")

        print("To correctly select an option please input the option number, for example to select option 1 type 1\n")
        print("A correct input would look like the following:")
        print("Example Please select an option number: 1\n")
        selectedOption = input("Please select an option number: ")
        welcomeSwitch(selectedOption)

    welcomePrints()
        
    

    
    # print(myRuleSet.Rules)
    #myRuleSet.importRules()
    # myDF = DataFrame.generateDataFrame(fileName)
    #Take the DataFrame and pass it to a ruleset function which will allow for the rule generation
    # can index individual fields by using myDF.iloc[0,0] etc 
    # myRuleSet.importFromDataFrame(myDF) 
    # testRule = myRuleSet.Rules[0]

    # print(testRule.getS_Flag())

    # print(testRule.getIPBreakDownByPart(0))
    # print(testRule.getIPBreakDownByPart(1))
    # print(testRule.getIPBreakDownByPart(2))
    # print(testRule.getIPBreakDownByPart(3))
    # print(testRule.getIPBreakDownByPart(4))
    # print(testRule.getIPBreakDownByPart(5))
    # print(testRule.getIPNetworkID())
    # print(testRule.getIPHostID())
    # testRule2 = myRuleSet.Rules[1]
    #print(testRule.S_Flag)

    # Compares a packet to a rule and gives a boolean output
    #output = BDD.generateBoolExpression(testRule,testRule2)
    #print(output)

    #output = BDD.generateFieldBoolExpressions(testRule)
    #print(output)

    # BDDExpression = BDD.generateBDDBoolExpression(myRuleSet)
    #print('\n')
    #print(BDDExpression)

    # myBDD = BDD.generateBDDfromExpr(BDDExpression)
main()
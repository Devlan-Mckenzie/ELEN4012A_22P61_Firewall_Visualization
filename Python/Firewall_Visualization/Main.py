import Ruleset
import DataFrame

def main():
    print("Main Starts Here")
    fileName = input("Enter fileName with extension:")
    myRuleSet = Ruleset.RuleSet(fileName)
    #myRuleSet.importRules()
    myDF = DataFrame.generateDataFrame(fileName)
    #Take the DataFrame and pass it to a ruleset function which will allow for the rule generation
    # can index individual fields by using myDF.iloc[0,0] etc 
    myRuleSet.importFromDataFrame(myDF) 

main()
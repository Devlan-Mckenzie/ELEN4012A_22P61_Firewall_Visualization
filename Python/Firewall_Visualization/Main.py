import Ruleset

def main():
    print("Main Starts Here")
    fileName = input("Enter fileName with extension:")
    myRuleSet = Ruleset.RuleSet(fileName)
    myRuleSet.importRules()
main()
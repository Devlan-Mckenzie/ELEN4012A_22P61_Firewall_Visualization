import Rule

class RuleSet:

    Rules = []

    def __init__(self,fileName):
        self.fileName = "Python\\Firewall_Visualization\\" + fileName
    
    def importRules(self):
        print("The file path is " + self.fileName)

        #Attempting to read in the textfile 
        try:
            file = open(self.fileName,'rt')
            for x in file:
                # Each x is a single line of the file
                # Use the split functionality to seperate the fields 
                # Assign the fields to a new rule and append it to the rules array
                tempArr = x.split()
                newRule = Rule.Rule(tempArr[0],tempArr[1])
                self.Rules.append(newRule)

            if len(self.Rules) > 0:
                print("The following is a list of the stored rules in the Ruleset:")
                for x in self.Rules:
                    print(x)

        except:
            print("File not found")
        
import Rule

#r1 = Rule.Rule("192.168.1.1","Accepted")

#print(r1)

class RuleSet:

    Rules = []

    def __init__(self,fileName):
        self.fileName = "Python\\Firewall_Visualization\\" + fileName
    
    def importRules(self):
        print("The importRules function was called successfully")
        print(self.fileName)
        newRule = Rule.Rule("192.168.1.1","Accepted")
        self.Rules.append(newRule)
        print(self.Rules[0])
        #Attempting to read in the textfile 
        file = open(self.fileName,'rt')
        print(file.read())
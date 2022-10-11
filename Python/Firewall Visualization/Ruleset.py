import Rule

#r1 = Rule.Rule("192.168.1.1","Accepted")

#print(r1)

class RuleSet:

    Rules = []

    def __init__(self,fileName):
        self.fileName = fileName
    
    def importRules(self):
        print("The importRules function was called successfully")
        print(self.fileName)
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
    
    def importFromDataFrame(self,dataframe):
        # passing a 2D dataframe which follows 
        #       -A      -s               -j        -p         -m            --state     --dport
        #   0   INPUT   169.213.14.0/16  ACCEPT    $          $            $            $
        try:
            # i is the total number of rules (up and down)
            #i = len(dataframe)
            # j is the number of fields in the table (left and right)
            #j = len(dataframe.iloc[1])

            for i in range(len(dataframe)):
                # i is the total number of rules (up and down)
                DF_Row = dataframe.iloc[i]
                # Currently assumes that the fields will never change 
                newRule = Rule.Rule(DF_Row[0],DF_Row[1],DF_Row[2],DF_Row[3],DF_Row[4],DF_Row[5],DF_Row[6])
                self.Rules.append(newRule)
            
            if len(self.Rules) > 0:
                print("The following is a list of the stored rules in the Ruleset:")
                for x in self.Rules:
                    print(x)
        except:
            print("An error occured while trying to read in the dataframe in RuleSet class")

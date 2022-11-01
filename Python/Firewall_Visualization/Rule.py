# This class will contain the information relevant to each Firewall rule 

class Rule:
    # def __init__(self,A_Flag,S_Flag,J_Flag,P_Flag,M_Flag,State_Flag,Dport_Flag):
    def __init__(self,newRule):
        # A_Flag shows direction like input or output
        # S_Flag shows Ip 
        # J_Flag shows status like Accept or Drop
        # P_Flag shows protocol like tcp
        # M_Flag shows state or multiport 
        # State_Flag shows if a connection has been established 
        # Dport_Flag shows which port is the destination port like 25 etc 

        # self.A_Flag = A_Flag
        # self.S_Flag = S_Flag
        # self.J_Flag = J_Flag
        # self.P_Flag = P_Flag
        # self.M_Flag = M_Flag
        # self.State_Flag = State_Flag
        # self.Dport_Flag = Dport_Flag 
        flagPair = {}
        i=0
        while i<len(newRule):
            a = newRule[i]
            b = newRule[i+1]
            flagPair[a]=b
            i+=2
        self.ruleFlags = flagPair
        
            


    # def __str__(self):
    #     return f"{self.A_Flag,self.S_Flag,self.J_Flag,self.P_Flag,self.M_Flag,self.State_Flag,self.Dport_Flag}"
    
    def __str__(self):
        return f"{self.ruleFlags}"

    def getFlag(self,flag):
        return self.ruleFlags[flag]
    # def getA_Flag(self):
    #     return self.A_Flag

    # def getS_Flag(self):
    #     return self.S_Flag

    # def getJ_Flag(self):
    #     return self.J_Flag

    # def getP_Flag(self):
    #     return self.P_Flag

    # def getM_Flag(self):
    #     return self.M_Flag

    # def getState_Flag(self):
    #     return self.State_Flag

    # def getDport_Flag(self):
    #     return self.Dport_Flag

    def getIPBreakDownByPart(self,part):
        # Takes in an interger as variable part and returns the spot as string
        # an example IP would be 169.213.14.0/16 and 
        # part 1 = 169
        # part 2 = 213 
        # part 3 = 14 
        # part 4 = 0/16
        try:

            if(part < 1 or part > 4):
                print("The part number ranges from 1 to 4 thus " + str(part) + " is not a valid part number")
                return
            
            # Break apart the string using '.' as a delimiter 
            parts = self.ruleFlags['-s'].split(".")
            if(part == 1):
                return parts[0]    
            if(part == 2):
                return parts[1] 
            if(part == 3):
                return parts[2] 
            if(part == 4):
                return parts[3] 
            
        except:
            print("An error occured when trying to break the IP string")
    
    def getIPNetworkID(self):
        # Returns the first 3 parts of a IP string 
        # an example IP would be 169.213.14.0/16 and 
        # returns 169.213.14 as the network id 
        return (self.getIPBreakDownByPart(1) + "." + self.getIPBreakDownByPart(2) + "." + self.getIPBreakDownByPart(3))
    
    def getIPHostID(self):
        # Returns the last part of an IP string
        # an example IP would be 169.213.14.0/16 and 
        # returns 0/16 as the Host id
        return (self.getIPBreakDownByPart(4))
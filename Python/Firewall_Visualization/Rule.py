# This class will contain the information relevant to each Firewall rule 

class Rule:
    def __init__(self,A_Flag,S_Flag,J_Flag,P_Flag,M_Flag,State_Flag,Dport_Flag):
        # A_Flag shows direction like input or output
        # S_Flag shows Ip 
        # J_Flag shows status like Accept or Drop
        # P_Flag shows protocol like tcp
        # M_Flag shows state or multiport 
        # State_Flag shows if a connection has been established 
        # Dport_Flag shows which port is the destination port like 25 etc 

        self.A_Flag = A_Flag
        self.S_Flag = S_Flag
        self.J_Flag = J_Flag
        self.P_Flag = P_Flag
        self.M_Flag = M_Flag
        self.State_Flag = State_Flag
        self.Dport_Flag = Dport_Flag 

    def __str__(self):
        return f"{self.A_Flag,self.S_Flag,self.J_Flag,self.P_Flag,self.M_Flag,self.State_Flag,self.Dport_Flag}"

    # def getA_Flag(self):
    #     return f"{self.A_Flag}"

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
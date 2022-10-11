# This class will contain the information relevant to each Firewall rule 

class Rule:
    def __init__(self,Ip,Status):
        self.Ip = Ip
        self.Status = Status

    def __str__(self):
        return f"{self.Ip}({self.Status})"
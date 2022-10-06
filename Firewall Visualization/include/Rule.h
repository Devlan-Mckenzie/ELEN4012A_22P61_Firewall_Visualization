#ifndef RULE_H
#define RULE_H

#include <iostream>
#include <string.h>

class Rule
{
    public:
        Rule();
        virtual ~Rule();
        void setIP(std::string sIP);
        void setStatus(std::string sStatus);
        std::string getIP();
        std::string getStatus();
    protected:

    private:
        std::string IP = "";
        std::string Status = "";
};

#endif // RULE_H

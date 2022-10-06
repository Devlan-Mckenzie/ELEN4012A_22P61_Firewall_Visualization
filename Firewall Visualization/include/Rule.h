#ifndef RULE_H
#define RULE_H

#include <iostream>
#include <string.h>
#include "Utils.h"

using std::string;
class Rule
{
    public:
        Rule();
        virtual ~Rule();
        void setIP(string ip){IP = ip;};
        void setStatus(string stat){Status = stat;};
        //void setDirection(string)

    protected:

    private:
        string DestinationPort;
        string IP;
        Direction _dir;
        Status _status;
        Protocol _protocol;

};

#endif // RULE_H

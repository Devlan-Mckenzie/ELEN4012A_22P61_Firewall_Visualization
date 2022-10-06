#ifndef RULE_H
#define RULE_H

#include <iostream>
#include <string.h>

class Rule
{
    public:
        Rule();
        virtual ~Rule();

    protected:

    private:
        std::string IP = "";
        std::string Status = "";
};

#endif // RULE_H

#ifndef RULESET_H
#define RULESET_H

#include "../include/Rule.h"
#include <iostream>
#include <iomanip>
#include <fstream>
#include <vector>
#include <bits/stdc++.h>
class RuleSet : public Rule
{
    public:
        RuleSet();
        virtual ~RuleSet();
        void ImportRules();

    protected:

    private:
        std::vector<Rule> rules;
};

#endif // RULESET_H

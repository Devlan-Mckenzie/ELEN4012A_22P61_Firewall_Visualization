#include "../include/RuleSet.h"

RuleSet::RuleSet()
{
    //ctor
}

RuleSet::~RuleSet()
{
    //dtor

}

void RuleSet::ImportRules()
{
    //Import rules from text file and assign each rules IP and Status in array of rules
    std::ifstream inFile;
    std::string tempLine;
    std::string tempWord;

    inFile.open("TempRuleSet.txt");
    if (!inFile) {
        std::cout << "Unable to open file" << std::endl;
        exit(1); // terminate with error
    }
    //inFile >> tempLine
    std::cout << "Started Importing the rules" << std::endl;
    std::cout << '\n' << std::endl;
    while(std::getline(inFile,tempLine))
    {
        std::istringstream ss(tempLine);
        // create a rule type variable
            Rule tempRule;
        while(ss >> tempWord)
        {
            // adding a conditional if statement to control rule property assingment
            if(tempRule.getIP() == "")
            {
                tempRule.setIP(tempWord);
            }
            else if(tempRule.getStatus() == "")
            {
                tempRule.setStatus(tempWord);
                rules.push_back(tempRule);
                tempRule.setIP("");
                tempRule.setStatus("");
            }
        }

    }
    Rule testRule;
    for(int i = 0;i<this->rules.size();i++)
    {
        testRule = this->rules[i];
        std::cout << "This is rule number "<< i << std::endl;
        std::cout << "The rule`s IP is " << testRule.getIP() << std::endl;
        std::cout << "The rule`s Status is " << testRule.getStatus() << std::endl;
        std::cout << '\n' << std::endl;
    }

    inFile.close();
    std::cout << "Finished Importing the rules" << std::endl;
    return;
}

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
    while(std::getline(inFile,tempLine))
    {
        std::cout << tempLine << std::endl;
        std::istringstream ss(tempLine);
        std::cout << '\n' << std::endl;
        while(ss >> tempWord )
        {
            std::cout << tempWord << std::endl;
        }
        std::cout << '\n' << std::endl;
    }

    inFile.close();
    std::cout << "Finished Importing the rules" << std::endl;
    return;
}

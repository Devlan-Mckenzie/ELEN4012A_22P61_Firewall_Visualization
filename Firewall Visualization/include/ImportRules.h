#ifndef IMPORTRULES_H
#define IMPORTRULES_H
#include <iostream>
#include <fstream>
#include <vector>
using std::fstream;
using std::vector;
using std::cout;
using std::cerr;
using std::endl;
using std::string;


class ImportRules
{
    public:
        ImportRules(string filename_){filename = filename_;};
        void setRules();


    protected:

    private:
        void organise();
        vector<string> words;
        vector<string> rule;
        fstream file;
        string filename;
        string word;
        vector<vector<string>> ruleSet;
};

#endif // IMPORTRULES_H

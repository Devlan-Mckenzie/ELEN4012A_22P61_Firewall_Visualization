#include "ImportRules.h"

//ImportRules::ImportRules(string filename_)
//{
//    //ctor
//}
void ImportRules::setRules()
{
    file.open(filename.c_str());
    while(file>>word)
    {
        words.push_back(word);
    }
}

void ImportRules::organise()
{
    vector<string> temp;
    for(string wrd : words)
    {
        if (wrd == "-A")
        {

        }
    }
}

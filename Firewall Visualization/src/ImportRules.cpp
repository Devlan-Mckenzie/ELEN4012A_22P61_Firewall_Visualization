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
    organise();
}


void ImportRules::organise()
{

    //for(string wrd : words)
    for(auto i=0; i<words.size();i++)
    {
        int n = i+1;


        if (words[i] == "-A")
        {
            temp.push_back(words[n]);
        }

        if (words[i] == "-p")
        {
            temp.push_back(words[n]);
        }

        if (words[i] == "--dport")
        {
            temp.push_back(words[n]);
            cout<<temp[1]<<endl;
        }

        if (words[i] == "--sport")
        {
            temp.push_back(words[n]);
        }
         if (words[i] == "-j")
        {
            temp.push_back(words[n]);
        }

        if (words[i] == "-s")
        {
            temp.push_back(words[n]);
        }

        if (words[i] == "-i")
        {
            temp.push_back(words[n]);
        }

        if (words[i] == "-o")
        {
            temp.push_back(words[n]);
        }

        if (words[i] == "--state")
        {
            temp.push_back(words[n]);
        }

        if (words[i] == "$ipt")
        {
            ruleSet.push_back(temp);
            temp.clear();
        }
    }
}

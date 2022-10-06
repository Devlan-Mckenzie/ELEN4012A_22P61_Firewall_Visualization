#include <iostream>
#include "include\RuleSet.h"
#include "include\ImportRules.h"
using namespace std;

int main()
{
    cout << "Hello world!" << endl;
    ImportRules ruleS("Sample Rules.txt");
//    cout << ruleS.getRules(); << endl;
    auto vec = ruleS.getRules();

    for (int i = 0; i < vec.size(); i++) {
        for (int j = 0; j < vec[i].size(); j++)
            cout << vec[i][j] << " ";
        cout << endl;
    }

    return 0;
}

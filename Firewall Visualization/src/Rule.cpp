#include "../include/Rule.h"

Rule::Rule()
{
    //ctor
}

Rule::~Rule()
{
    //dtor
}

void Rule::setIP(std::string sIP)
{
    this->IP = sIP;
}

void Rule::setStatus(std::string sStatus)
{
    this->Status = sStatus;
}

std::string Rule::getIP()
{
    return this->IP;
}

std::string Rule::getStatus()
{
    return this->Status;
}

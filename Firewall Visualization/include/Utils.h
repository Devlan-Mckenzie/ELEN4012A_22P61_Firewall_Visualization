#ifndef UTILS_H_INCLUDED
#define UTILS_H_INCLUDED


typedef enum
{
  INPUT, OUTPUT
} Direction;

typedef enum
{
    ACCEPT, DROP
}Status;

typedef enum
{
    TCP, UDP
}Protocol;

typedef enum
{
    INVALID,
    ESTABLISHED,
    RELATED,
    NEW
}State;
#endif // UTILS_H_INCLUDED

from pyeda.inter import *

f = expr("a & b | a & c | b & c")
print(f)
f = expr2bdd(f)
print(f)
a,b,c = map(bddvar,'abc')
type(a)
isinstance(a,BinaryDecisionDiagram)
a0 = bddvar('a',0)
print(a0)
b_a_0_1 = bddvar(('a','b'), (0,1))
#b.a[0,1] not working 
X = bddvars('x',4,4)
print(X)
f = a & b | a & c | b & c
print(f)
f.restrict({a: 0})
print(f)
f.restrict({a:1, b:0})
print(f)
f.restrict({a:1,b:1})
print(f)
print(list(f.satisfy_all()))
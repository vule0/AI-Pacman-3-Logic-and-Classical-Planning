from logicPlan import *

print(findModel(sentence1()))
print(findModel(sentence2()))
print(findModel(sentence3()))
A = Expr('A')
B = Expr('B')
C = Expr('C')
expr1 = A & B >> C
print(to_cnf(expr1))
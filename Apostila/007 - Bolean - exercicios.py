# 1. Quais são os dois valores do tipo de dado booleano? Como eles são escritos?
#True e False

# 2. Quais são os três operadores booleanos?
# and, or e not

# 3. Quais são os seis operadores de comparação?
# == igual != diferente
# > maior que >= maior ou igual 
#< menor que , <= menor ou igual

# 4. Considerando que x = 5, y = 5, z = 1 e w = 2:
# a. Qual o resultado da expressão not (x > y or z < w)?
# 5>5 falso , 1<2 verdeiro, falso ou verdadeiro = verdadeiro. verdadeiro negado é falso
# b. Qual o resultado da expressão not x > y or z < w?
#5>5 falso , falso negado é verdadeiro.  1<2 verdeiro, verdadeiro ou verdadeiro é verdadeiro
# c. Os resultados foram iguais ou diferentes? Por que?
# foram diferentes pois no a. o not inverte a expressão inteira. no b o not inverte apenas o x>y
x = 5
y = 5
z = 1 
w = 2
print("a. Qual o resultado da expressão not (x > y or z < w)? ", not (x > y or z < w))
print("b. Qual o resultado da expressão not x > y or z < w? ", not x > y or z < w)

# En el laboratorio anterior resolvimos un problema que consistia en crear una lista de numeros pares del 1 al 100 a partir de otra. 
# Te propongo crear una función que indique si un número es par o no, y la utilices en la solución anterior. 
# Puedes hacer lo mismo pero con números impares definiendo una función lambda
# con funcion
# def es_par(num):
#     if num%2==0: return True
#     else: return False
# labmda par
#is_even = lambda num: num%2==0
is_odd = lambda num: num%2!=0
for j in [i for i in range(1,101) if !is_odd(i)]: print(j)
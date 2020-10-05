# Supongamos que tenemos una lista de numeros del 1 al 100. 
# Te propongo obtener la lista sólo de aquellos números pares. 
# Haz una versión con comprensión de listas y otra sin ella.
# lista = [1, 2, 3, 4, 5, 6, 7, 8, 9,...]
# resultado = [2, 4, 6, 8, ...]

# [i*i for i in range(10) if i%2 == 0]:

for j in [i for i in range(1,101) if i%2 == 0]: print(j)




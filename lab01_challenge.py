# Tenemos que crear un diccionario fibonnaci. Por clave tendrá la posición, y por valor la lista de números fibonnaci hasta esa posición. 
# Se pide además dar una salida formateada del diccionario
# entrada = 5
# # fibonnaci es un diccionario
# fibonnaci[5] # la salida sería [1,2,3,5,8]
# comentario de prueba para merge

fibonnaci_list = [1,2,3,5,8]
fibonnaci_dict = dict()
for i in range(0,len(fibonnaci_list)): fibonnaci_dict.update(dict({i+1:fibonnaci_list[0:i+1]}))
for i in range(1,len(fibonnaci_dict)+1): print("fibonnaci[{}] es {}".format(i,fibonnaci_dict[i]))


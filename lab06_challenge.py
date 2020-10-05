# Para comenzar con la instalación de paquetes, vamos a utilizar pandas. 
# Esta es una librería muy conocida para análisis de datos. 
# Como fuente de datos usaremos un fichero con todos los Pokemon e imprimiremos los 5 primeros:

#    #                   Name Type 1  ... Speed  Generation  Legendary
# 0  1              Bulbasaur  Grass  ...    45           1      False
# 1  2                Ivysaur  Grass  ...    60           1      False
# 2  3               Venusaur  Grass  ...    80           1      False
# 3  3  VenusaurMega Venusaur  Grass  ...    80           1      False
# 4  4             Charmander   Fire  ...    65           1      False

# [5 rows x 13 columns]
# Como ayuda mirar las funciones read_csv y head

import pandas

datos = pandas.read_csv("./Pokemon.csv")
print(datos.head(5))
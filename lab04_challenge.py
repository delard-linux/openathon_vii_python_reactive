# Crear una clase Hero con cuatro atributos: nombre, sexo, saludo y nivel (del 1 al 100). 
# Crea varios personajes y crea un método lucha que recibirá dos parámetros, de tipo Hero y en base al nivel de poder mostrará un saludo o otro. 
# Por cierto comprueba que los parámetros no sean nulos.

class Hero:
    nombre = None
    sexo = None
    saludo = None
    nivel = None
  
    # Constructor de la clase Persona
    def __init__(self, nombre, sexo, saludo, nivel):
        list_err = list()
        str_nulo =  "{} no puede ser nulo"
        str_nivel =  "nivel tiene que ser entero de 1 a 100 [{}]"
        if nombre == None: list_err.append(str_nulo.format("nombre"))
        else: self.nombre = nombre 
        if sexo == None: list_err.append(str_nulo.format("sexo"))
        else: self.sexo = sexo
        if saludo == None: list_err.append(str_nulo.format("saludo"))
        else: self.saludo = saludo 
        if nivel == None: list_err.append(str_nulo.format("nivel"))
        elif type(nivel)!=type(1) or nivel<1 or nivel > 100 : list_err.append(str_nivel.format(nivel))
        else: self.nivel = nivel         
        if len(list_err)>0:
            print("Error de creación de objeto Hero:")
            for st in list_err: print("  - {}".format(st))     

    def lucha_con(self, otro_hero):
        if type(otro_hero) != type(self): print("No soy un Hero [{}]".format(type(otro_hero)))
        elif self.nivel >= otro_hero.nivel: 
            print("Soy {}, {}, te crujo cabronazo {}, ya que tu nivel es {} y el mio {}".format(self.nombre, self.saludo, otro_hero.nombre, otro_hero.nivel, self.nivel)) 

heroe1 = Hero("PutoAmo", "female", "holaquease", 100)
heroe2 = Hero(None, None, None, 1111111111111111111111111)
heroe3 = Hero("Conan", "male", "argggg", 23)
heroe4 = Hero("Goku", "male", "hayuuuuke", 56)

heroe1.lucha_con(heroe3)
heroe1.lucha_con(heroe4)

    

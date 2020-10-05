# Define un método que reciba una palabra y devuelva el numero de vocales diferentes que contiene.
# Debes comprobar que sea un string. En caso de que no sea un string lanzaras una excepción de tipo ValueError.
# En caso de que no tenga vocales lanzaras una excepción propia NoVocalsError. Si tiene al menos una vocal, retornaras el número.
# El programa llamante tendra que capturas las dos excepciones e imprimir mensajes diferentes.

class NoVowelsError(Exception):
    pass

def num_vowels(cadena):
    ret_num_vowels = 0
    list_vowels = ['a', 'e', 'i', 'o', 'u']
    if type(cadena) != type(" "):
        msg = "Not a string [{}] is {}".format(cadena,type(cadena))
        raise ValueError(msg)
    else : 
        for c in cadena.lower() : 
            if list_vowels.count(c) > 0 : 
                ret_num_vowels = ret_num_vowels+1
    if ret_num_vowels > 0 : return ret_num_vowels
    else : 
        msg = "No vowels in  [{}]".format(cadena)
        raise NoVowelsError(msg)
    return 

## Test
list_test = [
            "werwerwerwe",
            "ee",
            "AeIoU",
            45,
            56.56,
            True,
            "rqwtwgqtqwgwqtw",
            "aaa"]

for i in list_test: 
    try:
        print("OK  : La cadena '{}' tiene {} vocales".format(i,num_vowels(i)))
    except (ValueError, NoVowelsError) as strerror:
        print("ERR : {}".format(strerror))


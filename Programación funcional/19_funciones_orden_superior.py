# El concepto de funciones de orden superior se refiere al uso de funciones
# como si de un valor cualquiera se tratara, posibilitando pasar funciones 
# como parámetros de otras funciones o devolver funciones como valor de retorno

def saludar(lang):
    def saludar_es():
        return "Hola"
    
    def saludar_en():
        return "Hi"
    
    def saludar_fr():
        return "Salut"
    
    lang_func = {"es":saludar_es,"en": saludar_en, "fr":saludar_fr}
    
    return lang_func[lang]

f = saludar("en")

print(f())
class Entrenador :
    def hablar(self):
        print("¡Soy el entrenador!")

class Futbolista:
    def hablar(self):
        print("¡Soy un futbolista!")

class Masajista:
    def hablar(self):
        print("¡Soy un masajista!")

def llama_hablar(x):
    x.hablar()
llama_hablar(Entrenador())
llama_hablar(Futbolista())
llama_hablar(Masajista())


#USO DE DISPATCH
from multipledispatch import dispatch
@dispatch(int, int) #Add que funciona como suma de enteros
def add(a, b):
    return print(a + b)
@dispatch(str, str)
def add(a, b):  #Add que funciona como concatenacion de cadenas
    return print(" ".join((a, b)))



add("Hola","mundo")
add(5,6)

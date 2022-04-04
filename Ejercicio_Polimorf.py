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
from abc import ABC, abstractmethod

class Animal(ABC):

    def __init__(self, nome: str):
        self.nome:str = nome
    
    def apresentar_nome(self):
        print(f"Eu sou um(a) {self.nome}")
    
    @abstractmethod
    def fazer_som(self):
        pass

    @abstractmethod
    def mover(self):
        pass

class Leão(Animal):

    def __init__(self,nome:str):
        super().__init__(nome)
    
    def fazer_som(self):
        print("ROOOOOAAAR")

    def mover(self):
        print("tump tump tump")

    def apresentar_nome(self):
        return super().apresentar_nome()
    
class Urso(Animal):

    def __init__(self, nome:str):
        super().__init__(nome)

    def fazer_som(self):
        print("grrr")

    def mover(self):
        print("crac crac")

    def apresentar_nome(self):
        return super().apresentar_nome()

class Jacaré(Animal):

    def __init__(self, nome):
        super().__init__(nome)

    def fazer_som(self):
        print("rrrrr")

    def mover(self):
        print("chop chop")

    def apresentar_nome(self):
        return super().apresentar_nome()

def apresentar(animais:list):
    for animal in animais:
        print(f"{animal.__class__.__name__}")
        animal.apresentar_nome()
        animal.fazer_som()
        animal.mover()

animais = [
    Leão("Mufasa"),
    Urso("Zé Colmeia"),
    Jacaré("Louis")
]

apresentar(animais)
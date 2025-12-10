from abc import ABC, abstractmethod

class Veículo(ABC):

    def __init__(self, tipo:str, id:str):
        self.__id = id
        self._tipo = tipo
        self._horaE = 0

    def setEntrada(self, horaE: int):
        self._horaE = horaE

    def getEntrada(self):
        return self._horaE
    
    def getTipo(self):
        return self._tipo
    def getId(self):
        return self.__id
    
    @abstractmethod
    def calcularV(self, horaS:int):
        pass
    
    def __str__(self):
        tipo_fmt = self._tipo.rjust(10,"_")
        id_fmt = self.__id.rjust(10,"_")
        return f"{tipo_fmt} : {id_fmt} : {self._horaE}"
    
    
class Carro(Veículo):

    def __init__(self, id:str):
        super().__init__("Carro",id )
    
    def calcularV(self, horaS):
        diferença = horaS - self._horaE
        v = diferença / 10
        valor = f"R$ {v:.2f}"
        if v < 5:
            valor = "R$ 5.00"
        return valor
        
    
class Moto(Veículo):

    def __init__(self, id:str):
        super().__init__("Moto",id )

    def calcularV(self, horaS):
        diferença = horaS - self._horaE
        v = diferença / 20
        valor = f"R$ {v:.2f}"
        return valor
    
class Bike(Veículo):

    def __init__(self, id):
        super().__init__("Bike",id)
    
    def calcularV(self, horaS):
        valor = "R$ 3.00"   
        return valor    

class Estacionamento:

    def __init__(self):
        self.__veículos: list[Veículo] = []
        self.horaA:int = 0

    def estacionar(self, tipo:str, id:str):
        if tipo == "bike":
            v = Bike(id)
        elif tipo == "carro":
            v = Carro(id)
        elif tipo == "moto":
            v = Moto(id)
        
        v.setEntrada(self.horaA)
        self.__veículos.append(v)

    def passarTempo(self, tempo:int):
        self.horaA += tempo

    def __str__(self):
        if self.__veículos != []:
           txt = ""
           for v in self.__veículos:
               txt += str(v) + "\n"
           txt += f"Hora atual: {self.horaA}"
           return txt
        else:
            return f"Hora atual: {self.horaA}"
    
    def pagar(self, id:str):
        for v in self.__veículos:
            if id == v.getId():
                valor = v.calcularV(self.horaA)
                print(f"{v.getTipo()} chegou {v.getEntrada()} saiu {self.horaA}. Pagar {valor}")
           
        
    def show(self):
        print(self)
    
def main():
    estacionamento = Estacionamento()

    while True:
        linha = input()
        arg:list[str] = linha.split(" ")
        print("$"+linha)

        if arg[0] == "end":
            break
        elif arg[0] == "show":
            estacionamento.show()
        elif arg[0] == "estacionar":
            tipo:str = arg[1]
            id:str = arg[2]
            estacionamento.estacionar(tipo, id)
        elif arg[0] == "tempo":
            tempo:int = int(arg[1])
            estacionamento.passarTempo(tempo)
        elif arg[0] == "pagar":
            id:str = arg[1]
            estacionamento.pagar(id)
main()
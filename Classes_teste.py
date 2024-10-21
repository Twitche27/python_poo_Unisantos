from abc import ABC

class Atleta(ABC):
    nome : str
    idade : int
    peso: float

    def __init__(self, nome, idade, peso) -> None:
        self.nome = nome
        self.idade = idade
        self.peso = peso

    def aquecer(self) -> str:
        return "Aquecendo..."
    
    def __str__(self) -> str:
        return f'Nome: {self.nome}\nIdade: {self.idade}\nPeso: {self.peso}kg'
    
class Corredor(Atleta):
    def correr(self) -> str:
        return "Correndo..."
    
class Nadador(Atleta):
    def nadar(self) -> str:
        return "Nadando..."
    
class Ciclista(Atleta):
 def pedalar(self) -> str:
     return "Pedalando..."
 
class Triatleta(Corredor, Nadador, Ciclista):
    def realizar_maratona(self) -> str:
        info = self.nadar()
        info += self.pedalar()
        info += self.correr()
        return info
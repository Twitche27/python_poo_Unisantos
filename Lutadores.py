from abc import ABC

class Lutador(ABC):
    nome : str
    energia : float

    def __init__(self, nome) -> None:
        self.nome = nome
        self.energia = 100

    def soco(self, oponente):
        print("Soco!")
        oponente.energia -= 5.5

    def __str__(self) -> str:
        return f'Nome: {self.nome}\nEnergia: {self.energia}%'
    
class Boxeador(Lutador):
    def cruzado(self, oponente:Lutador):
        print("Cruzado!")
        oponente.energia -= 10.2

    def gancho(self, oponente:Lutador):
        print("Gancho!")
        oponente.energia -= 20.8

class Muay_Thai(Boxeador):
    def chute_alto(self, oponente:Lutador):
        print("Chute Alto!")
        oponente.energia -= 15.4

class Jiujitsu(Lutador):
    def chave_braco(self, oponente:Lutador):
        print("Chave de Braço!")
        oponente.energia -= 100

class MMA(Muay_Thai, Jiujitsu):
    def superman_punch(self, oponente:Lutador):
        print("Superman Punch!")
        oponente.energia -= 53.2
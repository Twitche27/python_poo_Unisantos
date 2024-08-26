class Carro:
    modelo : str
    marca : str
    cor : str
    __odometro : 0.0
    __motor_on : False
    __tanque: float
    consumo_medio: float

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, tanque : float,
                       consumo_medio : float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.__odometro = odometro
        self.__motor_on = motor
        self.__tanque = tanque
        self.consumo_medio = consumo_medio

    def get_odometro(self):
        return self.__odometro

    def get_tanque(self):
        return self.__tanque

    def ligar(self):
        if self.__tanque > 0:
            if not self.__motor_on:
                self.__motor_on = True
            else:
                raise Exception("Erro: Motor já ligado!")
        else:
            raise Exception("Erro: Tanque Vazio")

    def acelerar(self, velocidade : float, tempo : float):
        if self.__motor_on:
            kilometragem = velocidade * tempo
            litros = kilometragem*self.consumo_medio
            if litros <= self.__tanque:
                self.__tanque -= litros
                self.__odometro += kilometragem
            else:
                self.__odometro += kilometragem*(self.__tanque/litros)
                self.__tanque = 0
                self.__motor_on = False
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.__motor_on:
            self.__motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.__odometro} Km, '
                f'motor {self.__motor_on}, tanque {self.__tanque}\n'
                f'km/L {self.consumo_medio}')
        return info






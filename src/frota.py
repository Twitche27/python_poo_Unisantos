class Carro:
    modelo : str
    marca : str
    cor : str
    odometro : 0.0
    motor_on : False
    tanque: float
    consumo_medio: float

    def __init__(self, modelo : str, marca : str, cor : str,
                       odometro : float, motor : bool, tanque : float,
                       consumo_medio : float):
        self.modelo = modelo
        self.marca = marca
        self.cor = cor
        self.odometro = odometro
        self.motor_on = motor
        self.tanque = tanque
        self.consumo_medio = consumo_medio

    def ligar(self):
        if self.tanque > 0:
            if not self.motor_on:
                self.motor_on = True
            else:
                raise Exception("Erro: Motor já ligado!")
        else:
            raise Exception("Erro: Tanque Vazio")

    def acelerar(self, velocidade : float, tempo : float):
        if self.motor_on:
            kilometragem = velocidade * tempo
            litros = kilometragem*self.consumo_medio
            if litros <= self.tanque:
                self.tanque -= litros
                self.odometro += kilometragem
            else:
                self.odometro += kilometragem*(self.tanque/litros)
                self.tanque = 0
                self.motor_on = False
        else:
            raise Exception("Erro: Não é possível acelerar! Motor desligado!")

    def desligar(self):
        if self.motor_on:
            self.motor_on = False
        else:
            raise Exception("Erro: Motor já desligado!")

    def __str__(self):
        info = (f'Carro {self.modelo}, marca {self.marca}, '
                f'cor {self.cor}\n{self.odometro} Km, '
                f'motor {self.motor_on}, tanque {self.tanque}\n'
                f'km/L {self.consumo_medio}')
        return info






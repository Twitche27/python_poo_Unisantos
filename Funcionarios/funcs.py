from abc import ABC, abstractmethod

class Funcionario(ABC):
    __nome : str
    __cpf : str
    __salario : float
    __senha : int

    def __init__(self, nome : str, cpf : str, salario : float, senha : int) -> None:
        super().__init__()
        self.__nome = nome
        self.__cpf = cpf
        self.__salario = salario
        self.__senha = senha

    @abstractmethod
    def autenticar(self, usuario : str, senha : int) -> bool:
        if usuario == self.__cpf and senha == self.__senha:
            return True
        return False
    
class Gerente(Funcionario):
    __nFunc : int

    def __init__(self, nome: str, cpf: str, salario: float, senha: int, nFunc : int) -> None:
        super().__init__(nome, cpf, salario, senha)
        self.__nFunc = nFunc

    def cancelarOperacao(self) -> None:
        print("Operação cancelada com sucesso!")

class OperadorCaixa(Funcionario):
    __numeroCaixa : int

    def __init__(self, nome: str, cpf: str, salario: float, senha: int, numeroCaixa : int) -> None:
        super().__init__(nome, cpf, salario, senha)
        self.__numeroCaixa = numeroCaixa

    def registrar(self) -> None:
        print("Registro efetuado com sucesso!")

    @abstractmethod
    def autenticar(self, numeroCaixa: str, senha: int) -> bool:
        if numeroCaixa == self.__numeroCaixa and senha == self.__senha:
            return True
        return False

class Seguranca(Funcionario):
    __posto : str

    def __init__(self, nome: str, cpf: str, salario: float, senha: int, posto : str) -> None:
        super().__init__(nome, cpf, salario, senha)
        self.__posto = posto

    def acionarAlarme(self) -> None:
        print("UOOOOOOOOOUUUUUOOOOOOOOOOOOUUUUUUOOOOOOOO")
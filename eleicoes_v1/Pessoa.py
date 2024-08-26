class Pessoa():
    __nome : str
    __RG: str
    __CPF: str

    def __init__(self, nome: str, RG: str, CPF: str):
        self.__nome = nome
        self.__RG = RG
        self.__CPF = CPF

    def __str__(self):
        return f'Nome: {self.__nome}, RG: {self.__RG}, CPF: {self.__CPF}'

    def __repr__(self):
        return f"Pessoa(nome='{self.__nome}', RG='{self.__RG}', CPF='{self.__CPF}'"

class Eleitor(Pessoa):
    __titulo: str
    secao: int
    zona: int

    def __init__(self, nome: str, RG: str, CPF: str, titulo: str, secao: int, zona: int) -> None:
        super().__init__(nome, RG, CPF)
        self.__titulo = titulo
        self.secao = secao
        self.zona = zona

    def __str__(self):
        return (super().__str__() +
                f', Titulo: {self.__titulo}, Secão: {self.secao}, Zo: {self.zona}')

    def __repr__(self):
        return f"Eleitor({super().__repr__()}, titulo='{self.__titulo}', secao='{self.secao}', zona='{self.zona}'"

    def get_titulo(self):
        return self.__titulo

class Candidato(Pessoa):
    __numero: int

    def __init__(self, nome: str, RG: str, CPF: str, numero: int) -> None:
        super().__init__(nome, RG, CPF)
        self.__numero = numero

    def __str__(self):
        return (super().__str__() + f", Numero: {self.__numero}")

    def __repr__(self):
        return f"Candidato({super().__repr__()}, numero='{self.__numero}')"

    def get_numero(self):
        return self.__numero

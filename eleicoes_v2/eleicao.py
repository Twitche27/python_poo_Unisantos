import pickle
from typing import List
from Common import *
from datetime import date

class Urna:
    mesario : Pessoa
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor]
    __votos = {} #dicionario chave = numero do candidato, valor é a quantidade de votos

    def __init__(self, mesario : Pessoa, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}'
        self.__candidatos = candidatos
        self.__eleitores = []
        self.__eleitores_presentes = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(f'{self.__nome_arquivo}.pkl', 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

        with open(f'{self.__nome_arquivo}_zeresima.pkl', 'wb') as arquivo:
            pickle.dump(self.get_zerissima(), arquivo)

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor : Eleitor, n_cand : int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        elif n_cand == 0:
            self.__votos['BRANCO'] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_zerissima(self):
        info : str = ""
        for candidato, votos in self.__votos.items():
            info += f'{candidato} = {votos}\n'
        return info

    def __del__(self):
        with open(f'{self.__nome_arquivo}_zerF.pkl', 'wb') as arquivo:
            pickle.dump(self.get_zerissima(), arquivo)

    def __str__(self):
        data_atual = date.today()
        info = f'{data_atual.ctime()}'
        info += (f'Urna da seção {self.__secao}, zona {self.__zona}\n'
                f'Mesario {self.mesario}\n')
        for candidato, votos in self.__votos.items():
            info += f'{candidato} = {votos}\n'
        return info
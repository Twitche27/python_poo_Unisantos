import pickle
from typing import List
from common import *
from Interface_Eleicao import Transparencia
import csv

class Urna(Transparencia):
    mesario : Pessoa
    __secao : int
    __zona : int
    __eleitores_presentes : List[Eleitor]
    __votos = {} #dicionario chave = numero do candidato, valor é a quantidade de votos
    __counter = 0

    def __init__(self, mesario : Pessoa, secao : int, zona : int,
                 candidatos : List[Candidato], eleitores : List[Eleitor]):
        self.__eleitores_presentes = []
        self.mesario = mesario
        self.__secao = secao
        self.__zona = zona
        self.__nome_arquivo = f'{self.__zona}_{self.__secao}.pkl'
        self.__candidatos = candidatos
        self.__eleitores = []
        for eleitor in eleitores:
            if eleitor.zona == zona and eleitor.secao == secao:
                self.__eleitores.append(eleitor)
        self.__class__.__counter += 1
        self.__counterinst = self.__counter

        for candidato in self.__candidatos:
            self.__votos[candidato.get_numero()] = 0
        self.__votos['BRANCO'] = 0
        self.__votos['NULO'] = 0

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def get_eleitor(self, titulo : int):
        for eleitor in self.__eleitores:
            if eleitor.get_titulo() == titulo:
                return eleitor
        return False

    def registrar_voto(self, eleitor : Eleitor, n_cand : int):
        self.__eleitores_presentes.append(eleitor)
        if n_cand in self.__votos:
            self.__votos[n_cand] += 1
        else:
            self.__votos['NULO'] += 1

        with open(self.__nome_arquivo, 'wb') as arquivo:
            pickle.dump(self.__votos, arquivo)

    def __str__(self):
        info =  f'Urna da seção {self.__secao}, zona {self.__zona}\n'
        info += f'Mesario {self.mesario}\n'
        return info

    def to_csv(self):
        with open(f'Urna_{self.__counterinst}.csv', mode='w', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Seção', 'Zona', 'Título do Eleitor Presente'])

            for eleitor in self.__eleitores_presentes:
                writer.writerow([self.__secao, self.__zona, eleitor.get_titulo()])
    
    def to_txt(self):
        with open(f'Urna_{self.__counterinst}.txt', 'w') as file:
            file.write('Seção' + ' Zona' + ' Título do Eleitor Presente\n')
            for eleitor in self.__eleitores_presentes:
                file.write(str(self.__secao) + " " + str(self.__zona) + " " + str(eleitor.get_titulo()) + "\n")

if __name__ == "__main__":
    mes = Eleitor("AAA", "111", "333", 123, 3, 1)
    can1 = Candidato("sgdafdahd", "36363", "235235", 23)
    el1 = Eleitor("aaa", "132", "213", 123213, 3, 1)
    u1 = Urna(mes, 3, 1, [can1], [el1])
    u1.registrar_voto(el1, 23)
    can2 = Candidato("sgdafdahd", "36363", "235235", 23)
    el2 = Eleitor("aaa", "132", "213", 123213, 4, 2)
    u2 = Urna(mes, 4, 2, [can2], [el2])
    u2.registrar_voto(el2, 23)
    u2.to_csv()
    u2.to_txt()
    u1.to_csv()
    u1.to_txt()


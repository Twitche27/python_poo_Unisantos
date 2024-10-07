import pickle
import traceback
from gerenciar_urna import *
from Common import *


FILE_ELEITORES = 'eleitores.pkl'
FILE_CANDIDATOS = 'candidatos.pkl'

def escolha_menu():
    print("1-Menu Candidato")
    print("2-Menu Eleitor")
    print("3-Menu Urna")
    print("4-Sair")
    op = int(input("Digite a opcao [1,2,3,4]? "))
    while op not in (1, 2, 3, 4):
        op = int(input("Digite a opcao [1,2,3,4]? "))
    return op

def menu_candidato():
    print("1-Novo Candidato")
    print("2-Listar Candidatos")
    print("3-Sair")
    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def menu_eleitor():
    print("1-Novo Eleitor")
    print("2-Atualizar Eleitor")
    print("3-Sair")
    op = int(input("Digite a opcao [1,2,3]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3]? "))
    return op

def menu_urna():
    print("1-Iniciar Urna")
    print("2-Votar")
    print("3-Desligar Urna")
    print("4-Sair")
    op = int(input("Digite a opcao [1,2,3,4]? "))
    while op not in (1, 2, 3):
        op = int(input("Digite a opcao [1,2,3,4]? "))
    return op

def inserir_candidato(candidatos: dict[int, Candidato]):
    numero = int(input("Digite o Numero: "))

    if numero in candidatos:
        raise Exception("Numero já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")

    candidato = Candidato(nome, RG, CPF, numero)
    candidatos[candidato.get_numero()] = candidato

    with open(FILE_CANDIDATOS, 'wb') as arquivo:
        pickle.dump(candidatos, arquivo)

    print("Candidato gravado com sucesso!")
    print(candidato)

def inserir_eleitor(eleitores: dict[int, Eleitor]):
    titulo = int(input("Digite o Título: "))

    if titulo in eleitores:
        raise Exception("Titulo já existente!")

    nome = input("Digite o nome: ")
    RG = input("Digite o RG: ")
    CPF = input("Digite o CPF: ")
    secao = int(input("Digite a secao: "))
    zona = int(input("Digite a zona: "))

    eleitor = Eleitor(nome, RG, CPF, titulo, secao, zona)
    eleitores[eleitor.get_titulo()] = eleitor

    with open(FILE_ELEITORES, 'wb') as arquivo:
        pickle.dump(eleitores, arquivo)

    print('Eleitor gravado com sucesso!')
    print(eleitor)

def listar_candidatos(candidatos: dict[int, Candidato]):
    for candidato in candidatos.values():
        print(candidato)

def atualizar_eleitor(eleitores: dict[int, Eleitor]):
    titulo = int(input('Digite o titulo do eleitor: '))

    if titulo in eleitores:
        eleitor = eleitores[titulo]
        print(eleitor)
        secao = int(input("Digite a nova secao: "))
        zona = int(input("Digite a nova zona: "))
        eleitor.secao = secao
        eleitor.zona = zona

        with open(FILE_ELEITORES, 'wb') as arquivo:
            pickle.dump(eleitores, arquivo)

        print('Atualizados dados do eleitor!')
        print(eleitor)
    else:
        raise Exception('Titulo inexistente')


if __name__ == "__main__":
    candidatos = {}
    eleitores = {} #dicionário a chave será o titulo

    try:
        print("Carregando arquivo de candidatos ...")

        with open(FILE_CANDIDATOS, 'rb') as arquivo:
            candidatos = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum candidato carregado!")

    try:
        print("Carregando arquivo de eleitores ...")

        with open(FILE_ELEITORES, 'rb') as arquivo:
            eleitores = pickle.load(arquivo)
    except FileNotFoundError as fnfe:
        print(fnfe)
        print("Arquivo nao encontrado, nenhum eleitor carregado!")

    opcao = 1
    while opcao in (1,2,3):
        try:
            opcao = escolha_menu()
            if opcao == 1:
                opcao = menu_candidato()
                if opcao == 1:
                    inserir_candidato(candidatos)
                elif opcao == 2:
                    listar_candidatos(candidatos)
                else:
                    print("Saindo...")
            elif opcao == 2:
                opcao = menu_eleitor()
                if opcao == 1:
                    inserir_eleitor(eleitores)
                elif opcao == 2:
                    atualizar_eleitor(eleitores)
                else:
                    print("Saindo...")
            elif opcao == 3:
                opcao = menu_urna()
                if opcao == 1:
                    urna = iniciar_urna(eleitores.values(), candidatos.values())
                elif opcao == 2:
                    try:
                        votar(urna)
                    except NameError as erro:
                        print(erro)
                        print("Urna não foi iniciada!")
                elif opcao == 3:
                    del urna
                else:
                    print("Saindo...")
            elif opcao == 4:
                print("Saindo!")
                break
        except Exception as e:
            traceback.print_exc()
            print(e)
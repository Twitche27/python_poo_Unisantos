import random
from Lutadores import *

if __name__ == "__main__":
    jj = Jiujitsu("Lutador 1")
    jj_ataques = ["soco", "chave_braco"]
    mma = MMA("Lutador 2")
    mma_ataques = ["soco", "cruzado", "gancho", "chute_alto", "chave_braco", "superman_punch"]
    while (jj.energia > 0 and mma.energia > 0):
        eval(f'jj.{random.choice(jj_ataques)}(mma)')
        print(mma)
        if mma.energia <= 0:
            break
        eval(f'mma.{random.choice(mma_ataques)}(jj)')
        print(jj)
    if jj.energia <= 0:
        print(jj.nome + " Perdeu")
    else:
        print(mma.nome + " Perdeu")


from Lutadores import *

if __name__ == "__main__":
    jj = Jiujitsu("Lutador 1")
    mma = MMA("Lutador 2")
    jj.soco(mma)
    print(mma)
    mma.cruzado(jj)
    print(jj)
    mma.superman_punch(jj)
    print(jj)

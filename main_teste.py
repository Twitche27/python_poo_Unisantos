from Classes_teste import *

if __name__ == "__main__":
    bolt = Corredor("Usain Bolt", 38, 86)
    print(bolt)
    print(bolt.aquecer())
    print(bolt.correr())
    phelps = Nadador("Michael Phelps", 39, 88)
    print(phelps)
    print(phelps.aquecer())
    print(phelps.nadar())
    quintana = Ciclista("Nairo Alexander Quintana Rojas", 34, 59)
    print(quintana)
    print(quintana.aquecer())
    print(quintana.pedalar())
    keller = Triatleta("Fernanda Keller", 61, 56)
    print(keller)
    print(keller.aquecer())
    print(keller.realizar_maratona())
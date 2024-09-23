from funcs import *

if __name__ == "__main__":
    f2 = Gerente("Geraldo", "111111", 123.5, 123, 6661)
    f3 = OperadorCaixa("Geraldo", "111111", 123.5, 123, 6661)
    f4 = Seguranca("Geraldo", "111111", 123.5, 123, 6661)
    f3.autenticar(6661, 123)
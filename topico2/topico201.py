import datetime

def escrevehora():
    print(datetime.datetime.now())

def sub(a, b, func):
    func()
    return a - b

soma = lambda param1: print(param1)

tete = [10, 22, 3, 57, 99, 54, 103 , 259, 254]

def funcDiferenteZero(x):
    r = x % 2 != 0
    if (r):
        return x

retornaaquilista = list(filter(funcDiferenteZero, tete))

print(globals()["retornaaquilista"])
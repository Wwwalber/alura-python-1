from carro import Carro
from moto import Moto

carro1 = Carro('Ford', 'Focus', 4)
carro2 = Carro("Honda", "Civic", 2)
carro3 = Carro("Ford", "Fusion", 4)

moto1 = Moto("Kawazaqui", "Ninja", 1)
moto2 = Moto("Honda", "CBR 400CC", 2)
moto3 = Moto("Yamaha", "XJ6", 1)
moto4 = Moto("Honda", "CG 160", 2)

def main():
    print('Hello!')
    print(carro1)
    print(carro2)
    print(carro3)
    print(moto1)
    print(moto2)
    print(moto3)

if __name__ == '__main__':
    main()
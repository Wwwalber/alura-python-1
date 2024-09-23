# Crie uma classe chamada Veiculo com um método abstrato chamado ligar.

from abc import ABC, abstractmethod

class Veiculo(ABC):
    @abstractmethod
    def ligar(self):
        pass

    def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
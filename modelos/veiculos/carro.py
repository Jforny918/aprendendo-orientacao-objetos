from modelos.veiculos.veiculo import Veiculo

class Carro(Veiculo):
    def __init__(self, marca, modelo, portas):
        super().__init__(marca, modelo)
        self.portas = portas

    def __str__(self):
        info_veiculo = super().__str__()
        return f'{info_veiculo} e tem {self.portas} portas.'

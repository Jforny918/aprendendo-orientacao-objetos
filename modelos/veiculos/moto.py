from modelos.veiculos.veiculo import Veiculo

class Moto(Veiculo):
    def __init__(self, marca, modelo, tipo):
        super().__init__(marca, modelo)
        self.tipo = tipo

    def __str__(self):
        info_veiculo = super().__str__()
        return f'{info_veiculo} e é uma moto do tipo {self.tipo}.'

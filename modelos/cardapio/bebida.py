from modelos.cardapio.item_cardapio import ItemCardapio

class Bebida (ItemCardapio):
    def __init__ (self, nome, preco, tamanho):
        super().__init__(nome,preco) #chamando o construtor da classe mae
        self.tamanho = tamanho #atributo especifico da classe bebida foi criado pois a classe bebida herda de item_cardapio que ja possui o atributo nome e preco

    def __str__(self):
        return self._nome
    
    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.05)
      
    
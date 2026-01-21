from modelos.cardapio.item_cardapio import ItemCardapio

class Prato (ItemCardapio): 
    def __init__(self, nome, preco, descricao):
        super().__init__(nome, preco)
        self.descricao = descricao #atributo especifico da classe prato foi criado pois a classe prato herda de item_cardapio que ja possui o atributo nome e preco

    def __str__(self):
        return self._nome

    def aplicar_desconto(self):
        self._preco -= (self._preco * 0.08)
      
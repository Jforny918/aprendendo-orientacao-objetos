from modelos.restaurante import Restaurante
from modelos.cardapio.bebida import Bebida
from modelos.cardapio.prato import Prato
from modelos.cardapio.sobremesa import Sobremesa

restaurante_praca = Restaurante ('praca', 'gourmet')
bebida_suco = Bebida('Suco de Laranja', 5.00, '300ml')
bebida_suco.aplicar_desconto()

bebida_agua = Bebida('Água sem gás', 3.00, '500ml')
bebida_agua.aplicar_desconto()

prato_bife = Prato('Bife a cavalo', 25.00, '')
prato_bife.aplicar_desconto()

prato_strogonoff = Prato('Strogonoff de frango', 30.00, '')
prato_strogonoff.aplicar_desconto()

pave_chcolate = Sobremesa('Pavê de chocolate', 12.00, 'pudim', 'médio', 'Delicioso pavê com camadas de chocolate e creme.')
pave_chcolate.aplicar_desconto()

bolo_banana = Sobremesa('Bolo de banana', 10.00, 'bolo', 'grande', 'Bolo caseiro de banana com cobertura de açúcar e canela.')
bolo_banana.aplicar_desconto()

restaurante_praca.adicionar_no_cardapio(pave_chcolate)
restaurante_praca.adicionar_no_cardapio(bolo_banana)
restaurante_praca.adicionar_no_cardapio(bebida_suco)
restaurante_praca.adicionar_no_cardapio(bebida_agua)
restaurante_praca.adicionar_no_cardapio(prato_bife)
restaurante_praca.adicionar_no_cardapio(prato_strogonoff)

def main():
  restaurante_praca.exibir_cardapio()

if __name__ == '__main__':
    main()





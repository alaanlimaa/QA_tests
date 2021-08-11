from carrinho import Carrinho

carrinho = Carrinho()
itens = {'Notebook': 2500.00, 'Celular': 1282.00, 'Teclado': 158.98, 'Caneta': 2.68, 'Mouse': 69.98,
         'Lapis': 2.68, 'Headset': 1900.65, 'Fonte': 1900.65, 'Borracha': 0}
carrinho.add_item_carrinho(itens)

# APRESENTAÇÃO DOS DADOS

carrinho.view_lista_maior_produto()
carrinho.view_lista_menor_produto()
carrinho.view_carrinho()
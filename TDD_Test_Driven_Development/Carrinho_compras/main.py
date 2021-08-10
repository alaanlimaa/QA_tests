from carrinho import Carrinho

carrinho = Carrinho()
itens = {'Notebook': 19000.00, 'Celular': 1282.00, 'Teclado': 158.98, 'Caneta': 2.68, 'Mouse': 69.98,
         'Lapis': 0, 'Headset': 1900.65, 'Fonte': 1900.65, 'Borracha': 0}
carrinho.add_item_carrinho(itens)


print(carrinho)

print(carrinho.maior_produto)
print(carrinho.menor_produto)
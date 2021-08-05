from carrinho import Carrinho

carrinho = Carrinho()
itens = {'Notebook': 1900.65, 'Celular': 1282.00, 'Teclado': 158.98, 'Caneta': 2.68, 'Mouse': 69.98,
         'Lapis': 2.68}
for produto, valor in itens.items():
    carrinho.add_item_carrinho(produto, valor)

print(carrinho)

print(carrinho.maior_valor())
print(carrinho.menor_valor())
print(carrinho.menor_produto())

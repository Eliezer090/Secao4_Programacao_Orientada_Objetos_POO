"""
Aagregação uma classe depende da outra para funcionar corretamente
"""
from Classes.ClassesAgregacao import CarrinhoCompras, Produto

carrinho = CarrinhoCompras()
print(carrinho.soma_total())

p1 = Produto('Camiseta', 50)
p2 = Produto('iPhone', 10000)
p3 = Produto('caneca', 15)

carrinho.inserrir_produtos(p1)
carrinho.inserrir_produtos(p2)
carrinho.inserrir_produtos(p3)
carrinho.inserrir_produtos(p3)
carrinho.inserrir_produtos(p2)
carrinho.lista_produto()
print(carrinho.soma_total())

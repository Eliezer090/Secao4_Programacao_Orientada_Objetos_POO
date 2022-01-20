
class Produto:
    def __init__(self, nome, preco, telefone):
        self.nome = nome
        self.preco = preco
        self.telefone = telefone

    def desconto(self, percentual):
        self.preco = self.preco - (self.preco * (percentual / 100))

    # Getter
    @property
    def preco(self):
        return self._preco

    # Setter
    @preco.setter
    def preco(self, valor):
        # Checando se o valor é uma instancia de str
        if isinstance(valor, str):
            valor = float(valor.replace('R$', ''))
        self._preco = valor

    # Getters e setters sao basicamente filtros que podemos colocar no nosso código para tratar certas coisas
    @property
    def telefone(self):
        return self._telefone

    @telefone.setter
    def telefone(self, valor):
        if '(' in valor:
            valor = valor.replace('(', '')
            valor = valor.replace(')', '')
            valor = valor.replace('-', '')
        self._telefone = valor


p1 = Produto("Camiseta", 50, '(55)99293-12333')
p1.desconto(10)
print(p1.preco)
print(p1.telefone)

p2 = Produto('Caneca', 'R$10', '(11)92839-13323')
p2.desconto(10)
print(p2.preco)
print(p2.telefone)

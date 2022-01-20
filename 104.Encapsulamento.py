"""
_ protected(Na verdade é public mas com um _ na frente só para dizer que nao deve ser acessado)
__ private (Nao lista e nem deixa alterar o valor dele )
As regras acima tmabem funciona com métodos/Funcoes nao somente com variaveis
"""


class BaseDados:
    def __init__(self):
        self.__dados = {}

    # Se caso eu quiser liberar os valores dos __dados por dados pode ser feito por getters e setters
    @property
    def dados(self):
        return self.__dados

    def inserir_cliente(self, id, nome):
        if 'clientes' not in self.__dados:
            self.__dados['clientes'] = {id: nome}
        else:
            self.__dados['clientes'].update({id: nome})

    def lista_clientes(self):
        for id, nome in self.__dados['clientes'].items():
            print(id, nome)

    def apaga_cliente(self, id):
        del self.__dados['clientes'][id]


db = BaseDados()
db.inserir_cliente(1, 'otavio')
db.inserir_cliente(2, 'Luiz')
db.inserir_cliente(3, 'Eliezer')

# Aqui ele vai criar outro __dados
db.__dados = 'outra'
print(db.__dados)

db.lista_clientes()
# O atributo __dados da class BaseDados está em: db._BaseDados__dados, da erro que nao existe mas pode ser acessado mas nao deve.
print(db._BaseDados__dados)

print(db.dados)

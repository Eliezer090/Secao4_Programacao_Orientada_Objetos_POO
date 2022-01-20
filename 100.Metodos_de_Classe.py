from random import randint


class Pessoa:
    ano_atual = 2021

    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade

    # Este é um método de instancia  e precisa refceber o self
    def get_ano_nascimento(self):
        print(self.ano_atual - self.idade)

    # Este é um método de classe ele não se refere a instancia self mas se refere a class,
    # é utilizado para declarar coisas globais da classe, por isso do decorador
    @classmethod
    def por_ano_nascimento(cls, nome, ano_nascimento):
        # Com o decorador acima tenho um metodo da classe ou seja o cls instancia a class Pessoa
        idade = cls.ano_atual - ano_nascimento
        return cls(nome, idade)

    # É como uma funcao normal, mas nao podemos utilizar nem o self(Instancia) nem a clas(Que seria nossa classe)
    @staticmethod
    def gera_id():
        # O decorador staticmethod quer dizer que nao precisa de instancia só esta aqui dentro da class por organizacao mesmo
        return randint(1, 999)


p1 = Pessoa.por_ano_nascimento("Otavio", 1997)
print(p1.idade)
print(p1.gera_id())

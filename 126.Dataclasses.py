from dataclasses import dataclass

"""
Sem dataclass
class Pessoa:
    def __init__(self, nome, sobrenome):
        self.nome = nome
        self.sobrenome = sobrenome

p1 = Pessoa('a', 'b')
p2 = Pessoa('a', 'b')
print(p1 == p2) #Isso aqui é false pq n temos o método __eq__ imprementado
"""

"""
pode ser passado parametro para essa anotação para nao implementar método automaticos, procurrar na documentação
    o que cada coisa quer dizer
@dataclass(eq=False, rep=False, order=True, frozen=False, init=True) 
"""


# Com data class
@dataclass
class Pessoa:
    nome: str
    sobrenome: str


p1 = Pessoa('a', 'b')
p2 = Pessoa('a', 'b')
print(p1 == p2)

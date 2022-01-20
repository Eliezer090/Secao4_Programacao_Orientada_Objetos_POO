from Classes.ClassesHerancaSipls import Cliente, Aluno, ClienteVip

c1 = Cliente('Eliezer', 24)
print(c1.nome)
c1.comprar()
c1.falar()
a1 = Aluno('Maria', 30)
print(a1.nome)
a1.estudar()
a1.falar()


c2 = ClienteVip('Rose', 22, "Eduarda")
c2.falar()
c2.comprar()

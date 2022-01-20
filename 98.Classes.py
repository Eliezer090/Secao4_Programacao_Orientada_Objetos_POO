from pessoa import Pessoa

p1 = Pessoa('Luiz', 29)
p2 = Pessoa('João', 32)

p1.falar('eu falando')
p1.falar('eu falando 2')
p1.parar_falar()
p1.parar_comer()
p1.falar('maca')

p2.falar('POO')
p2.comer('sorvete')


print(p1.get_ano_nascimento())
print(p2.get_ano_nascimento())

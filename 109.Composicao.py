"""
Usando uma classe para compor a outra e mostrando quando é apagado as coisas
"""

from Classes.ClassesComposicao import Cliente

cliente1 = Cliente('Luiz', 32)
cliente1.inserre_enderecos('Belo Horizonte', 'MG')
cliente1.lista_enderecos()
print()

cliente2 = Cliente('Maria', 55)
cliente2.inserre_enderecos('Salvador', 'BA')
cliente2.inserre_enderecos('Rio', 'RJ')
cliente2.lista_enderecos()

print("#######################")

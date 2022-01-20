"""
Comunicação entre classes
"""
from Classes.ClassesAssociacao import Escritor, Caneta, MaquinaEscrever
escritor = Escritor('JOAO')
# print(escritor.nome)

caneta = Caneta('bic')
# print(caneta.marca)

maquina = MaquinaEscrever()
maquina.escrever()


escritor.ferramenta = maquina
escritor.ferramenta.escrever()

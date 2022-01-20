"""
Não se limita somente a arquivos, pode ser feito:
- conexao com base dados onde precisa ser fechado
- Conexao de rede
- Captura e depois solta algo pode ser utilizado o gerenciador de contexto
"""
from contextlib import contextmanager

# Maneira 1 de criar Context Mananger


class Arquivo():
    def __init__(self, arquivo, modo):
        print('abrindo arquivo')
        self.arquivo = open(arquivo, modo)

    def __enter__(self):
        print('Retornando arquivo')
        return self.arquivo

    # Os demais parametros alem do Self são para exeções, serve para tratarmos exceções também
    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Fechando arquivo')
        self.arquivo.close()
        print(exc_type)
        print(exc_val)
        print(exc_tb)
        # Somente dar o true depois que tratou a exeção
        return True


with Arquivo('abc.txt', 'w') as arquivo:
    arquivo.write('Alguma coisa')
    # Para estourar o erro no __exit__
    arquivo.aaaaa('Alguma coisa')


# Maneira 2 de criar Context Mananger
@contextmanager
def abrir(arquivo, modo):
    try:
        print("Abrindo arquivo")
        arquivo = open(arquivo, modo)
        # Serve para continuar ou seja fazer o finally ser executado
        yield arquivo
    finally:
        print('Fechando arquivo')
        arquivo.close()


with abrir('abc.txt', 'w') as arquivo:
    arquivo.write("Linha 1")
    arquivo.write("Linha 2")
    arquivo.write("Linha 3")

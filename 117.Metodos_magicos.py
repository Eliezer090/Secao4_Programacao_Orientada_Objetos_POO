# https://rszalski.github.io/magicmethods/

class A:
    # Este seria o método construtor desta classe em pyhton, mas geralmente é usado o __init__ de fato
    def __new__(cls, *args, **kwargs):
        print('Eu sou o New')
        return super().__new__(cls)

    def __init__(self):
        print('Eu sou init')

    # meio que transforma a class em uma função
    def __call__(self, *args, **kwargs):
        print(args)
        print(kwargs)

    def fala_oi(self):
        print('Oi')

    # sera chamado sempre que tentar setar um atributo
    def __setattr__(self, key, value):
        if key == 'nome':
            self.__dict__[key] = 'Nao pode fazer isso'
        else:
            self.__dict__[key] = value

    def __len__(self):
        return 55


a = A()
# Por causa do metodo __call__ a class se comporta como uma função, mas o resto da classe funciona normalmente
# o call só sera chamado quando é passado parametros
a(1, 2, 3, 4, 5, nome="Luiz")
a.fala_oi()
print("############################")
a.nome = 'Luiz'
print(a.nome)
a.sobrenome = 'paulo'
print(a.sobrenome)

print(len(a))

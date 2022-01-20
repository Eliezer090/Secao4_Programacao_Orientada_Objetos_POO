# Superclasse
class Pessoa:
    def __init__(self, nome, idade):
        self.nome = nome
        self.idade = idade
        self.nomeClasse = self.__class__.__name__

    def falar(self):
        print(f'{self.nomeClasse} falando')


class Cliente(Pessoa):
    # Subclasses
    def comprar(self):
        print(f'{self.nomeClasse} comprando')

    def falar(self):
        print(f'qualquer falarndo cliente')


class ClienteVip(Cliente):
    # Só o cliente vip tem algo a mais pode ser feito asism
    def __init__(self, nome, idade, sobrenome):
        super().__init__(nome, idade)  # Instanciando o init da Pessoa
        self.sobrenome = sobrenome

    # Sobrepondo a funcao Falar da pessoa

    def falar(self):
        super().falar()  # Define que o falar da Pessoa deve ser executado antes
        # Pode ser feito assim tambem para chamar de outras classes
        Pessoa.falar(self)
        print(f'{self.nome} {self.sobrenome} vip falando')


class Aluno(Pessoa):
    # Subclasses
    def estudar(self):
        print(f'{self.nomeClasse} estudando')

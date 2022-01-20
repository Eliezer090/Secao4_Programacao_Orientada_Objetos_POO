from Classes.Classe122DesafioPOO import Banco, Cliente, ContaPoupanca, ContaCorrente

banco = Banco()

cliente1 = Cliente('Luiz', 30)
cliente2 = Cliente('Eduardo', 10)

conta1 = ContaPoupanca(1111, 254136, 0)
conta2 = ContaCorrente(2222, 254137, 0)

cliente1.inserir_conta(conta1)
cliente2.inserir_conta(conta2)

banco.inserir_cliente(cliente1)
banco.inserir_cliente(cliente2)

cliente1.conta.depositar(50)
cliente1.conta.Sacar(20)

cliente2.conta.depositar(0)
cliente2.conta.Sacar(99)

from Classes.ClassContaPoupanca import ContaPoupanca
from Classes.ClassContaCorrente import ContaCorrente

cp = ContaPoupanca(111, 222, 0)
cp.depositar(15)
cp.sacar(5)
print("###############")
cc = ContaCorrente(111, 333, 0, 500)
cc.depositar(100)
cc.sacar(6000)
cc.depositar(1000)
cc.sacar(50)
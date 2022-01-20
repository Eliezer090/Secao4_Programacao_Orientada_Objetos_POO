

class A:
    vc = 123

    def __init__(self):
        self.vc = 5555


a1 = A()
a2 = A()

a1.vc = 321

print(f'a1: {a1.__dict__}')
print(f'a2: {a2.__dict__}')
print(f'Class: {A.__dict__}')

print(a1.vc)
print(a2.vc)
print(A.vc)

print("inverte")
A.vc = 321
print(a1.vc)
print(a2.vc)
print(A.vc)

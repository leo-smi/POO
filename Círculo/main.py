from círculo import Círculo

c1 = Círculo(raio=2.7, um='mm')
print(f'Diâmetro = {c1.diâmetro(precisão=4)}')
print(f'Circunferência = {c1.circunferência(precisão=4)}')
print(f'Área = {c1.área(precisão=4)}')
print(c1.__str__())
print(c1.__repr__())


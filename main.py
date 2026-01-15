from modelos.veiculos.carro import Carro
from modelos.veiculos.moto import Moto

carro1 = Carro('Toyota', 'Corolla', 4)
carro2 = Carro('Honda', 'Civic', 2)
carro3 = Carro('Ford', 'Mustang', 2)

moto1 = Moto('Harley-Davidson', 'Street 750', 'Cruiser')
moto2 = Moto('Ducati', 'Panigale V4', 'Esportiva')
moto3 = Moto('Kawasaki', 'Ninja 400', 'Esportiva')

print(carro1)
print(carro2)
print(carro3)

print("=" * 30)

print(moto1)
print(moto2)
print(moto3)

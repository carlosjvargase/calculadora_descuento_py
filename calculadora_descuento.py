'''
En una fábrica de computadoras se planea ofrecer a los clientes un descuento que dependerá del número de computadoras que compre. 
Si las computadoras son menos de cinco se les dará un 10% de descuento sobre el total de la compra; 
si el número de computadoras es mayor o igual a cinco pero menos de diez se le otorga un 20% de descuento; 
y si son 10 o más se les da un 40% de descuento. El precio de cada computadora es de $3.500.000
'''

n_computadoras = int(input("Ingrese el numero de computadoras compradas: "))
precio = 3500000

if (n_computadoras <5) and (n_computadoras >1):
  #Descuento del 10%
  total = (precio * n_computadoras) * 0.90
  print(f"El precio total es: {total}")
elif (n_computadoras >=5) and (n_computadoras <10):
  #Descuento del 20%
  total = (precio * n_computadoras) * 0.80
  print(f"El precio total es: {total}")  
elif (n_computadoras >=10):
  #Descuento del 40%
  total = (precio * n_computadoras) * 0.60
  print(f"El precio total es: {total}")
else:
  print("Tienes que ingresar un valor positivo")
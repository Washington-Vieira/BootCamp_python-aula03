import math

# numero_01 = int(input("inserior um numero inteiro"))
# numero_02 = int(input("inserior outro numero inteiro"))

# resultado = numero_01 // numero_02

# print(resultado)


raio_do_circulo = float(input("Digite o raio: "))
area_do_circulo =  math.pi * raio_do_circulo ** 2
#area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
print(f"{area_do_circulo:.2f}")
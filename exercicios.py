import math

# numero_01 = int(input("inserior um numero inteiro"))
# numero_02 = int(input("inserior outro numero inteiro"))

# resultado = numero_01 // numero_02

# print(resultado)


# raio_do_circulo = float(input("Digite o raio: "))
# area_do_circulo =  math.pi * raio_do_circulo ** 2
# #area_do_circulo_formatada = "{:.2f}".format(area_do_circulo)
# print(f"{area_do_circulo:.2f}")

input("insira uma data no formato dd/mm/aaaa")
data_do_usuario = "23/09/2024"
lista_de_dia_mes_ano = data_do_usuario.split("/")
print(f"O elemento 1 e o : {lista_de_dia_mes_ano[0]}")
print(f"O elemento 2 e o : {lista_de_dia_mes_ano[1]}")
print(f"O elemento 3 e o : {lista_de_dia_mes_ano[2]}")
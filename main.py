# Exemplo typeError

# try:
#     resultado = len("washington")
#     print(resultado)
# except TypeError as e:
#     print(e)
# else:
#     print("tudo ocorreu bem")
# finally:
#     print("o importante e participar")

numero = int(input("insira um numero: "))
#isinstance consigo verificar a variavél se é do tipo que preciso
if isinstance(numero, int):
    print("A variavel é um inteiro")
else:
    print("A variavel não é um inteiro")
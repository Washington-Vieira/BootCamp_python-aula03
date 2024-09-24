# Exemplo typeError

try:
    resultado = len("washington")
    print(resultado)
except TypeError as e:
    print(e)
else:
    print("tudo ocorreu bem")
finally:
    print("o importante e participar")
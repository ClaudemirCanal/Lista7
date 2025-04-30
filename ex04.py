soma = 0
contador = 0

for numero in iter(lambda: int(input("Digite um número inteiro (-1 para sair): ")), -1):
    soma += numero
    contador += 1

if contador > 0:
    media = soma / contador
    print(f"A média dos números digitados é: {media}")
else:
    print("Nenhum número válido foi digitado.")
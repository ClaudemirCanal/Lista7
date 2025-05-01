maior = 0

for altura in iter(lambda: float(input("Digite sua altura (0 para encerrar): ")), 0):
    if altura > maior:
        maior = altura

print("A maior altura digitada foi", maior)
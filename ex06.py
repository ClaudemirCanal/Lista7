numero = int(input('Digite um numero: '))
fatorial = 1
for numero in range(numero, 0, -1):
    fatorial *= numero
    print(f'{numero} --> {fatorial}')
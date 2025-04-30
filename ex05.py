for _ in range(1000):
    senha = input("Digite uma senha (mínimo 8 caracteres): ")
    if len(senha) == 8:
        print("Senha válida!")
        break
    else:
        print("Senha inválida! Tente novamente.")
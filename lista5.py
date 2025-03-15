def criptografar(numero):
    """Criptografa um número de quatro dígitos"""
    # Converte o número para string e separa os dígitos
    digitos = [int(d) for d in str(numero)]

    # Aplica a transformação: (dígito + 7) % 10
    digitos = [(d + 7) % 10 for d in digitos]

    # Troca de posições
    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]

    # Retorna o número criptografado como string
    return "".join(map(str, digitos))


def descriptografar(numero):
    """Descriptografa um número de quatro dígitos criptografado"""
    # Converte o número para string e separa os dígitos
    digitos = [int(d) for d in str(numero)]

    # Inverte a troca de posições
    digitos[0], digitos[2] = digitos[2], digitos[0]
    digitos[1], digitos[3] = digitos[3], digitos[1]

    # Reverte a transformação: (dígito - 7 + 10) % 10
    digitos = [(d - 7 + 10) % 10 for d in digitos]

    # Retorna o número original como string
    return "".join(map(str, digitos))


# Executando o programa
num = input("Digite um número de 4 dígitos para criptografar: ")

# Verifica se a entrada tem 4 dígitos e é numérica
if len(num) == 4 and num.isdigit():
    criptografado = criptografar(num)
    print(f"Número criptografado: {criptografado}")

    # Descriptografando para testar
    original = descriptografar(criptografado)
    print(f"Número descriptografado: {original}")
else:
    print("Erro! Digite um número válido de 4 dígitos.")
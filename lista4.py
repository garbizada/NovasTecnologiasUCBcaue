def contar_vogais(frase):
    vogais = "aeiou"
    frase = frase.lower()  # Converte para minúsculas
    contagem = {vogal: frase.count(vogal) for vogal in vogais}  # Conta cada vogal
    total = sum(contagem.values())  # Soma todas as vogais
    return contagem, total

# Solicita a frase ao usuário
frase_usuario = input("Digite uma frase: ")

# Conta as vogais
contagem_vogais, total_vogais = contar_vogais(frase_usuario)

# Exibe os resultados
print(f"A frase contém {total_vogais} vogais no total.")
print("Frequência de cada vogal:", contagem_vogais)
def separate_digits():
    number = input("Digite um número de cinco dígitos: ")
    if len(number) == 5 and number.isdigit():
        print("   ".join(number))
    else:
        print("Por favor, insira exatamente cinco dígitos.")

if __name__ == "__main__":
    separate_digits()
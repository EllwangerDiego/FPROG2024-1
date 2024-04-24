def is_prime(numero):
    if numero <= 1:
        return False  # Números menores ou iguais a 1 não são primos

    for i in range(2, int(numero ** 0.5) + 1):
        if numero % i == 0:
            return False  # Se encontrar um divisor, não é primo
    return True  # Se nenhum divisor foi encontrado, é primo

# Exemplos de uso da função
print(is_prime(5))  # Saída: True
print(is_prime(10))  # Saída: False
print(is_prime(13))  # Saída: True
print(is_prime(25))  # Saída: False
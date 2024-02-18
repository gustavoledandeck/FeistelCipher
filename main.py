from random import randint

"Algoritmo da cifra de Feistel Exercício 7 do laboratório de Segurança de Redes"
'''
O algoritmo utiliza a cifra de feistel com entrada de inteiros de 0 à 255 gerados
pela função geradora de números inteiros aleatórios do python
'''
def encrypt(input, key):
    """
    Criptografa um bloco de 8 bits usando o algoritmo Feistel com dois estágios.
    >> é o right_shift e << é o left_shift
    Args:
        input (int): Bloco de entrada de 8 bits como inteiro.
        key (int): Chave de 4 bits como inteiro.

    Returns:
        int: Bloco criptografado como inteiro.
    """

    l = input >> 4
    r = input & 0b1111

    for i in range(2):
        temp = l
        l = r
        r = temp ^ f(r, key >> (3 - i) & 0b1111)

    return (r << 4) | l


def decrypt(input, key):
    """
    Descriptografa um bloco de 8 bits criptografado usando o algoritmo Feistel com dois estágios.

    Args:
        input (int): Bloco criptografado de 8 bits como inteiro.
        key (int): Chave de 4 bits como inteiro.

    Returns:
        int: Bloco descriptografado como inteiro.
    """

    l = input >> 4
    r = input & 0b1111

    for i in range(1, -1, -1):
        temp = l
        l = r
        r = temp ^ f(r, key >> (3 - i) & 0b1111)

    return (r << 4) | l


def f(r, k):
    """
    Função F do algoritmo Feistel.

    Args:
        r (int): Sub-bloco direito como inteiro.
        k (int): Chave como inteiro.

    Returns:
        int: Saída da função F como inteiro.
    """

    return (r ^ k) & 0b1111

def keyGenerator():
    # Chave de 4 bits
    key = bin(randint(1, 16))
    return int(key, 2)

def inputGenerator():
    # Bloco de entrada de 8 bits
    input = bin(randint(1, 256))
    return int(input, 2)

if __name__ == "__main__":

    input = inputGenerator()
    key = keyGenerator()

    #input gerado:
    print(f"em inteiro: {input}")
    print(f"em binário: {bin(input)}")

    #key gerada:
    print(f"em inteiro: {key}")
    print(f"em binário: {bin(key)}")

    # Criptografar
    encrypted = encrypt(input, key)
    print("Bloco criptografado (inteiro):", encrypted)
    print("Bloco criptografado (bin):", bin(encrypted))

    # Decriptografar
    decrypted = decrypt(encrypted, key)
    print("Bloco descriptografado:", decrypted)
    print("Bloco criptografado (bin):", bin(decrypted))
M = 2
N = 27


# Following function generates the key matrix for the key string
def get_key_matrix(key):
    k = 0
    key_matrix = [[0] * M for _ in range(M)]
    for i in range(M):
        for j in range(M):
            key_matrix[i][j] = ord(key[k]) % 65 + 1
            k += 1

    return key_matrix


# Generate vector for the message
def get_message_vector(message):
    k = 0
    message_size = len(message) // M if len(message) % M == 0 else len(message) // M + 1
    message_vector = [[0] * M for _ in range(message_size)]

    for i in range(message_size):
        for j in range(M):
            if k >= len(message):
                message_vector[i][j] = 0
            else:
                message_vector[i][j] = ord(message[k]) % 65 + 1
            k += 1

    return message_vector


# Following function encrypts the message
def encrypt(message_vector, key_matrix):
    cipher_matrix = [[0] * M for _ in range(M)]
    i = 0

    for message_sequence in message_vector:
        for j in range(M):
            for x in range(M):
                cipher_matrix[i][j] += (message_sequence[x] * key_matrix[x][j])
            cipher_matrix[i][j] = cipher_matrix[i][j] % N
        i += 1

    return cipher_matrix


# Generate the encrypted text from the encrypted vector
def get_encrypted_text(cipher_matrix):
    cipher_text = []
    for i in range(M):
        for j in range(M):
            cipher_text.append(chr(cipher_matrix[i][j] - 1 + 65))
    return cipher_text


def hill_cipher(message, key):
    key_matrix = get_key_matrix(key)
    message_vector = get_message_vector(message)
    print(message_vector, key_matrix)

    cipher_matrix = encrypt(message_vector, key_matrix)
    cipher_text = get_encrypted_text(cipher_matrix)
    print("Ciphertext: ", "".join(cipher_text))


def main():
    message = "four"
    key = "khcg"

    hill_cipher(message.upper(), key.upper())


if __name__ == "__main__":
    main()

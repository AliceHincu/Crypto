alphabet = [i for i in range(27)]
letter_to_alphabet = {'_': 0}
alphabet_to_letter = {0: '_'}
for i in range(26):
    c = chr(ord('A') + i)
    letter_to_alphabet[c] = i + 1
    alphabet_to_letter[i + 1] = c

def gcd(a, b):
    while a != b:
        if a > b:
            a -= b
        else:
            b -= a
    return a

def is_prime(n):
    if n < 2: return False
    if n == 2: return True
    if n % 2 == 0: return False
    i = 3
    while i * i <= n:
        if n % i == 0:
            return False
        i += 2
    return True

def encode(block):
    block = block[::-1]
    value = 0
    for i in range(len(block)):
        value += (len(alphabet) ** i) * letter_to_alphabet[block[i]]
    return value

def decode(value):
    block = ""
    while value > 0:
        block += alphabet_to_letter[value % len(alphabet)]
        value //= len(alphabet)
    while len(block) < k:
        block += '_'
    return block[::-1]

if __name__ == '__main__':
    ### CHANGE THESE -->
    k = 2
    l = 3

    p = 53
    q = 83

    ciphertext = "DEXCWGDPC"
    ### <-- CHANGE THESE

    while len(ciphertext) % l != 0:
        ciphertext += '_'

    n = p * q
    fi_n = (p - 1) * (q - 1)

    e = 3
    while e < fi_n and not (is_prime(e) and (gcd(e, fi_n) == 1)):
        e += 2

    d = pow(e, -1, fi_n)
    print(f'n = {n}, fi(n) = {fi_n}, e = {e}, d = {d}')

    blocks = []

    while len(ciphertext) > 0:
        block = ciphertext[:l]
        blocks.append(encode(block))
        ciphertext = ciphertext[l:]
        print(block, end = ' ')

    print()
    print(blocks)

    encoded_blocks = []
    for block in blocks:
        value = block ** d % n
        print(value, end = ' ')
        encoded_blocks.append(decode(value))

    print()

    print(encoded_blocks)
    print(''.join(encoded_blocks))
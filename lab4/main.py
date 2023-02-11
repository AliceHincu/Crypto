# from Crypto.Util.number import getPrime
#
# # generate alphabet
# alphabet = [i for i in range(27)]
# letter_to_alphabet = {'_': 0}
# alphabet_to_letter = {0: '_'}
# for i in range(26):
#     c = chr(ord('A') + i)
#     letter_to_alphabet[c] = i + 1
#     alphabet_to_letter[i + 1] = c
#
#
# def gcd(a, b):
#     while a != b:
#         if a > b:
#             a -= b
#         else:
#             b -= a
#     return a
#
#
# def is_prime(number):
#     if number < 2:
#         return False
#     if number == 2:
#         return True
#     if number % 2 == 0:
#         return False
#     i = 3
#     while i * i <= number:
#         if number % i == 0:
#             return False
#         i += 2
#     return True
#
#
# # convert from string to number
# def string_to_number(block):
#     block = block[::-1]
#     value = 0
#     for i in range(len(block)):
#         value += (len(alphabet) ** i) * letter_to_alphabet[block[i]]
#     return value
#
#
# # convert from number to string
# def number_to_string(value):
#     block = ""
#     while value > 0:
#         block += alphabet_to_letter[value % len(alphabet)]
#         value //= len(alphabet)
#     while len(block) < l:
#         block += '_'
#     return block[::-1]
#
#
# if __name__ == '__main__':
#     k = 2
#     l = 7
#     assert k < l, "initial block size must be greater than final block size"
#     nr_bits = 6
#     plaintext = "CRYPTOCRYPTOCRYPTO"
#
#     # generate 2 random prime numbers
#     p = getPrime(nr_bits)
#     q = getPrime(nr_bits)
#     while p == q:
#         q = getPrime(nr_bits)
#     print("p = ", p, " and q = ", q)
#
#     while len(plaintext) % k != 0:
#         plaintext += '_'
#     print(plaintext)
#
#     # the Euler function φ(n)
#     n = p * q
#     fi_n = (p - 1) * (q - 1)
#
#     # Randomly selects 1 < e < φ(n) with gcd(e, φ(n)) = 1
#     e = 3
#     while e < fi_n and not (is_prime(e) and (gcd(e, fi_n) == 1)):
#         e += 2
#
#     d = pow(e, -1, fi_n)
#
#     # public key is (n, e) and private key is d.
#     print(f'{n = }, {fi_n = }, {e = }, {d = }')
#
#     blocks = []
#
#     # split the message in k blocks
#     while len(plaintext) > 0:
#         block = plaintext[:k]
#         blocks.append(string_to_number(block))
#         plaintext = plaintext[k:]
#         print(block, end=' ')
#
#     print()
#     print(blocks)
#
#     encoded_blocks = []
#     for block in blocks:
#         value = block ** e % n
#         print(value, end=' ')
#         encoded_blocks.append(number_to_string(value))
#
#     print()
#     print(encoded_blocks)
#
#     ciphertext = "".join(encoded_blocks)
#     print(ciphertext)
#     print()
#
#     # reverse the process for decoding
#     blocks = []
#
#     while len(ciphertext) > 0:
#         block = ciphertext[:l]
#         blocks.append(string_to_number(block))
#         ciphertext = ciphertext[l:]
#         print(block, end=' ')
#
#     print()
#     print(blocks)
#
#     decoded_blocks = []
#     for block in blocks:
#         value = block ** d % n
#         print(value, end=' ')
#         decoded_blocks.append(number_to_string(value))
#
#     print()
#
#     print(decoded_blocks)
#     print(''.join(block.replace("_", "") for block in decoded_blocks))

N = 4


def getInvCount(arr):
    arr1 = []
    for y in arr:
        for x in y:
            arr1.append(x)
    arr = arr1
    inv_count = 0
    for i in range(N * N - 1):
        for j in range(i + 1, N * N):
            # count pairs(arr[i], arr[j]) such that
            # i < j and arr[i] > arr[j]
            if (arr[j] and arr[i] and arr[i] > arr[j]):
                inv_count += 1

    return inv_count


# find Position of blank from bottom
def findXPosition(puzzle):
    # start from bottom-right corner of matrix
    for i in range(N - 1, -1, -1):
        for j in range(N - 1, -1, -1):
            if (puzzle[i][j] == 0):
                return N - i


# This function returns true if given
# instance of N*N - 1 puzzle is solvable
def isSolvable(puzzle):
    # Count inversions in given puzzle
    invCount = getInvCount(puzzle)

    # If grid is odd, return true if inversion
    # count is even.
    if (N & 1):
        return ~(invCount & 1)

    else:  # grid is even
        pos = findXPosition(puzzle)
        if (pos & 1):
            return ~(invCount & 1)
        else:
            return invCount & 1


# Driver program to test above functions
if __name__ == '__main__':
    puzzle = [
        [0, 1, 2, 3, ],
        [4, 5, 6, 7, ],
        [8, 9, 10, 11, ],  # Value 0 is used for empty space
        [12, 13, 14, 15, ], ]

    print("Solvable") if isSolvable(puzzle) else print("Not Solvable")

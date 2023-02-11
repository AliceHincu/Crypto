import time
import timeit


# method 1: naive method to compute gcd ( recursion )
def gcd_naive(number_1, number_2):
    if number_2 == 0:
        return abs(number_1)
    return gcd_naive(number_2, number_1 % number_2)


# method 2: euclidean algo
# you can find the gcd of the value by taking the second number and making it the first, and taking the remainder of a/b
# to get the second.
def gcd_euclidean(number_1, number_2):
    while number_2:
        number_1, number_2 = number_2, number_1 % number_2
    return abs(number_1)


# method 3: Stein's Algorithm (Iterative version)
# Stein’s algorithm replaces division with arithmetic shifts, comparisons, and subtraction.
def gcd_stein(number_1, number_2):
    # gcd(a, 0) = a and gcd(0, b) = b because everything divides 0.
    if number_1 == 0:
        return number_2

    if number_2 == 0:
        return number_1

    # Finding K, where K is the greatest power of 2 that divides both a and b.
    k = 0
    # If a and b are both even, gcd(a, b) = 2*gcd(a/2, b/2) because 2 is a common divisor.
    while ((number_1 | number_2) & 1) == 0:  # x & 1 is equivalent to x % 2
        number_1 = number_1 >> 1  # x >> 1 is equivalent to x / 2
        number_2 = number_2 >> 1
        k = k + 1

    # Dividing a by 2 until a becomes odd. If a is odd and b is even, gcd(a, b) = gcd(a/2, b).
    # It is because 2 is not a common divisor.
    while (number_1 & 1) == 0:
        number_1 = number_1 >> 1

    # From here on, 'a' is always odd.
    while number_2 != 0:
        # If b is even, remove all factor of 2 in b (It is because 2 is not a common divisor.)
        while (number_2 & 1) == 0:
            number_2 = number_2 >> 1

        # If both a and b are odd, then gcd(a, b) = gcd(|a-b|/2, b). Note that difference of two odd numbers is even
        if number_1 > number_2:
            number_1, number_2 = number_2, number_1

        number_2 = (number_2 - number_1)

    #  the GCD is power(2, k) * b
    # ‘(x<<y)’ is equivalent to multiplying x with 2^y (2 raised to power y).
    return number_1 << k


def show_time():
    numbers = [[100000, 2000000],
               [778395889, 3458892359],
               [111243253543, 645756868585],
               [24325235525, 76595670506859],
               [334534543535543, 999999999999],
               [234121, 234131],
               [100000000, 1000000],
               [0, 7556658467],
               [7569567956959, 4536464363],
               [1, 5945995849],
               [4444444444444444444444444444444444444, 234239533508349064936],
               [4444444444444444444444444444444444444, 234239533508349064936]]

    # record start time
    t_0 = timeit.default_timer()
    for number in numbers:
        gcd_naive(number[0], number[1])
    # record end time
    t_1 = timeit.default_timer()
    elapsed_time = round((t_1 - t_0) * 10 ** 6, 3)  # microseconds
    print(f'Naive method took: {elapsed_time} µs')

    t_0 = timeit.default_timer()
    for number in numbers:
        gcd_euclidean(number[0], number[1])
    t_1 = timeit.default_timer()
    elapsed_time = round((t_1 - t_0) * 10 ** 6, 3)  # microseconds
    print(f'Euclidean method took: {elapsed_time} µs')

    t_0 = timeit.default_timer()
    for number in numbers:
        gcd_stein(number[0], number[1])
    t_1 = timeit.default_timer()
    elapsed_time = round((t_1 - t_0) * 10 ** 6, 3)  # microseconds
    print(f'Stein method took: {elapsed_time} µs')


if __name__ == '__main__':
    show_time()

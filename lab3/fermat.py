from math import ceil, sqrt, floor


# This function finds the value of a and b and  returns a+b and a-b
def fermat_factors(number, bound):
    # since fermat's factorization applicable for odd positive integers only
    if number <= 0:
        return [number]

    # check if n is an even number
    if (number & 1) == 0:
        return [floor(number / 2), 2]

    # check if is perfect root ->  both its square roots are its factors
    a = ceil(sqrt(number))
    if a * a == number:
        return [a, a]

    # Fermat’s Algorithm
    unicorns_exist = True
    k = 1
    while unicorns_exist:
        t0 = floor(sqrt(k * n))  # for every k, find the square root of k*n
        for t in range(t0 + 1, t0 + bound):  # until bound, increase value of t
            # if s is square root of t^2-kn then n = 1/k(t-s)(t+s)
            s = ceil(sqrt(t * t - k * n))
            if s * s == t * t - k * n:
                return [t - s, t + s]
        k += 1

    return [number, 1]


if __name__ == '__main__':
    n = 141467
    B = 200
    print(fermat_factors(n, B))

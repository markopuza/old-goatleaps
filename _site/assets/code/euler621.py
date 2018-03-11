from pyprimesieve import primes

n = 17526000000000

# for faster squaring operation
square = []
for i in range(int(n**0.5) + 10):
    square.append(i*i)
PRIMES = primes(int(n**0.5) + 10)


def sum_of_two_squares(n):
    if n <= 1: return 0
    # we do not care about the factors of 2
    while not n&1: n >>= 1
    if (n&3) == 3: return 0

    product = 1
    # factorize
    for prime in PRIMES:
        if square[prime] > n:
            break
        exp = 0
        while 0 == n % prime:
            exp += 1
            n //= prime
        if (prime&3) == 3 and (exp&1):
            return 0
        if (prime&3) == 1:
            product *= exp + 1
    if n > 1:
        product *= 2

    return product

def sum_of_three_squares(n):
    lamb = 0
    while n % 9 == 0:
        lamb += 1
        n //= 9
    if lamb > 0:
        if n % 24 == 11:
            return 3**lamb * sum_of_three_squares(n)
        if n % 24 == 19:
            return (2 * 3**lamb - 1) * sum_of_three_squares(n)
        if n % 72 in [3, 51]:
            return (3**(lamb + 1) - 1) * sum_of_three_squares(n) // 2
    return sum(sum_of_two_squares(n - k*k) for k in range(1, int(n ** 0.5) + 1))

def sum_of_three_triangles(n):
    return sum_of_three_squares(8*n+3)

if __name__ == "__main__":
    print('The answer is {:d}.'.format(sum_of_three_triangles(n)))

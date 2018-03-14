from pyprimesieve import factorize
from functools import reduce
from operator import mul
from itertools import chain, combinations

def powerset(s):
    return chain.from_iterable(combinations(s, r) for r in range(len(s)+1))

def s(n):
    ''' Computes s(n) as defined in the problem. s(n) = order of 2 modulo n-1. '''
    assert n % 2 == 0
    if n == 2:
        return -1
    curr, cnt = 2, 1
    while curr != 1:
        curr, cnt = (2 * curr) % (n - 1), cnt + 1
    return cnt

def s_inverse(k):
    # Factorize 2^k - 1
    factors = list(chain(*[[prime] * exp for prime, exp in factorize(2**k - 1)]))
    # Compute all divisors of 2^k - 1. These are candidates n for s(n + 1) = k
    divisors = set([reduce(mul, subset, 1) for subset in powerset(factors)])
    return [x + 1 for x in divisors if s(x + 1) == k]

def S(k):
    return sum(s_inverse(k))

# from sympy.ntheory import n_order, divisors
# S = lambda k: sum(x + 1 for x in divisors(2**k - 1) if n_order(2, x) == k)

# Fastest approach:
# from sympy.ntheory import mobius, divisor_sigma, divisors
# S = lambda k: sum(mobius(m) * (divisor_sigma(2**(k//m) - 1, 0) + divisor_sigma(2**(k//m) - 1, 1)) for m in divisors(k))

print(S(60))

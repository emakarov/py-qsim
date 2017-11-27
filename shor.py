"""
Shor.
See description here
https://arxiv.org/pdf/quant-ph/0010034.pdf
"""
import random
try:
    from math import gcd
except:
    from fractions import gcd


def step_1_euclidean_gcd(n):
    """
    Choose a random positive integer m. Use the polynomial time Euclidean
    algorithm to compute the greatest common divisor gcd (m,N)
    of m and N. If the greatest common divisor gcd (m,N) != 1, then we
    have found a non-trivial factor of N, and we are done.
    """
    m = random.randint(1, n-1)
    greatest = gcd(n, m)
    return m, greatest

def quantum_step_2():
    return


def shor(n):
    m, euclidean_gcd = step_1_euclidean_gcd(n)
    if euclidean_gcd != 1:
        print('found factor {} with m: {}'.format(euclidean_gcd, m))
        return
    print('not found with m: {}'.format(m))

if __name__ == "__main__":
    shor(6)

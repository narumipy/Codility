def solution(N, P, Q):
    res = []
    semiprimes = [0] * (N + 1)
    for i in range(4, len(semiprimes)):
        if is_semiprime(i):
            semiprimes[i] = 1 + semiprimes[i - 1]
        else:
            semiprimes[i] = semiprimes[i - 1]
    for i in range(len(P)):
        res.append(semiprimes[Q[i]] - semiprimes[P[i] - 1])
    return res


def prime_factors(n):
    i = 2
    factors = []
    while i * i <= n:
        if n % i:
            i += 1
        else:
            n /= i
            factors.append(i)
    if n > 1:
        factors.append(n)
    return factors


def is_semiprime(n):
    factors = prime_factors(n)
    m = len(factors)
    if m == 1 and n / factors[0] == factors[0]:
        return True
    if m == 2 and factors[0] * factors[1] == n:
        return True
    return False

if __name__ == '__main__':
    print(solution(26, [1, 4, 16], [26, 10, 20]))
    print(set(filter(lambda n: is_semiprime(n), [i for i in range(1, 27)])))

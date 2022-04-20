def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False
    
    root = int(n ** 0.5)
    for i in range(3, root+1, 2):
        if n % i == 0:
            return False
    return True


def gen_prime(start_prime_n, count):
    primes = []
    i = 0
    while i < count:
        if is_prime(start_prime_n):
            primes.append(start_prime_n)
            i += 1
        start_prime_n += 1
    return primes


if __name__ == '__main__':
    primes = gen_prime(2, 10)
    sum_primes = sum(primes)
    print('Sum: ', sum_primes)


def is_prime(n):
    if n <= 1:
        return False
    if n == 2:
        return True
    if n % 2 == 0:
        return False

    root = int(n**0.5)  # square root
    for i in range(3, root+1, 2):
        if n % i == 0:
            return False

    return True


def gen_prime(start, count):
    while True:
        if is_prime(start):
            yield start
            count -= 1
            if count == 0:
                return
        start += 1


if __name__ == "__main__":
    start, count = 2, 10
    primes = gen_prime(start, count)
    print('Sum: ', sum(primes))


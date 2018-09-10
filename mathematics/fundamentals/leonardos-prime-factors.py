# https://www.hackerrank.com/challenges/leonardo-and-prime/problem


def get_next_prime(lower, upper):
    for n in range(lower, upper + 1):
        is_prime = True
        for i in range(2, n):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            return n
    return 0


for _ in range(int(input())):
    n = int(input())
    primes = 0
    product = 1
    next_prime = 1  # I know, it's just an initial value

    done = False
    while not done:
        next_prime = get_next_prime(next_prime + 1, n)
        if next_prime:
            product *= next_prime
            if product <= n:
                primes += 1
            else:
                done = True
        else:
            done = True

    print(primes)

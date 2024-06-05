def sieve_of_eratosthenes(n):
    prime = [True for _ in range(n+1)]
    p = 2
    while p * p <= n:
        if prime[p] is True:
            for i in range(p * p, n+1, p):
                prime[i] = False
        p += 1
    prime_numbers = []
    for p in range(2, n+1):
        if prime[p]:
            prime_numbers.append(p)
    return prime_numbers

N = int(input())
prime_numbers = sieve_of_eratosthenes(N)
print(" ".join(map(str, prime_numbers)))
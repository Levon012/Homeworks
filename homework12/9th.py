"""Write a function that prints all prime numbers up to a given limit."""


def prime_numbers(limit):
    def is_prime(n):
        if n <= 1:
            return False
        for i in range(2, int(n ** 0.5) + 1):
            if n % i == 0:
                return False
        return True
    for j in range(2, limit + 1):
        if is_prime(j):
            print(j)
print(prime_numbers(31))


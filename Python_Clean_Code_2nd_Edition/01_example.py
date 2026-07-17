import math


def is_prime(n: int):
    if n <= 1:
        return False

    sqn = int(math.sqrt(n))
    for d in range(2, sqn + 1):
        if n % d == 0:
            return False

    return True


def find_prime_with_remainder(n: int, remainder: int, max_value: int = 5000) -> list[int]:
    """Find primes whose remainder when divided by n is specific value."""

    result = []
    i = 0

    while True:
        value = i * n + remainder
        if value > max_value:
            return result
        if is_prime(value):
            result.append(value)
        i += 1


if __name__ == '__main__':
    print(is_prime(2023))
    print(is_prime(49))
    print(find_prime_with_remainder(5, 2, 100))

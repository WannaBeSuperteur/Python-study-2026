import math

def is_prime(n):
    breakpoint()  # start debugger (Python 3.7+)
    if n <= 1:
        return False

    sqn = int(math.sqrt(n))
    for d in range(2, sqn):  # sqn + 1 is correct, sqn is wrong
        if n % d == 0:
            return False

    return True


if __name__ == '__main__':
    print(is_prime(2023))
    print(is_prime(49))

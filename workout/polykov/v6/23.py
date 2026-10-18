def is_prime(num):
    if num < 2:
        return False
    for i in range(2, num):
        if num % i == 0:
            return False
    return True

def prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num


def f(num, end):
    if num == end: return 1

    if num > end: return 0
    if num == 33: return 0

    if num < end: return f(num + 2, end) + f(prime(num), end)


print(f(2, 14) * f(14, 45)) # 881
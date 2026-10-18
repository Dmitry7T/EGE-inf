import math

def get_min_max_divisors(n):
    if n <= 1:
        return None, None

    min_div = n
    for i in range(2, int(math.sqrt(n)) + 1):
        if n % i == 0:
            min_div = i
            break
            
    if min_div == n:
        return None, None

    max_div = n // min_div
    return min_div, max_div

res = {}
for x in range(800001, 10**6): 
    min_div, max_div = get_min_max_divisors(x)
    if min_div is not None and max_div is not None:
        s = min_div + max_div
        if s % 138 == 0:
            res[str(x)] = s

    if len(res) >= 5:
        break

for key, value in res.items():
    print(f"{key} {value}")
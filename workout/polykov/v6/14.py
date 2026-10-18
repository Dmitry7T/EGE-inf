x = 11 * 15**65 + 18 * 15**38 - 14 * 15**17 + 19 * 15**11 + 18338

digits = "0123456789ABCDE"
res = ""

while x > 0:
    res += digits[x % 15]
    x //= 15

res[::-1]
print(len(set(res))) # 10
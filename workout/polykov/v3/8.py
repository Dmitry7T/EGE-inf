from itertools import product

ans = 0

octs_set = set()
for let in "1234567":
    for i in product("01234567", repeat=6):
        i_str = "".join(i)
        x_str = let + i_str[:3] + '2' + i_str[3:] + '3'
        octs_set.add(int(x_str, 8))


for let in "1234567": 
    for i in product("0123456789ABCDEF", repeat=5):
        i_str = "".join(i)
        x_str = let + i_str[:3] + 'A' + i_str[3:]
        x = int(x_str, 16)
        
        if x in octs_set:
            ans += 1

print(ans)
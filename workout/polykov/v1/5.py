for n in range(100, 1000):
    digits = [n % 10, n // 10 % 10, n // 100]
    
    digits.sort()

    if digits[0] == 0:
        i1 = int(str(digits[1]) + str(digits[0]))
    else:
        i1 = int(str(digits[0]) + str(digits[1]))
        
    i2 = int(str(digits[-1]) + str(digits[-2]))
    
    d = i2 - i1
    
    if d == 60:
        print(n)
        break
for x in "0123456789ABCDE":
    s = (int(f"67845{x}65", 15) + int(f"1{x}23456", 15))
    if s % 14 == 0:
        print(s / 14) # 80788834
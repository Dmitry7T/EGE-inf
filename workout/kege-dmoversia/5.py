for N in range(100):
    s = bin(N)[2:]

    if N % 2 == 0:
        s = "11" + s + "11"

    else:
        s = '1' + s + "00"

    if int(s, 2) > 95:
        print(N, int(s, 2))
        
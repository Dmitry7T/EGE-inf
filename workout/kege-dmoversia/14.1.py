
for x in "0123456789ABCDEFGHIJKL":
    if(int(f"27{x}98876", 22) + int(f"26{x}51", 22) + int(f"711{x}5", 22)) % 21 == 0:
       print(x, (int(f"27{x}98876", 22) + int(f"26{x}51", 22) + int(f"711{x}5", 22)) / 21)
       
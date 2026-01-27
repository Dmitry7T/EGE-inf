# Здесь собраны все шаблоны для задач №15
def f(x, y, A):
  return (x - 2*y < 3*A) or (2*y > x) or (3*x > 50)
for A in range(1, 1000):
  if all(f(x, y, A) for x in range(1, 1000) for y in range(1, 1000)):
    print(A)
    break

def f(x, A):
  return (x & 29 != 0) <= ((x & 17 == 0) <= (x & A != 0))
for A in range(1, 1000):
  if all(f(x, A) for x in range(1, 1000)):
    print(A)
    break

def F(x,A):
    P=list(range(20,101))
    Q=list(range(60,141))
    return ((x in A)<=(x in P)) or (x in Q)

A=list(range(1000))
for x in range(1000):
    if not(F(x,A)):
        A.remove(x)
print(A)
print((max(A)-min(A))//10)
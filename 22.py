for x in range(1, 100):
    a = 0
    b = 1
    i = x
    while i > 0:
        a = a + 1
        b = b * (i % 10)
        i = i // 10
    if a == 2 and b == 15:
        print(x)
        break

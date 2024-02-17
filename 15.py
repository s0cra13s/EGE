for a in range(100, 0, -1):
    k = 0
    for x in range(1000):
        if (x & a != 0) <= ((x & 17 == 0 and x & 5 == 0) <= (x & 3 != 0)):
            k += 1
    if k == 1000:
        print(a)
        break
def factorize(n):
    r = []
    k = 2
    while (k <= n):
        if n % k == 0:
            n = n // k
            if k not in r:
                r.append(k)
        else:
            k += 1

    return r


p = 670001
i = 0
while (i < 5):
    f = factorize(p)
    if sum(f) % 10 == 5:
        print(p, f, sum(f))
        i += 1
    p += 1
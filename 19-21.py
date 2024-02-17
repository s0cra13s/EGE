def f(s, c, m):
    if s >= 50:
        if s > 119:
            return c % 2 != m % 2
        return c % 2 == m % 2
    if c == m:
        return 0
    if c % 2 != m % 2:
        return f(s + 2, c + 1, m) or f(s * 3, c + 1, m)
    else:
        return f(s + 2, c + 1, m) and f(s * 3, c + 1, m)

for s in range(1, 50):
    for i in range(1, 30):
        if f(s, 0, i):
            if i == 4:
                print(s)
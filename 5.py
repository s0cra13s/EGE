n_sum = 0

for n in range(1,100):
    s = bin(n)[2:]
    s_str = str(s)
    for i in range(2):
        for j in range(0, len(s_str)):
            n_sum += int(s_str[j])
        s_str += str(n_sum % 2)
        n_sum = 0
    r = int(s_str, 2)
    if r > 60:
        print(r)
        break
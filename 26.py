f = open('26.txt')
S, N = f.readline().split()
S = int(S)
CONST_S = S

A_Sizes, B_Sizes = [], []
count = 1
a_count, b_count = 0, 0

for i in f:
    if 'A' in i:
        a, b = i.split()
        A_Sizes.append(int(a))
    elif 'B' in i:
        a, b = i.split()
        B_Sizes.append(int(a))

f.close()
A_Sizes.sort()
B_Sizes.sort()

for i in range(0, len(A_Sizes)):
    if S - A_Sizes[i] >= 0:
        S -= A_Sizes[i]
    else:
        count += 1
        S = CONST_S

S = CONST_S
print("Task 1 ", count)

for i in range(count):
    for j in range(a_count, len(A_Sizes)):
        if S - j >= 0:
            S -= j
            a_count += 1
        else:
            for x in range(b_count, len(B_Sizes)):
                if S - B_Sizes[x] >= 0:
                    S -= B_Sizes[x]
                    b_count += 1
                else:
                    S = CONST_S
                    break

print("Task 2", b_count)



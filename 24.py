f = open('24.txt')
a = f.read().strip()
max_local = 1
max_global = 0
last = ''
for i in a:
    if i >= last:
        max_local += 1
    else:
        max_global = max(max_global, max_local)
        max_local = 1
    last = i

print(max_global)

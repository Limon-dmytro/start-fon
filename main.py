a = [3, 4, 8]
b = [2, 4, 7]
c = []
for i in a:
    if i not in b:
        c.append(i)


for j in b:
    if j not in c:
        c.append(j)

print(c)

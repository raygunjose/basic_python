# 13-16 for, while, break, continue

for i in range(3):
    print(i)

count = 0
while count < 3:
    print(count)
    count += 1

for i in range(5):
    if i == 3:
        break
    print(i)

for i in range(5):
    if i == 2:
        continue
    print(i)

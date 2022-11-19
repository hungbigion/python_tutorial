l1 = [4, 1, 2, 3]
l2 = [0, 1, 2, 4]
common_s = set(l1) & set(l2)
for i in common_s:
    if i % 2 == 0:
        print(i)

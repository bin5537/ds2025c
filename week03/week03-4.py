def inters(l1, l2):
    s1 = set(l1)
    s2 = set(l2)
    # return sorted(list(s1.intersection((s2))))

    # return  sorted(list(s1 | s2))
    return  sorted(list(s1 & s2))
    # return  sorted(list(s1 - s2))

l1 = [45, 5, 22, 31, 7, 19]
l2 = [2, 1, 5, 22, 7, 38, 28, 13, 41, 19]

print("중복 값:", inters(l1, l2))

def super_sum2(A):
    list1 = []

    for i in A:
        if i % 2 == 0:
            list1.append(i / 2)
        else:
            list1.append(i * 2)

    total = sum(list1)
    return total

print super_sum2([2, 3])


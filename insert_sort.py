def insert_sort(a: list) -> list:
    """
    берем элемент сравниваем с предыдущим
    если меньше меняем местами и так двигаемся от текущего элемента к нулю
    потом берем следующий повторяем.
    сложность n2? у меня получается что сложность n!
    :param a:
    :return:
    """
    counter = 0
    for i in range(0, len(a)):
        for j in range(i, 0, -1):
            counter += 1
            if a[j] < a[j-1]:
                a[j], a[j-1] = a[j-1], a[j]
            else:
                break

            print(counter, a)
    return counter, a



mylist = [
    # [-3, 5, 0, -8, 1, 10, 7, 6, 9, 13]
    # [10, 9, 8, 7, 6, 5, 4, 3, 2, 1, 0],
    # [6, -1, 7, 6, 5, 4, 3, 2, 1, 0, 8],
    # [i for i in range(11)],
    [i for i in range(11, 0, -1)]

    ]
for each in mylist:
    print(insert_sort(each))







# mylist_sorted = list(reversed(sorted(mylist)))
# print(mylist_sorted)
# print(insert_sort(mylist))
# print(insert_sort(mylist_sorted))

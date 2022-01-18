a = [-8, 5, 0, -3, 1, 11, 10]
print('исходный')
print(a)
print('-'*100)
N = len(a)


def choice_sort(mylist):
    """
    берем первый
    ищем минимальный среди остальных
    если он меньше первого - меняем их местами
    берем второй
    ищем минимальный среди остальных...
    сложность n2
    :param mylist:
    :return:
    """
    for i in range(len(mylist) - 1):
        current_min = mylist[i]
        current_min_index = i
        for j in range(i+1, len(mylist)):
            if mylist[j] < current_min:
                current_min = mylist[j]
                current_min_index = j
        if current_min_index != i:
            a[i], a[current_min_index] = a[current_min_index], a[i]
    return mylist

print(choice_sort(a))

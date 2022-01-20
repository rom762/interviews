def choice_sort(mylist):
    """
    Сортировка выбором
    берем первый
    ищем минимальный среди остальных
    если он меньше первого - меняем их местами
    берем второй
    ищем минимальный среди остальных...
    сложность n2
    :param mylist:
    :return:
    """
    for i in range(len(mylist)):
        current_min_index = i
        for j in range(i+1, len(mylist)):
            if mylist[j] < mylist[current_min_index]:
                current_min_index = j
        if current_min_index != i:
            a[i], a[current_min_index] = a[current_min_index], a[i]
    return mylist


def choice_sort_v2(data):
    for i, e in enumerate(data):
        local_min = min(range(i, len(data)), key=data.__getitem__)
        data[i], data[local_min] = data[local_min], data[i]
    return data


a = [-3, 5, 0, -8, 1, 11, 10]
print(choice_sort(a))
print(choice_sort_v2(a))

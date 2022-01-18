# сортировка слиянием
# слияние отсортированных массивов в один
# [-8, 5, 0, -3, 1, 10]


def merge(a: list, b: list) -> list:
    i = j = 0
    c = []
    while i < len(a) and j < len(b):
        if a[i] <= b[j]:
            c.append(a[i])
            i += 1
        elif a[i] > b[j]:
            c.append(b[j])
            j += 1
    c += a[i:] + b[j:]
    return c


def merge_sort(a: list):
    if len(a) < 2:
        return a[:]
    m = len(a) // 2
    left, right = a[:m], a[m:]
    print(f'left: {left}')
    print(f'right: {right}')
    merge_sort(left)
    merge_sort(right)
    return merge(left, right)




# print(mylist)
# n = len(mylist) // 2
#
#
# print(n, mylist[n])
#
# a = mylist[:n]
# print(*a)
# b = mylist[n:]
# print(*b)
# print(merge(mylist[:n], mylist[n:]))


# def merge_sort(arr):
#     # Последнее разделение массива
#     if len(arr) <= 1:
#         return arr
#     mid = len(arr) // 2
#     # Выполняем merge_sort рекурсивно с двух сторон
#     left, right = merge_sort(arr[:mid]), merge_sort(arr[mid:])
#
#     # Объединяем стороны вместе
#     return merge(left, right, arr.copy())
#
#
# def merge(left, right, merged):
#     left_cursor, right_cursor = 0, 0
#     while left_cursor < len(left) and right_cursor < len(right):
#
#         # Сортируем каждый и помещаем в результат
#         if left[left_cursor] <= right[right_cursor]:
#             merged[left_cursor + right_cursor] = left[left_cursor]
#             left_cursor += 1
#         else:
#             merged[left_cursor + right_cursor] = right[right_cursor]
#             right_cursor += 1
#
#     for left_cursor in range(left_cursor, len(left)):
#         merged[left_cursor + right_cursor] = left[left_cursor]
#
#     for right_cursor in range(right_cursor, len(right)):
#         merged[left_cursor + right_cursor] = right[right_cursor]
#
#     return merged

mylist = [-8, 5, 0, -3, 1, 10]
mylist_system_sorted = sorted(mylist)
mylist_sorted_by_me = merge_sort(mylist)

# print(f'before {mylist}')
# print(f'my sort: {mylist_sorted_by_me}')
# print(f'system sort: {mylist_system_sorted}')
# print(f'is it equal: {mylist_sorted_by_me == mylist_system_sorted}')
print(merge([-8, -3, 0], [1, 5, 10]))

# Сортировка слиянием

def merge(a: list, b: list) -> list:
    """
    слияние уже отсортированных частей
    :param a:
    :param b:
    :return:
    """
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
    if len(a) <= 1:
        return a
    m = len(a) // 2
    left, right = a[:m], a[m:]
    return merge(merge_sort(left), merge_sort(right))


a = [-3, 5, 0, -8, 1, 10]
print(merge_sort(a))

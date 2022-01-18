def quick_sort(mylist):
    """
    берем любой элемент в качестве барьерного
    делим исходный список на ТРИ части
    меньше барьерного, равные ему, больше барьерного
    рекурсивно проходимся по 1 и 3 части
    крайний случай - когда пустой список или один элемент
    на выходе складываем все части
    хорошее объяснение
    https://www.youtube.com/watch?v=mCl1hBMFS8U&t=300s&ab_channel=egoroff_channel
    у хирьялова не очень (не использует плюшки питонячьи)
    :param mylist:
    :return:
    """
    if len(mylist) <= 1:
        return mylist
    base = mylist[0]
    left = list(filter(lambda x: x < base, mylist))
    center = [i for i in mylist if i == base]
    right = list(filter(lambda x: x > base, mylist))

    return quick_sort(left) + center + quick_sort(right)

mylist = [7, 6, 10, 5, 9, 8, 3, 4, 7]
print(quick_sort(mylist))

a = [-3, 5, 0, -8, 1, 10]

N = len(a)

for i in range(1, N):
    print(i)
    for j in range(i, 0, -1):
        print(f'____{j}')

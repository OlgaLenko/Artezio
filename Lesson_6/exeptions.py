T = int(input())
for i in range(T):
    line = input().split()
    a = line[0]
    b = line[1]
    try:
        print(int(a) // int(b))
    except ZeroDivisionError as e:
        print('Error Code:', e)
    except ValueError as e:
        print('Error Code:', e)

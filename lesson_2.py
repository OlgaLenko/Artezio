# ex. 1

def sq(a, x):
    res = []
    count = 0
    for i in range(0, x+1):
        if i % 2 != 0:
            res += [i**2]
            count += 1
            i += 1
    print(*res, 'всего чисел -', count)
sq(0, 9)
    
# ex. 2

def div_by_c(a, b, c):
    count = 0
    for i in range(a+1, b):
        if i % c == 0:
            count += 1
            i += 1
    print(count)
div_by_c(-11, 12, 4)

# ex. 3

def fact(a):
    result = 1
    for i in range(2, a+1):
        result *= i
        i += 1
    print(result)
fact(45)

# ex. 4

def old_range(a, b):
    range_list = []
    i = a
    while i < b:
        range_list += [i]
        i += 1
    print(range_list)
old_range(-8, 2)

# ex. 5

name_password = {
    'Vasyliy': '123456',
    '123ya': '123ya',
    'Angelina': 'porosenochek'
    }
    
name = input("Введите имя пользователя ")
password = input("Введите пароль ")

for key, value in name_password.items():
    if name_password[name] == password:
        print("Password for user:", name, "is correct")
        break
    else:
        print("Password for user:", name, "is incorrect")
        print("Please try again...")
        password = input("Введите пароль ")

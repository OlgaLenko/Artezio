# ex. 1

s = input()
if 0 < len(s) < 1000:
    full_name = s.split()
    name = full_name[0]
    surname = full_name[1]
    print(name.capitalize(), surname.capitalize())
    
# OR, for full name including more than two words:

s = input()
if 0 < len(s) < 1000:
    full_name = s.split()
    for i in full_name:
        print(i.capitalize(), end = ' ')

# ex. 2

string = input()
result = {}
for i in string:
    result[i] = string.count(i)
print(result)

# ex. 3

string = input()
if len(string) < 2:
    print('Empty String')
else:
    new_string = string[0:2] + string[-2:]
    print(new_string)


# ex. 4

list = input().split()
count = 0
for string in list:
    if len(string) >= 2 and string[0] == string[-1]:
        count += 1
    else:
        continue
print(count)

# ex. 5

set1 = set(input().split())
set2 = set(input().split())
set3 = set(input().split())
if set3.issubset(set1) and set3.issubset(set2):
    print("True")
else:
    print("False")

# ex. 6

n = int(input())
new_dict = {}
i = 1
while i <= n:
    new_dict[i] = i*i
    i += 1
print(new_dict)

# ex. 7

dict1 = {}
key1 = input()
while key1 != '':
    dict1[key1] = input()
    key1 = input()
    
dict2 = {}
key2 = input()
while key2 != '':
    dict2[key2] = input()
    key2 = input()

for key1, value1 in dict1.items():
    for key2, value2 in dict2.items():
        if key1 == key2:
            dict2[key2] = value1, value2
dict1.update(dict2)
print(dict1)

# dict1 = {'cat': 'Vaska', 'second_cat': 'Tishka'}
# dict2 = {'dog': 'Robert', 'hamster': 'Marfusha', 'cat': 'Murzik'}

# ex. 8

salary = {}
month = input()
while month != '':
    salary[month] = input()
    month = input()

salary = sorted(salary.values())
salary_i_like = salary[-1:-4:-1]
print(*salary_i_like)

# salary = {
#    'jan': 12020, 
#    'feb': 45000, 
#    'mar': 68000,
#    'apr': 15900,
#    'may': 28200,
#    'jun': 41000
#    }

# ex. 9

input_list = input().split()
new = set(input_list)

print(*new)

# OR
list = input().split()
list.sort()
list.append(0)
for i in range(len(list)-1):
    if list[i] == list[i+1]:
        i += 1
    else:
        print(list[i], end = ' ')
        i += 1
        
# ex. 10

list1 = input().split()
list2 = input().split()
difference = list(set(list1)^set(list2))
print(*difference)
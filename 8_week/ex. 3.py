def analog_enumirate(arr, start):
    for i in range(len(arr)):
        print(i + start, arr[i])


arr = ["Alex", "Bob", "Alice"]
start = 1
analog_enumirate(arr, start)


print('next analog')


def baz(value):
    return value*value


def analog_map(lst):
    for i in range(len(lst)):
        print(baz(lst[i]))


lst = [ 1, 2, 3, 4, 5]
analog_map(lst)

##########
print('next analog')
##########


def analog_zip(names, age, sex):
    min_len = min(len(names), len(age), len(sex))
    for i in range(min_len):
        print("name:", names[i],"age:", age[i], "sex:", sex[i])


names = ["Alex", "Bob", "Alice"]
age = [25, 17, 34]
sex = ["M", "M", "F"]
analog_zip(names, age, sex)

import re

a = input()  # Ввод: ABCagsfsfyagYABU
result = re.sub('[a-z]', '', a)
print(result)  # Вывод: ABCYABU


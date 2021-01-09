# Создание 1000 файлов
for i in range(1000):
    with open("./{}.txt".format(i), "w") as file:
        file.write("posdishuds\n")
        file.write("dfdfre\n")
        file.write("srgers\n")
    file.close()

with open("./упр1.txt", "r") as file:
    a, b = -1, -1
    for line in file:
        i = 0
        while " " in line[i]:
            i += 1
        a = i
        i = len(line) - 2
        while " " in line[i]:
            i -= 1
        b = i
        print(line[a:(b+1)])
file.close()
with open("./упр1.txt", "r") as file:
    a, b = -1, -1
    for strr in file:
        i = 0
        while " " in strr[i]:
            i += 1
        a = i
        i = len(strr) - 2
        while " " in strr[i]:
            i -= 1
        b = i
        print(strr[a:(b+1)])
file.close()
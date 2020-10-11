with open("./упр1.txt", "r") as file1, open("./упр2.txt", "w") as file2:
    file2.write(file1.read())
file1.close()
file2.close()
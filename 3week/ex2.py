import shutil
with open("./упр1.txt", "r") as file1, open("./упр2.txt", "w") as file2:
     shutil.copyfileobj(file1, file2)
file1.close()
file2.close()
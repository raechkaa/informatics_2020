import shutil
import os
a = []
b = input()
# shutil.unpack_archive(input())
for current_dir, dirs, files in os.walk("./main"):
    for line in files:
        if line[-1] == "y":
            if line[-2] == "p":
                if line[-3] == ".":
                    a.append(line)
b = sorted(a)
with open("./упр3.txt", "w") as file:
    file.write('\n'.join(b))
file.close()









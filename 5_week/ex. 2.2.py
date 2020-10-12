class Mother:

    def __str__(self):
        return "MOTHER"

class Daughter(Mother):

    def __str__(self):
        return "DAUGHTER"

a = Daughter()
print(a)
b = Mother()
print(b)

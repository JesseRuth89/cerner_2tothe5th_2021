# cerner_2tothe5th_2021
import random
c = ['b', 'c', 'd', 'f', 'g', 'h', 'j', 'k', 'r', 'q', 't']
v = ['e', 'i', 'o', 'u', 'a' , 'h']
a = c + v
def dog_name():
    name = []
    name_length = int(random.randrange(5, 11))
    for i in range(name_length):
        name += random.choice(c) if i == 0 else random.choice(a) if i == name_length -1 else random.choice(v)
    return ''.join(name).title()
print(f"Your dog's name is : {dog_name()}")



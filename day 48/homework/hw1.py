import random

def add_randoms():
    list = []
    for nums in range(50):
        A = random.randint(1, 50)
        list.append(A)
    print(list)

add_randoms()
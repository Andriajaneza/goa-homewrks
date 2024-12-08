# 5) შექმენით ფუნცია სადაც მომხარებელს შეეკითხებით 4 ჯერ თავის საყვარელი სახის ცხოველს ესენი მოათავსეთ  მასივში ანუ /სიაში/list და ამ სიაში რენოდუმალდ გამოიტანეთ ეს ელემენტები

import random 

A = input("first : ")
B = input("second : ")
C = input("third : ")
D = input("fourth : ")

list1 = [A,B,C,D]

A1 = random.choice(list1)
B1 = random.choice(list1)
C1 = random.choice(list1)
D1 = random.choice(list1)

list2 = [A1,B1,C1,D1]

print(list2)
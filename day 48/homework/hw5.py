import random

A = input("your first favorite sport : ") 
B = input("your second favorite sport : ") 
C = input("your third favorite sport : ") 

list = [A,B,C]

print("your favorite sport is " + random.choice(list))
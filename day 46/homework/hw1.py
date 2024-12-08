# 1) შექემენით ფუცნია სადაც იქენბა სია ცხვოლებეზე და random.choces() გამოყენებით დაამატეთ ახალ საიში რენდომ ცოხველები

import random

list1 = ['აქლემი','ცხენი','მგელი','კატა','ძაღლი','ტახი']
list2 = []

for i in range(3):
    choice = random.choice(list1)
    list2.append(choice)

print (list2)
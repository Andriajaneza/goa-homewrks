# 2) შექმმენით ფუცნია სადაც იქენბა სია თქვნს საყავრელ ფილმებზე და random.choces() გამოყენებით დაამტეთ 4 რემდონ ფილმი

import random

list1 = ['harry potter','fall','titanic']

RandomMovies = [
    "Inception", "The Matrix", 
    "Parasite", "The Dark Knight", 
    "Forrest Gump", "Interstellar",
    "The Godfather", "Pulp Fiction", 
    "The Shawshank Redemption", "Spirited Away"
]

for i in range(4):
    list1.append(random.choice(RandomMovies))

print (list1)
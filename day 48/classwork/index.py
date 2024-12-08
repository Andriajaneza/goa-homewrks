#start

import random # import of random for line(14)

list1 = ['harry potter','fall','titanic'] # list movies

RandomMovies = [
    "Inception", "The Matrix", 
    "Parasite", "The Dark Knight",  
    "Forrest Gump", "Interstellar",         # list of random movies
    "The Godfather", "Pulp Fiction",    
    "The Shawshank Redemption", "Spirited Away"
]

for i in range(4): # make it 4 times  
    A = random.choice(RandomMovies) # chosse random index from (RandomMovies)
    list1.append(A) # add it to (list1)
    RandomMovies.remove(A) # remove the taked index

print(list1) # print result

#end
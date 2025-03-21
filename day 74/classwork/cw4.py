def stone_throw(throwed):
    if throwed < 2:
        return ("ეის ვენტურა: ვაიმე პირდაპირ ფეხში მომხვდა!")
    if throwed > 2:
        return ("ეის ვენტურა: ვაიმე ორივე ფეხში მომხვდა!")
    
print(stone_throw(1))
print(stone_throw(2))
print(stone_throw(3))
print(stone_throw(4))
print(stone_throw(5))
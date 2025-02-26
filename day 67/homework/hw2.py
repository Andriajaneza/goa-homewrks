def points(games):
    total = 0
    
    for game in games:
        x = int(game[0])
        y = int(game[2])
        
        if x > y:
            total = total + 3
        elif x == y:
            total = total + 1
            
    return total

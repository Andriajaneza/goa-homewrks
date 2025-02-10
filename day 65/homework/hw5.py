def divisors(integer):
    divs = []
    
    for i in range(2, integer):
        if integer % i == 0:
            divs.append(i)
    
    if len(divs) == 0:
        return str(integer) + " is prime"
    
    return divs

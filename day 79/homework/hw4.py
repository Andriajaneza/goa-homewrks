def temperatura(temp):
    if temp == 30:
        return "ცხელა"
    if temp > 20 and temp < 30:
        return "თბილა"
    if temp > 10 and temp < 19:
        return "ცოტა ცივა"
    if temp < 10:
        return "ძალიან ცივა"

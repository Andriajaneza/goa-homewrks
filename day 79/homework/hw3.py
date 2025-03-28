def cars(time):
    if time < 1:
        return "უფასო"
    if time > 1 and time < 3:
        return "5 ლარი"
    if time > 3 and time < 6:
        return "10 ლარი"
    if time > 6:
        return "20 ლარი"

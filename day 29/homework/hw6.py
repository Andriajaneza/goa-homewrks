list = ["harry potter","fall","gods","titanic","xd"]

a = str(input("chosse 'add' , 'insert' or 'delete' something : "))

if a is "add":
    d = int(input("chosse your text : "))
    list.append(d)

if a is "insert":
    e = int(input("on wich index? : "))
    h = int(input("chosse your text : "))
    list.insert[e](h)

if a is "delete":
    f = int(input("on wich index? : "))
    list.delete(e)

A = (input("chosse password : "))

B = (input("write your password : "))

while A > B or A < B:
    B = (input("write your password : "))

if B == A:
    print("password is correct")
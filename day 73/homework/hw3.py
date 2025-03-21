def Remove_Highest():
    arr = []
    A = int(input())
    arr.append(A)
    B = int(input())
    arr.append(B)
    C = int(input())
    arr.append(C)
    D = int(input())
    arr.append(D)
    E = int(input())
    arr.append(E)
    
    arr.remove(max(arr))
    
    return arr

Remove_Highest()
def monkey_count(n):
    arr = []
    num = 1
    while num <= n:
        arr.append(num)
        num += 1
    return arr

monkey_count(20)
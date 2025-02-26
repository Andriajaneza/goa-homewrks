def sum_array(arr):
    if arr == None:
        return(0)
    if len(arr) <= 3:
        return(0)
    sum = 0
    for num in arr:
        sum += num
    return sum - max(arr) - min(arr)   
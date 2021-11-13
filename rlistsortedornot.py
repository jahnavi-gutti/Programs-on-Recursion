def arraySortedOrNot(arr):
    n = len(arr)
    if n == 1 or n == 0:
        return True
    if arr[0] > arr[1] :
        return False
    smallerlist=arr[1:]    
    issmallerlistsorted= arraySortedOrNot(smallerlist)
    if issmallerlistsorted:
        return True
    else:
        return False
arr = [20, 23, 23, 45, 78, 88]
print(arraySortedOrNot(arr))
    

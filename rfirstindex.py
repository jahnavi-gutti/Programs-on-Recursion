def firstindex(arr,x):
    n = len(arr)
    if  n == 0:
        return -1
    if arr[0] ==x :
        return 0
    smallerlist=arr[1:]    
    smallerlistotput= firstindex(smallerlist,x)
    if smallerlistotput==-1:
        return -1
    else:
        return smallerlistotput+1
arr = [1,2,4,5,7,8,9,7]
print(firstindex(arr,7))
    

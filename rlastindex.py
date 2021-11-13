def lastindex(arr,x):
    n = len(arr)
    if  n == 0:
        return -1
    smallerlist=arr[1:]    
    smallerlistotput= lastindex(smallerlist,x)
    if smallerlistotput!=-1:
        return smallerlistotput+1
    else:
        if arr[0]==x:
            return 0
        else:
            return 1
    
        
arr = [1,2,4,5,7,8,9,7]
print(lastindex(arr,7))
    

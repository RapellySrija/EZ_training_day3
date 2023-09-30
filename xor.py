#find out that which occurs once
#xor of all elements.. same elements will get cancelled
#i.e 5^5^3^2^2 repeated element gets cancelled and 3 remains
def findSingle(ar,n):
    res=ar[0]
    #do xor of all elements and return
    for i in range(1,n):
        res=res^ar[i]
    return res
ar=[2,3,5,4,5,3,4,2,88]
print(findSingle(ar,len(ar)))

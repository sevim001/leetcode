
def merge(array1,array2,m,n):
    for i in range(n):
        array1[m+i]=array2[i]
    array1.sort()
    return array1

array1= [1,2,3,0,0,0]
m=3
array2= [2,5,6]
n=3    
print(merge(array1,array2,m,n))
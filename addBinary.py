#Given two binary strings a and b, return their sum as a binary string.

def addBinary(a,b):
    a,b=a[::-1],b[::-1]
    solution=""
    carry=0
    for i in range(max(len(a),len(b))):
        A = int(a[i])-int("0") if i<len(a) else 0
        B = int(a[i])-int("0") if i<len(b) else 0
        total=A+B+carry
        char=str(total%2)
        solution=solution+char
        carry=total//2

    if carry:
       solution = "1" + solution
    return solution   

a="11"
b="1"
print(addBinary(a,b))
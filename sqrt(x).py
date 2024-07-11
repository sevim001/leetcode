#iven a non-negative integer x, return the square root of x rounded down to the nearest integer.
#  The returned integer should be non-negative as well.

def sqr(a):
   left=0
   right=a
   while left<=right:
      mid=(left+right)//2
      if mid*mid<a:
         left=mid+1
      elif mid*mid>a:
         right=mid-1
      else:
         return mid
      
   return right        
        
a=4  
print(sqr(a)) 

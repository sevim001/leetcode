""" def getConcatenation( nums):
        nums=nums+nums

        ans= nums
        
        return ans 
nums=[1,2,3]
print (getConcatenation(nums))  """

""" def getConcatenation( nums):
        n=len(nums)
        ans=[]
        for i in range(n):
            ans.append(nums[nums[i]])
            i+=1        
        return ans 
nums=[0,2,1,5,3,4]
print (getConcatenation(nums))
 """

""" def getConcatenation(nums):
    n = len(nums)
    ans = []
    
    for i in range(n):
        for j in range(i+1, n):
            if nums[i] == nums[j] and i < j:
                ans.append([i, j])
    
    return len(ans)

nums = [1, 2, 3, 1, 1, 3]
print(getConcatenation(nums)) """



""" def rearrangeArray(nums):
    positives = [num for num in nums if num > 0]
    negatives = [num for num in nums if num < 0]
    
    result = []
    
    pos_idx, neg_idx = 0, 0
    
    for i in range(len(nums)):
        if i % 2 == 0:
            result.append(positives[pos_idx])
            pos_idx += 1
        else:
            result.append(negatives[neg_idx])
            neg_idx += 1
            
    return result

nums = [3, 1, -2, -5, 2, -4]
print(rearrangeArray(nums)) """

#1324. Print Words Vertically
""" def printVertically(s):
    words = s.split(" ")
    max_len = max(len(word) for word in words)
    result=[]
    for i in range(max_len):
        ver_words=''
        for word in words:
            if i <len(word):
                ver_words+=word[i]
            else:
                ver_words += ' '
        result.append(ver_words.rstrip()) 
    return result """



#1701. Average Waiting Time
""" def averageWaitingTime(self, customers: List[List[int]]) -> float:
        finish_time = -maxsize
        total_wait_time = 0

        for time, duration in customers:
            if time < finish_time:
                total_wait_time += finish_time - time + duration
                finish_time += duration
            else:
                total_wait_time += duration
                finish_time = time + duration

        return total_wait_time / len(customers)

customers = [[1,2],[2,5]]
print(averageWaitingTime(customers)) """

""" def diagonalSum(mat):
    n=len(mat)
    sum1=[]
    sum2=[]
    for i in range(0,n):
        sum1.append(mat[i][i])
        i+=1
    for j in range(n,0):
        sum2.append(mat[j][j])
        j-=1
    return sum1,sum2    

mat = [[1,2,3],[4,5,6],[7,8,9]]
print(diagonalSum(mat))
 """


""" def tictactoe( moves):
    winner=''
    n=2
    A=[]
    B=[]
    for j in range(len(moves)):
        if j%2==0 or j==0:
            A.append(moves[j])
        else:
            B.append(moves[j])


    for i in range(3):
        if A == [0,i] or [i,0] or [i,i] or [i,1] or [i,n-i-1] or [2,i]:
            i+=1
            return "A"
        elif B == [0,i] or [i,0] or [i,i] or [i,1] or [i,n-i-1] or [2,i]: 
            i+=1
            return "B"
        else:
            "Draw"
    

moves = [[0,0],[1,1],[0,1],[0,2],[1,0],[2,0]]
print(tictactoe( moves)) """
""" def restoreString(s,indices):
    ans="" 
    for i in range(len(s)):
            b=indices.index(i)   
            ans+=s[b]
            i+=1
    return ans        


s = "codeleet"
indices = [4,5,6,7,0,2,1,3]  
print(restoreString(s,indices))   """

""" def luckyNumbers (self, matrix):
        minrow = {min(r) for r in matrix}
        maxcol = {max(c) for c in zip(*matrix)}
        return list(minrow & maxcol)
  
       

matrix = [[1,10,4,2],[9,3,8,7],[15,16,17,12]]
print(luckyNumbers (matrix))   """

""" def getNoZeroIntegers(n):
    a=[]
    a.append((n//2)-1)
    a.append(((n//2)-1)+((n%2)+2))
    return a

n =  2
print(getNoZeroIntegers(n)) """
def All_substrings(s):
    for i in range(len(s)):
            b=''
            if s[i] == s[:i]:
              b+=s[:i]       
    return b 
 
s = "abcabcbb" 
print(All_substrings(s))       

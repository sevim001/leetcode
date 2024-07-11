
def canJump(nums):
        ans=len(nums)-1
        for i in range(len(nums)):
            if range(0,nums[i])+range(0,nums[i+1]) == ans:
               return True
        return False
nums = [3,2,1,0,4]
print(canJump(nums))
    

def remove_duplicants(nums):
        i=1
        while i <len(nums):
                if nums[i] == nums[i-1]:
                   nums.remove(nums[i])
                else:
                      i+=1   
        return nums           
        
nums=[0,0,1,1,1,2,2,3,3,4]
print(remove_duplicants(nums))        
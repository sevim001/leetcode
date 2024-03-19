def remove_element(nums , value:int):
        i=0
        while i <len(nums):
                if nums[i] == value:
                   nums.remove(nums[i])
                else:
                      i+=1   
        return nums           
        
nums=[0,1,2,2,3,0,4,2]
value=2
print(remove_element(nums ,value))        
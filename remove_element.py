def remove_element(nums , value:int):
        i=0
        while i <len(nums):
                if nums[i] == value:
                   nums.remove(nums[i])
                else:
                      i+=1   
        return nums           
        
nums=[3,2,2,3]
value=3
print(remove_element(nums ,value))        
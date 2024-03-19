def searchInsert(nums , target):
        l = 0
        r = len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            if nums[mid] < target:
                l = mid + 1
            elif nums[mid] > target:
                r = mid - 1
            else:
                return mid
        return l   
    
        
nums=[1,3,5,6]
target=2
print(searchInsert(nums , target))        
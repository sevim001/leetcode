
def twoSum(self, nums: list[int], target: int) -> list[int]:
    hashMap={}
    n=len(nums)
    ##cheking existing values in hashmap and adding them into hashmap
    for i in range(n):
        diff= target-nums[i]
        if diff in hashMap:
            return[hashMap[diff],i]
        hashMap[nums[i]] = i 
    return []       
                
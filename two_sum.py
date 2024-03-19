def twosum(nums , target):
    for i in range (len(nums)):
        for j in range (i+1 , len(nums)):
            if nums[i] + nums[j] == target:
                return[i,j]

n = [3, 1, 1, 2]
t = 5
print(twosum(n, t))
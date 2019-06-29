def remove_adjacent(nums):
    i=0
    while True:
        if nums[i]==nums[i+1]:
            nums.remove(nums[i+1])
        if i<len(nums)-2:
            i=i+1    
        else:
            break   
    return nums

nums=[1, 2, 2, 2, 3, 3, 4, 4, 3]
print(remove_adjacent(nums))
        

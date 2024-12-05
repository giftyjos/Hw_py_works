def find_closest_to_zero(nums):
    closest = nums[0]
    for num in nums:
        
        if abs(num) < abs(closest) or (abs(num) == abs(closest) and num > closest):
            closest = num
    return closest


nums = [-4, -2, 1, 4, 8]
print(find_closest_to_zero(nums))



def sum_of_unique_elements(nums):
    from collections import Counter

    
    counts = Counter(nums)
    
  
    unique_sum = sum(num for num, count in counts.items() if count == 1)
    
    return unique_sum

nums = [1, 2, 3, 2]
print("The sum of unique elements is:", sum_of_unique_elements(nums))  


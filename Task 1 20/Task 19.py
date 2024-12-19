def max_sum_div_three(nums):
    sum_all = sum(nums)
    remainder1 = []
    remainder2 = []

    for num in nums:
        if num % 3 == 1:
            remainder1.append(num)
        elif num % 3 == 2:
            remainder2.append(num)

    remainder1.sort()
    remainder2.sort()

    if sum_all % 3 == 0:
        return sum_all
    elif sum_all % 3 == 1:
        if len(remainder1) >= 1 and len(remainder2) >= 2:
            return sum_all - min(remainder1[0], sum(remainder2[:2]))
        elif len(remainder1) >= 1:
            return sum_all - remainder1[0]
        elif len(remainder2) >= 2:
            return sum_all - sum(remainder2[:2])
    elif sum_all % 3 == 2:
        if len(remainder2) >= 1 and len(remainder1) >= 2:
            return sum_all - min(remainder2[0], sum(remainder1[:2]))
        elif len(remainder2) >= 1:
            return sum_all - remainder2[0]
        elif len(remainder1) >= 2:
            return sum_all - sum(remainder1[:2])

    return 0
nums = [3, 6, 5, 1, 8]
print("The maximum possible sum divisible by three is:", max_sum_div_three(nums))  


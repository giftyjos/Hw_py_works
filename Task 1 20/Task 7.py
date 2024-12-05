def summary_ranges(nums):
    if not nums:
        return []

    ranges = []
    start = nums[0]
    end = nums[0]

    for num in nums[1:]:
        if num == end + 1:
            end = num
        else:
            if start == end:
                ranges.append(f"{start}")
            else:
                ranges.append(f"{start}->{end}")
            start = num
            end = num

    if start == end:
        ranges.append(f"{start}")
    else:
        ranges.append(f"{start}->{end}")

    return ranges


nums = [0, 1, 2, 4, 5, 7]
print(summary_ranges(nums))  

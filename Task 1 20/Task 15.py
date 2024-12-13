def is_additive_number(num):
    def is_valid(start, length1, length2):
        num1 = num[start:start + length1]
        num2 = num[start + length1:start + length1 + length2]
        
        if (num1[0] == '0' and length1 > 1) or (num2[0] == '0' and length2 > 1):
            return False
        
        while start + length1 + length2 < len(num):
            num3 = str(int(num1) + int(num2))
            length3 = len(num3)
            if not num.startswith(num3, start + length1 + length2):
                return False
            start += length1
            num1, num2 = num2, num3
            length1, length2 = length2, length3
        return True

    n = len(num)
    for length1 in range(1, n // 2 + 1):
        for length2 in range(1, (n - length1) // 2 + 1):
            if is_valid(0, length1, length2):
                return True
    return False


input_number = "112358"
print(is_additive_number(input_number)) 

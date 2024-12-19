def balanced_string_split(s):
    count = 0
    balance = 0
    
    for char in s:
        if char == 'L':
            balance += 1
        elif char == 'R':
            balance -= 1
        
        if balance == 0:
            count += 1
    
    return count


s = "RLRRLLRLRL"
print("The maximum number of balanced substrings is:", balanced_string_split(s))


def roman_to_int(s):
    # Map of Roman numerals to their integer values
    roman_values = {
        'I': 1,
        'V': 5,
        'X': 10,
        'L': 50,
        'C': 100,
        'D': 500,
        'M': 1000
    }
    total = 0
    prev_value = 0
    
    # Iterate through the string in reverse
    for char in reversed(s):
        current_value = roman_values[char]
        if current_value < prev_value:
            total -= current_value
        else:
            total += current_value
        prev_value = current_value
    
    return total

# Example usage
roman_numeral = "III"
integer_value = roman_to_int(roman_numeral)
print(f"The integer value of {roman_numeral} is {integer_value}.")

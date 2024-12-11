def is_anagram(s, t):
    
    if len(s) != len(t):
        return False
    
    
    return sorted(s) == sorted(t)


s = "anagram"
t = "nagaram"
print(f"Is '{t}' an anagram of '{s}'", is_anagram(s, t))  
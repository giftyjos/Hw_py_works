def merge_strings(word1, word2):
    merged_string = []
    i = 0
    while i < len(word1) or i < len(word2):
        if i < len(word1):
            merged_string.append(word1[i])
        if i < len(word2):
            merged_string.append(word2[i])
        i += 1
    return ''.join(merged_string)


word1 = "abc"
word2 = "pqr"
print(merge_strings(word1, word2))  
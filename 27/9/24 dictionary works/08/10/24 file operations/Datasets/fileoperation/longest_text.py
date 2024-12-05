


file = open("C:\\Users\\HP\\Desktop\\Hw_py\\27\\9\\24 dictionary works\\08\\10\\24 file operations\\Datasets\\longest text.txt", mode="r", encoding="utf8")

file = file.read().split()
lenght = 0
Longest_word = ""
for word in file:
    if len(word) > lenght:
        lenght = len(word)
        Longest_word = word

print(Longest_word, lenght)
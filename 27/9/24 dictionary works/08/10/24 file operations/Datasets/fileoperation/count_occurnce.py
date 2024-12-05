with open("C:\\Users\\HP\\Desktop\\Hw_py\\27\\9\\24 dictionary works\\08\\10\\24 file operations\\Datasets\\count.txt",'r') as file:
    a_count = 0
    for words in file:
        for c in words:
            if c=='e':
                a_count+= 1


print("Number of appearance of word'e' in text file:",a_count)
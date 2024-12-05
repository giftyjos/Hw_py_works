# f=open("C:\\\\Users\\\\HP\\\\Desktop\\\\Hw_py\\\\27\\\\9\\\\24 dictionary works\\\\08\\\\10\\\\24 file operations\\\\Datasets\\\\read.txt")
# for line in f:
#      print(line)

f=open("C:\\Users\\HP\\Desktop\\Hw_py\\27\\9\\24 dictionary works\\08\\10\\24 file operations\\Datasets\\read.txt","r")

words=[]

for line in f:

    # line=this python txt is very simple


    all_words=line.split(" ")

    for w in all_words:

        words.append(w)

    word_count={w:words.count(w) for w in words}#words count print

nested_word_count=[{v,k} for k,v in word_count.items()]

# word-key count-value reverse word-value,count-key

print(sorted(nested_word_count,reverse=True))



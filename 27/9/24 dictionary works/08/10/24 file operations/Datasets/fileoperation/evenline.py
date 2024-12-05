f1=open("C:\\Users\\HP\\Desktop\\Hw_py\\27\\9\\24 dictionary works\\08\\10\\24 file operations\\\Datasets\\even line.txt","r")
f2=open("C:\\Users\\HP\\Desktop\\Hw_py\\27\\9\\24 dictionary works\\08\\10\\24 file operations\\Datasets\\even_line.txt","w")
content=f1.readlines()
print(content)

for i in range(len(content)):
  if(i%2==0):
      f1.read(content[i])
else:
      f2.write(content[i])

f1.close()
f2.close()

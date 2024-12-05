fdr = open("C:\\Users\\HP\\Desktop\\Hw_py\\27\\9\\24 dictionary works\\08\\10\\24 file operations\\Datasets\\input.txt","r")
fdw = open("C:\\Users\\HP\\Desktop\\Hw_py\\27\\9\\24 dictionary works\\08\\10\\24 file operations\\Datasets\\output.txt","w")

content= fdr.read()
content_reverse = content[::-1]
fdw.write(content_reverse)

fdr.close()
fdw.close()
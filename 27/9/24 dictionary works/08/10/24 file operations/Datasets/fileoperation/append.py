
f=open("C:\\Users\\HP\\Desktop\\Hw_py\\27\\9\\24 dictionary works\\08\\10\\24 file operations\\Datasets\\frame_works.txt","a")
# f.write("spring"+"\n")
frame_works=["workpress","springboot","oodo","fastapi"]
for fw in frame_works:
    f.write(fw+"\n")
f.close()
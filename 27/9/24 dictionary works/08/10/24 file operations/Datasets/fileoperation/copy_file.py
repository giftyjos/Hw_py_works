f1 = open("C:\\Users\\HP\\Desktop\\Hw_py\\27\\9\\24 dictionary works\\08\\10\\24 file operations\\Datasets\\fileoperation\\copy1.txt","r") 
  
# To open the second file in write mode 
f2 = open("C:\\Users\\HP\\Desktop\\Hw_py\\27\\9\\24 dictionary works\\08\\10\\24 file operations\\Datasets\\fileoperation\\copy2.txt","w") 
  
# For loop to traverse through the file 
for line in f1: 
  
    # Writing the content of the first 
    # file to the second file 
      
    # Using upper() function to 
    # capitalize the letters 
    f2.write(line.upper())
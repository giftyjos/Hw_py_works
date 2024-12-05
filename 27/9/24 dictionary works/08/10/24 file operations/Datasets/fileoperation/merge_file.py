import shutil 
from pathlib import Path 
   
firstfile = Path(r'C:\Users\HP\Desktop\Hw_py\27\9\24 dictionary works\08\10\24 file operations\Datasets\first_txt.txt') 
secondfile = Path(r'C:\Users\HP\Desktop\Hw_py\27\9\24 dictionary works\08\10\24 file operations\Datasets\second_txt.txt') 

newfile = input("Enter the name of the new file: ") 
print() 
print("The merged content of the 2 files will be in", newfile) 
  
with open(newfile, "wb") as wfd: 
  
    for f in [firstfile, secondfile]: 
        with open(f, "rb") as fd: 
            shutil.copyfileobj(fd, wfd, 1024 * 1024 * 10) 
  
print("\nThe content is merged successfully.!") 
print("Do you want to view it ? (y / n): ") 
  
check = input() 
if check == 'n': 
    exit() 
else: 
    print() 
    c = open(newfile, "r") 
    print(c.read()) 
    c.close()
import PyPDF2
import os
file=input()
result=0

nosaukumi=[]
filenames=os.listdir("rekini/")
skaits=len(filenames)
for i in range(0,skaits):
    filename= "rekini/" + filenames[i]
    nosaukumi.append(filename)
# print(nosaukumi)

if file not in nosaukumi:
    print(result)
    exit()
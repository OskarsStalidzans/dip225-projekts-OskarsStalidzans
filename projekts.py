import PyPDF2
import os

result=0

nosaukumi=[]
filenames=os.listdir("rekini/")
skaits=len(filenames)
for i in range(0,skaits):
    filename= "rekini/" + filenames[i]
    nosaukumi.append(filename)
print(nosaukumi)


for i in range(0, 2):
    row=[]
    pdf_file=PyPDF2.PdfReader(open(nosaukumi[i],"rb"))
    number_of_pages=len(pdf_file.pages)
    page1=pdf_file.pages[0]
    page2=pdf_file.pages[1]
    text1=page1.extract_text()
    text2=page2.extract_text()

    vieta1 = text1.find("A003438301")
    paterins = text1[vieta1+11:vieta1+16]
    paterins = paterins.replace(" ", "")
    row.append(paterins)
    print(row)
exit()
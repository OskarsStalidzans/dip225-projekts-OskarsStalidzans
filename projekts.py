import PyPDF2
import os

videjais_paterins=0

nosaukumi=[]
filenames=os.listdir("rekini/")
skaits=len(filenames)
for i in range(0,skaits):
    filename= "rekini/" + filenames[i]
    nosaukumi.append(filename)
    nosaukumi.sort()
# print(nosaukumi)

menesa_paterins=[]
for i in range(0,skaits):
    pdf_file=PyPDF2.PdfReader(open(nosaukumi[i],"rb"))
    number_of_pages=len(pdf_file.pages)
    page1=pdf_file.pages[0]
    page2=pdf_file.pages[1]
    text1=page1.extract_text()
    text2=page2.extract_text()    
    
    if i in range(0,skaits):
        if "INFORMĀCIJA PAR DABASGĀZES PATĒRIŅU" in text1:
            vieta1 = text1.find("  (A003438301")
            paterins = text1[vieta1+14:vieta1+18]
            paterins = paterins.replace(" ", "")
            menesa_paterins.append(int(paterins))
        else:
            vieta2 = text2.find("  (A003438301")
            paterins = text2[vieta2+14:vieta2+18]
            paterins = paterins.replace(" ", "")
            menesa_paterins.append(int(paterins))

videjais_paterins = (sum(menesa_paterins))/skaits
videjais_paterins = round(videjais_paterins)
print(videjais_paterins)

exit()
import PyPDF2
import os
import openpyxl
import selenium
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
import time
from openpyxl import Workbook, load_workbook 

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

service = Service()
option = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=service, options=option)

tarifu_nosaukumi = ['Elektrum', 'Elenger', 'Latvijas Gāze']
tarifi = []

url = "https://www.elektrum.lv/lv/majai/elektrum-dabasgaze/dabasgazes-produkti/piemerotaka-produkta-kalkulators/"
driver.get(url)
time.sleep(1)
button = driver.find_element(By.ID, "ccc-notify-accept")
button.click()
find = driver.find_element(By.ID, "consumption-cubic")
find.clear()
find.send_keys(videjais_paterins)
button = driver.find_element(By.CLASS_NAME, "has-loader")
button.click()
time.sleep(2)
find = driver.find_element(By.CLASS_NAME, "major")
major = find.text
find = driver.find_element(By.CLASS_NAME, "minor")
minor = find.text
the_number = major + "." + minor
the_number = float(the_number)
tarifi.append(the_number)

url = "https://elenger.lv/majai/dabasgaze/#dabasgazes-kalkulators"
driver.get(url)
time.sleep(1)
find = driver.find_element(By.ID, "monthly_consumption_m3")
find.clear()
find.send_keys(videjais_paterins)
time.sleep(1)
find = driver.find_element(By.ID, "flexible_total")
the_number = find.text
the_number = float(the_number)
tarifi.append(the_number)

url = "https://lg.lv/majoklim/produkti"
driver.get(url)
find = driver.find_element(By.CLASS_NAME, "form-control")
find.clear()
find.send_keys(videjais_paterins)
button = driver.find_element(By.CLASS_NAME, "btn--primary")
button.click()
time.sleep(1)
find = driver.find_element(By.CLASS_NAME, "calc-product-price")
the_number = find.text
the_number = the_number.replace(",", ".")
the_number = float(the_number)
tarifi.append(the_number)


print(tarifu_nosaukumi)
print(tarifi)

def create_workbook(path):
    workbook = Workbook()
    sheet = workbook.active
    for i in range (0, len(tarifu_nosaukumi)):
        sheet["A" + str(i+1)] = tarifu_nosaukumi[i]
    for i in range (0, len(tarifi)):
        sheet["B" + str(i+1)] = tarifi[i]
    workbook.save(path)

if __name__ == "__main__":
    create_workbook("elektribas_tarifu_piedavajumi.xlsx")

exit()
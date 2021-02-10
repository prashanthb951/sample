import re
import PyPDF2 as p
import pdfplumber
#"D:/ExcelProject/DQR-11-E-MAG05-EB05-ES-001-en-B-EQUIPMENT SPECIFICATION  Air Cooled Condenser (EB05)_GRA (" \
     #      "2).pdf"
path = "C:/Users/Athamas/Desktop/proj5/DQR-11-E-MAG05-EB05-ES-001-en-B-EQUIPMENT SPECIFICATION  Air Cooled Condenser (EB05)_GRA"
string = input("Enter Some Data:- ").upper()
with pdfplumber.open(path) as pdf:
    page3 = pdf.pages[3]
    text = page3.extract_text()
if re.findall(string ,text):
    print(string)
'''
Created on Aug 8, 2019

@author: baras
'''

import PyPDF2
import os

path = input("Enter path of PDF files.")
endName = input("Enter name of final file.")
endNameFile = path + "\\" + endName
finish = open(endNameFile,'wb')
writer = PyPDF2.PdfFileWriter()
for fileName in os.listdir(path):
    if fileName!=endName:
        pdf = open(path + "\\" + fileName, 'rb')
        read_pdf = PyPDF2.PdfFileReader(pdf, strict = False)
    #print(read_pdf.numPages)
        for pageNum in range(read_pdf.numPages):
            page = read_pdf.getPage(pageNum)
            writer.addPage(page)
    
        writer.write(finish)
        pdf.close()
#writer.write(finish)
finish.close()

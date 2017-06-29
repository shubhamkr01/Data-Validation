import csv
import xlrd

workbook = xlrd.open_workbook('filePath')
sheet=workbook.sheet_by_index(0)

urls=[]
amount=[]

for rownum in range(sheet.nrows):
	urls.append(sheet.cell_value(rownum,18))
	amount.append(sheet.cell_value(rownum,5))

  
with open('E:/Shubhams_Library/validating/schol_url.csv','w') as writefile: #creates csv file
	writer=csv.writer(writefile,delimiter="\n") #writes each list element into new column
	writer.writerow(urls)
  

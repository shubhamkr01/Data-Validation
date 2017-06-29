import csv
import xlrd

workbook = xlrd.open_workbook('filePath')
sheet=workbook.sheet_by_index(0)

urls=[]
amount=[]
name=[]

for rownum in range(sheet.nrows):
	urls.append(sheet.cell_value(rownum,18))
	amount.append(sheet.cell_value(rownum,5))
	name.append(sheet.cell_value(rownum,1))

# column names: redirect, invalid url, name mismatch, amount mismatch, amount found
  
with open('E:/Shubhams_Library/validating/schol_url.csv','w') as writefile: #creates csv file
	writer=csv.writer(writefile,delimiter="\n") #writes each list element into new column
	writer.writerow(urls)
  

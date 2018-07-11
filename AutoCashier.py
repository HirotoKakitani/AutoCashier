from openpyxl import *	#for manipulating excel spreadsheet
import Window as w

#from openpyxl import load_workbook
#from openpyxl import Workbook

# get index of first row with entry
def findFirstEntryIndex(ws):
	#iterate through names of employees
	index = 0
	for name in ws['A']:
		#skips empty rows
		if not name.value:
			continue
		cellValue = name.value.split(',')
		if len(cellValue) == 2 and cellValue.pop(0) != "NAME\nLast Name":
			return index+1
		index += 1
		
	print ("Beginning not Found")
	return -1
	
# get index of last row with entry
def findLastEntryIndex(ws, index):
	#cellValue = ws.rows[index].value.split(',')
	i = 0
	for name in ws['A']:
		if i < index:
			i+= 1
			continue
		else:
			i += 1
			if name.value == None or len(name.value.split(',')) != 2:
				break
		
	return i
	
def main():
	
	#sets up work sheet. 
	#TODO Need to go to correct worksheet depending on location
#	fileName = 'C:/Users/hikakitani/Desktop/test1.xlsx'
	fileName = 'C:/Users/hikakitani/Desktop/AutoCashierTestWorkbook.xlsx'
	inputWindow = w.Window()
	wb = load_workbook(fileName)
	inputValues = inputWindow.getUserInput()
	
	#print (wb.sheetnames)
	#create gui functionality for changing worksheets
	ws = wb.active

	#get the index range
	
	indexFirst = findFirstEntryIndex(ws)
	indexLast = findLastEntryIndex(ws, indexFirst)

	#get user input and place in inputValues


	
	for i in inputValues:
		print (i)

	for i in range(indexFirst,indexLast):
		#TODO 1. check if data can go between row i and i+1
		#	  2. if yes, move all rows down and insert
		#	  3. else move on
		pass
	
	#print ("testing")

if __name__ == "__main__":
	main()
	
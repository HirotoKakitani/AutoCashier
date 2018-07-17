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
#	fileName = 'test1.xlsx'
	fileName = 'AutoCashierTestWorkbook.xlsx'
	wb = load_workbook(fileName)
	ws = wb.active
	inputWindow = w.Window(wb.sheetnames)
	inputValues = inputWindow.getUserInput()
	
	#sets active worksheet to be the selected one
	ws = wb[inputWindow.location]
	#print(ws)
	#get the index range
	
	indexFirst = findFirstEntryIndex(ws)
	indexLast = findLastEntryIndex(ws, indexFirst)

	#get user input and place in inputValues
	for i in inputValues:
		print (i[0])
	print (inputWindow.location)
	#ws.insert_rows(2, 1)
	print ("######################\n")
	# names that come first alphabetically are considered smaller
	for inputVal in inputValues:
		for i in range(indexFirst+2,indexLast):
			currentCell = ws.cell(row=i,column=1).value	#gets name of current row
			prevCell = ws.cell(row=i-1, column=1).value #gets name of previous row
			print (currentCell)
			print (prevCell)

			#check

			#TODO need to fix if insertion happens at the very beginning 
			if (i == indexFirst and inputVal[0] < currentCell):
				print ("first insertion")
				print (currentCell)
				break
				
			#TODO need to find cause of mailto issue. 
			if (inputVal[0] < currentCell and inputVal[0] > prevCell):
				print ("\n	inserting between here!")
				ws.insert_rows(i,1) 						#insert blank row
				ws.cell(row=i,column=1).value = inputVal[0]	#just write name column for now 
				indexLast += 1
				break
			
			print ()
	wb.save(fileName)
	#print ("testing")

if __name__ == "__main__":
	main()
	
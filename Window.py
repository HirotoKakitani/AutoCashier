import tkinter as tk	#for gui inputs

#root = tk.Tk()
#e1 = tk.Entry(root)
#entryList = []
#e2 = tk.Entry(root)

class Window:
	def __init__(self):
		self.root = tk.Tk()
		self.e1 = tk.Entry(self.root)
		self.entryList = []
		self.enterButton = tk.Button(self.root, text='Enter', command = self.enterCommand)
		self.confirmButton = None
		self.inputEntryList = []
		
	#get user input and place in list of tuples.
	def getUserInput(self):
		#entries will be ["name",id#,EID, "email","remove/notremove", "location", "existing/new"]

		tk.Label(self.root, text="Entries").grid(row=0)

		self.e1.grid(row=0, column=1, pady=10)
		#tk.Button(self.root, text='Enter', command = self.buttonCommand).grid(row=3, column=1)#, sticky=W, pady=4)
		self.enterButton.grid(row=3, column=1)#, sticky=W, pady=4)
		self.root.mainloop()
	
	
		return self.entryList
		#tk.Button(root,text = ent
		#TODO get user input as tuple form. place in returnList. 
	
	
	def getEntries(self):
		#get the raw string of input

		input = self.e1.get().split('\n')
		#print (input)
		#print (len(input))
	
		newEntry = []
		for i in input:
			if i == '':
				continue
			j = i.split('\t')
			newEntry = (j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7])
			self.entryList.append(newEntry)
	
		#clean up entryList
		for j in self.entryList:
			if j == ('','','','','','','',''):
				self.entryList.remove(j)
	
	
	
	#displays all read entries and allows user to make any changes if needed
	def confirmEntries(self):

		r = 1
		for i in self.entryList:
			for j in range(1,9):
				e2 = tk.Entry(self.root)
				self.inputEntryList.append(e2)	#---------------------------------------------
				
				#TODO need some padding on the right side of the frame.  
				if j==8:
					e2.grid(row=r, column = j, padx=(0,50))
				else:
					e2.grid(row=r, column = j)
				e2.insert(0, i[j-1])
				
			numLabel = tk.StringVar()
			numLabel.set(r)
			tk.Label(self.root, textvariable = numLabel).grid(row = r, column = 0)
			
			r +=1

		#using lambda function to pass argument to callback
		self.confirmButton = tk.Button(self.root, text = 'Confirm', command =self.confirmCommand)
		self.confirmButton.grid(row=r,column=4,pady=(20,10))
		#TODO TODO need to split up entries so each entry defaults to corresponding value in entryList
		#also need to implement scrollbar in case of many entries
	
	
	def confirmCommand(self):
		values = [entry.get() for entry in self.inputEntryList]
		numEntries = 0
		print ("length of entryList = ", len(self.entryList))
		
		#TODO TODO fix updating any changes to entryList
		for v in range(0,len(values)): 
			if v % 7 == 0 and v != 0:
				print (numEntries)
				tempE = (values[v-7],values[v-6],values[v-5],values[v-4],values[v-3],values[v-2],values[v-1],values[v])
				print (tempE)
				numEntries += 1
				self.entryList[numEntries-1] = tempE


		
		self.root.quit()
	
	#generic function to execute 3 funtions sequentially
	def enterCommand(self):
		self.enterButton.destroy()
		self.getEntries()
		self.confirmEntries()
		#root.quit()
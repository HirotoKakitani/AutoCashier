import tkinter as tk	#for gui inputs

class Window:
	def __init__(self, sheetNames):
		self.root = tk.Tk()
		self.e1 = tk.Entry(self.root)
		self.eLabel = tk.Label(self.root, text="Entries")
		self.entryList = []
		self.enterButton = tk.Button(self.root,	text='Enter', command = self.enterCommand)
		self.v = tk.StringVar(self.root)		#default value in drop down menu
		self.v.set("Location")					#set default value
		self.dropDown = tk.OptionMenu(self.root, self.v, *sheetNames, command=self.listSelect)	#populates dropdown menu with list items
		self.confirmButton = None
		self.inputEntryList = []
		self.location = None
		#Format window
		self.e1.grid(row=0, column=1, pady=10)
		self.eLabel.grid(row=0)
		self.enterButton.grid(row=3, column=1)
		self.dropDown.grid(row=0,column=2)
		
	#get user input and place in list of tuples.
	def getUserInput(self):
		#entries will be ["name",id#,EID, "email","remove/notremove", "location", "existing/new"]
		self.root.mainloop()
		return self.entryList
	
	
	def getEntries(self):
		#get the raw string of input

		input = self.e1.get().split('\n')
	
		newEntry = []
		for i in input:
			if i == '':
				continue
			j = i.split('\t')
			newEntry = (j[0],j[1],j[2],j[3],j[4],j[5],j[6],j[7])
			self.entryList.append(newEntry)
	
		#clean up entryListW
		self.entryList = [entry for entry in self.entryList if entry != ('','','','','','','','')]
		
		
	#displays all read entries and allows user to make any changes if needed
	def confirmEntries(self):
		r = 1
		for i in self.entryList:
			for j in range(1,9):
				e2 = tk.Entry(self.root)
				self.inputEntryList.append(e2)	
				
				if j==8:
					e2.grid(row=r, column = j, padx=(0,50))
				else:
					e2.grid(row=r, column = j)
				e2.insert(0, i[j-1])
				
			numLabel = tk.StringVar()
			numLabel.set(r)
			tk.Label(self.root, textvariable = numLabel).grid(row = r, column = 0)
			
			r +=1

		self.confirmButton = tk.Button(self.root, text = 'Confirm', command =self.confirmCommand)
		self.confirmButton.grid(row=r,column=4,pady=(20,10))
		
	
	#TODO TODO also need to implement scrollbar in case of many entries
	def confirmCommand(self):	
		values = [entry.get() for entry in self.inputEntryList]
		numEntries = 0
		vCounter = 0
		eCounter = 0
		for v in values: 
			if vCounter == 7:
				vCounter = 0
				tempE = (values[0],values[1],values[2],values[3],values[4], values[5], values[6], values[7])
				self.entryList[eCounter] = tempE
				values = values[8:]
				eCounter += 1
				continue
			
			vCounter += 1
			
		#clean up entryList
		self.entryList = [entry for entry in self.entryList if entry != ('','','','','','','','')]
		
		self.root.quit()
	
	
	#generic function to execute 3 funtions sequentially
	def enterCommand(self):
		if self.location == None:
			print ("Please select a location")
			return
			
		self.enterButton.destroy()
		self.getEntries()
		self.confirmEntries()
	
	
	#callback when a location is set
	def listSelect(self, location):
		self.location = location
		print (location)
		
	
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
		self.enterButton = tk.Button(self.root, text='Enter', command = self.buttonCommand)
		self.confirmButton = None
		
	#get user input and place in list of tuples.
	def getUserInput(self):
		#entries will be ["name",id#,EID, "email","remove/notremove", "location", "existing/new"]

		tk.Label(self.root, text="Entries").grid(row=0)

		self.e1.grid(row=0, column=1)
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
	
	
	
	#TODO displays all read entries and allows user to make any changes if needed
	def confirmEntries(self):

		r = 1
		for i in self.entryList:
			tk.Entry(self.root).grid(row=r, column = 1)
			r +=1 

		self.confirmButton = tk.Button(self.root, text = 'Confirm', command = self.root.quit)
		self.confirmButton.grid(row=r,column=1)
		#TODO TODO need to split up entries so each entry defaults to corresponding value in entryList
		#also need to implement scrollbar in case of many entries
	
	#generic function to execute 3 funtions sequentially
	def buttonCommand(self):
		self.enterButton.destroy()
		self.getEntries()
		self.confirmEntries()
		#root.quit()
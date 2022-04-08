output = []
var = []

print("1ux (CP Framework) Version 0.0.2")

def clearattribute():
	attribute = "NaN"

def cleartype():
	cmd = "NaN"

def clearvar():
	searchvar = "NaN"
	setvarname = ""
	setvarvalue = ""

class parsing():
	#initiate
	def __init__ (self, type, value):
		self.type = type
		self.value = value
	
	#gets type of command
	def gettype(self):
		cleartype()
		cmd = input("cmd: ")
		self.type = cmd
	#gets attribute of attribute
	def getattribute(self):
		clearattribute()
		attribute = input("attribute: ")
		self.value = attribute
	
	def sorttype(self):
		#basically print in python
		if self.type == "log":
			output.append(self.value)
		#variable system
		if self.type == "var":
			#splits the attribute by 1 underscore
			clearvar()
			searchvar = self.value
			setvarname, setvarvalue = searchvar.split('_')
			var.append([setvarname,setvarvalue])
		#exits the coding interface
		if self.type == "exit":
			global coding
			coding = False
	

coding = True

while coding:
	lines = parsing("NaN", "NaN")
	lines.gettype()
	if coding == True:
		lines.getattribute()
	lines.sorttype()


for n in range (len(output)):
	print(str(output[n]))

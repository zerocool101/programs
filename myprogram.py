#import libreries
import pickle

def message(self):
	print("""*****MyNotes*****

	MENU

	1[+] Add a new note
	2[+] Read one note existing

		""")
	self.choose = int(input("Select one option > "))

class myapp:
	def __init__(self, tittle, note, choose):
		self.tittle = tittle
		self.note = note
		self.choose = choose

	def add(self):
		message(self)
		while self.choose != 1 and self.choose != 2:
			message(self)
			self.choose = int(input("Select one option > "))
		else:
			if self.choose == 1:
				self.tittle = input("\nTittle > ")
				self.note = input("Note > ")
				#ask for save
				save = input("\nDo you want to save this note? Y/N: ")
				if save == "y" or save == "Y":
					#save files
					file = open(str(self.tittle)+".pickl", "wb")
					pickle.dump(self.tittle, file)
					file.close()
				elif save == "n" or save == "N":
					return "\n¡¡¡ATENTION!!! > Your object called {0}.pickl was descarted.".format(self.tittle)

	def read(self):
		try:
			if self.choose == 2:
				name = input("File's name > ")
				#read files
				file2 = open(name+".pickl", "rb")
				todo = pickle.load(file2)
				return todo
				file.close()
		except FileNotFoundError:
			return "[Errno 2] No such file or directory: '{0}.pickl'".format(name)

obj = myapp("", "", "")
print(obj.add())
print(obj.read())


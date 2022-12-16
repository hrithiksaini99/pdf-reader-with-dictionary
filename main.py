import os
from tkinter import * 
from tkdocviewer import *
from tkinter import filedialog 
from PyDictionary import PyDictionary
dic = PyDictionary()

def create():
	os.system('python test.py') 
def browseFiles(): 
	filename = filedialog.askopenfilename(
		         initialdir = "D:/", 
									title = "Select a File", 
										filetypes = (("Pdf files", 
													"*.pdf*"), 
													("all files", 
														"*.*"))) 
	viewer.display_file(filename)

	
	label_file_explorer.configure(text="File Opened: "+filename) 

def f_meaning():
	word=entr.get()
	output.delete(0.0,END)
	
	try:
		mean=dic.meaning(word,disable_errors=True)
		output.insert(0.0,mean)
	except:
		output.insert(0.0,'Sorry No word found')

	
window = Tk()  
window.title('PDF Reader')  
window.geometry("1320x1200")  
window.config(background = "#3AC5BF") 

label_file_explorer = Label(window, 
							text = "Open pdf file", 
							width = 50, height = 4, 
							fg = "blue") 

viewer = DocViewer(window,width=800,height=900)

	
button_explore = Button(window, 
						text = "Browse Files", 
						command = browseFiles) 


button_exit = Button(window, 
					text = "Exit", 
					command = exit)

button_create = Button(window, 
					text = "Create new", 
					command = create)

button_meaning = Button(window, 
					text = "Meaning",
					command = f_meaning)
label_dic = Label(window,
							 text = "Dictionary",
								width = 50, height = 4, 
								fg = "blue") 	

entr=Entry(window,font=("times",15))
output=Text(window,width=25,height=8,font=('Arial'))

label_file_explorer.grid(column = 1, row = 1) 
button_explore.grid(column = 1, row = 2) 
button_exit.grid(column = 1,row = 3) 
label_dic.grid(column = 2, row = 1)
button_meaning.grid(column=2,row=3)
entr.grid(column=2,row=2)
button_create.grid(column =1, row =4)
output.grid(column=2,row=5)
viewer.grid(column=1,row=5)
window.mainloop() 

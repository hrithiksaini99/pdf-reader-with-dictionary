from tkinter import *
from tkinter import filedialog,simpledialog
from tkinter.scrolledtext import ScrolledText
from tkinter  import messagebox
from tkinter.ttk import *
import re
from fpdf import FPDF
import easygui

root = Tk()
root.title('Create new pdf')
textPad = ScrolledText(root, width=100, height=50)
filename = ''
def newFile():
    global filename
    if len(textPad.get('1.0',END+'-1c'))>0:
        if messagebox.askyesno("SAVE","Do you want to save?"):
            saveFile()
        else:
            textPad.delete(0.0,END)
    root.title("Create new pdf")

def saveFile():
   
    f = easygui.enterbox("Name of the file:")
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15) 

    if f!= None:
        data = textPad.get('1.0',END)

    try:
        pdf.cell(200, 10, txt = data,  ln = 1, align = 'C') 
        pdf.output(f+".pdf")
       

    except:
        messagebox.showerror(title="Oops!!",message="Unable to save file!")
     


def openFile():
    f = filedialog.askopenfile(parent=root,mode='r')
    t = f.read()
    textPad.delete(0.0,END)
    textPad.insert(0.0,t)
    



def exit_command():
    if messagebox.askyesno("Exit","Are you sure you want to exit?"):
        root.destroy()
    

menuM = Menu(root)
root.configure(menu=menuM)

fileM = Menu(menuM)
menuM.add_cascade(label='File',menu=fileM)
fileM.add_command(label='New',command=newFile)
fileM.add_command(label='Open',command=openFile)
fileM.add_command(label='Save',command=saveFile)
fileM.add_separator()
fileM.add_command(label='Exit',command=exit_command)

editM = Menu(menuM)
menuM.add_cascade(label='Edit',menu=editM)
editM.add_command(label='Undo')
editM.add_command(label='Redo')
editM.add_command(label='Cut')
editM.add_command(label='Copy')
editM.add_command(label='Paste')
textPad.pack()
root.mainloop()




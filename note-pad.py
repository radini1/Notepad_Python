from tkinter.filedialog import * 
from tkinter import *

x = Tk()
x.geometry('400x500')
x.title('NotePad')
x.config(bg='white')

def savefile():
    new_file = asksaveasfile(mode = 'w', filetypes= [('text files', '.txt')])
    if new_file is None:
        return 
    text = str(entry.get(1.0, END))   # getting all words and sentences
    new_file.write(text)   # put the text in new_file
    new_file.close()
    
def openfile():
    file = askopenfile(mode= 'r', filetypes=[('text files', '*.txt')])
    if file is not None:
        content = file.read()
    entry.insert(INSERT, content)
    
def clear():
    entry.delete(1.0, END)  # delete all the text

top = Frame(x)
top.pack(padx=10, pady=5, anchor='nw')

btn = Button(x, text="Open file", bg='white', command=openfile)
btn.pack(side=LEFT, in_=top)

btn2 = Button(x, text="Save", bg='white', command=savefile)
btn2.pack(side=LEFT, in_=top)

btn3 = Button(x, text="Clear", bg='white', command=clear)
btn3.pack(side=LEFT, in_=top)

btn4 = Button(x, text="Exit", bg='white', command=exit)   
btn4.pack(side=LEFT, in_=top)

entry = Text(x,wrap=WORD, bg='#ADD8E6', font=('poppins', 15))
entry.pack(padx=10, pady=5)

x.mainloop()
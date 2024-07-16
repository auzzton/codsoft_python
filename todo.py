# Importing tkinter
from tkinter import *
from tkinter.font import Font

root = Tk()
root.title('ToDo List')
root.iconbitmap('d:/Auston/Pycharm Projects')
root.geometry("500x500")

# Font
my_font = Font(
	family="courier",
	size=20,
	weight="normal")

# frame
my_frame = Frame(root)
my_frame.pack(pady=10)

# listbox
my_list = Listbox(my_frame,
	font=("Courier", 20, "italic"),
	width=25,
	height=5,
	bg="SystemButtonFace",
	bd=0,
	fg="#000000",
	highlightthickness=0,
	selectbackground="#838B8B",
	activestyle="none")

my_list.pack(side=LEFT, fill=BOTH)

# Creating scrollbar
my_scrollbar = Scrollbar(my_frame)
my_scrollbar.pack(side=RIGHT, fill=BOTH)

# Adding scrollbar
my_list.config(yscrollcommand=my_scrollbar.set)
my_scrollbar.config(command=my_list.yview)

# adding to the list
my_entry = Entry(root, font=("Helvetica", 24))
my_entry.pack(pady=20)

# Create a button frame
button_frame = Frame(root)
button_frame.pack(pady=20)

# Functions to add and delete
def delete_item():
	my_list.delete(ANCHOR)

def add_item():
	my_list.insert(END, my_entry.get())
	my_entry.delete(0, END)


# buttons
delete_button = Button(button_frame, text="Delete Item", command=delete_item, bg='red')
add_button = Button(button_frame, text="Add Item", command=add_item, bg='green')

delete_button.grid(row=0, column=0)
add_button.grid(row=0, column=1, padx=20)

root.mainloop()
# load a Tkinter listbox with data lines from a file,
# sort data lines, select a data line, display the data line,
# edit the data line, update listbox with the edited data line
# add/delete a data line, save the updated listbox to a data file
# used a more modern import to give Tkinter items a namespace
# tested with Python24       vegaseat       16nov2006
   
import tkinter as tk  # gives tk namespace


def get_list(event):
    """
    function to read the listbox selection
    and put the result in an entry widget
    """
    # get selected line index
    index = listbox1.curselection()[0]
    # get the line's text
    seltext = listbox1.get(index)
    # delete previous text in enter1
    enter1.delete(0, 50)
    # now display the selected text
    enter1.insert(0, seltext)

def set_list(event):
    """
    insert an edited line from the entry widget
    back into the listbox
    """
    try:
        index = listbox1.curselection()[0]
        # delete old listbox line
        listbox1.delete(index)
    except IndexError:
        index = tk.END
    # insert edited item back into listbox1 at index
    listbox1.insert(index, enter1.get())

def printer(event):
    print("Alccolselect=",listbox1.get(listbox1.curselection()))
     
# create the sample data file
str1 = """HTTP
FTP
MAIL
"""
fout = open("chem_data.txt", "w")
fout.write(str1)
fout.close()
   
# read the data file into a list
fin = open("chem_data.txt", "r")
chem_list = fin.readlines()
fin.close()
# strip the trailing newline char
chem_list = [chem.rstrip() for chem in chem_list]
   
root = tk.Tk()
root.title("Listbox Operations")
# create the listbox (note that size is in characters)
listbox1 = tk.Listbox(root, width=10, height=3)
listbox1.grid(row=0, column=0)

# use entry widget to display/edit selection
enter1 = tk.Entry(root, width=20, bg='white')
enter1.insert(0, 'Choisissez un flux')
enter1.grid(row=0, column=1)
# pressing the return key will update edited line
enter1.bind('<Return>', set_list)
# or double click left mouse button to update line
enter1.bind('<Double-1>', set_list)

# load the listbox with data
for item in chem_list:
    listbox1.insert(tk.END, item)
   
# left mouse click on a list item to display selection
listbox1.bind('<ButtonRelease-1>', get_list)
   
root.mainloop()
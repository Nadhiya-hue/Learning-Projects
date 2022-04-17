"""Python Tkinter.filedialog--offer a Set of Dialogs that you can use when working with files."""
from tkinter.filedialog import*
from tkinter import*
"""The Shutil Provides several Funtions to deal with operations on files and their collections Similiar to OS."""
import shutil

def zip():
    source_dir = askdirectory()
    print(source_dir)
    dest_dir = source_dir
    print("Start Zip")
    shutil.make_archive(dest_dir, 'zip' ,source_dir)
    print("Done Zip")
    
def unzip():
    source_dir = askopenfilename()
    print(source_dir)
    print("Start Unzip")
    dest_dir = source_dir.replace('.zip',' ')
    #print(source_dir)
    #print(dest_dir)
    shutil.unpack_archive(source_dir,dest_dir,'zip')
    print("Done UnZip")
    
#zip()
#unzip()

window = Tk()
window.geometry("300x200")
lbl = Label(window, text="Chain Zip & Unzip" , fg="red",font=("Helvetica"))
lbl.place(x=50, y=20)
btn = Button(window, text="Zip Your Folder",fg = "blue",command =zip)
btn.place(x=80, y=60)
btn = Button(window, text="UnZip Your Folder",fg = "green",command = unzip)
btn.place(x=80, y=100)
window.mainloop()



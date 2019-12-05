from tkinter import *
from tkinter import filedialog
from tkinter import messagebox
import os

# ======================== SETTINGS =====================
root = Tk()
root.title("Directory Digger ver. 1.2.1")
color1 = 'gray77'
color2 = 'gray60'
font1 = 'consolas', 11
root.geometry('800x500')
root.configure(bg=color1)
root.resizable(width=True,height=True)

# ======================== FRAMES =======================
top = Frame(root,width=600,height=50,bg=color2)
top.pack()
top2 = Frame(root,width=600, height=50, bg=color2)
top2.pack()
top3 = Frame(root,width=600, height=50, bg=color1)
top3.pack()
# ======================== VARIABLES ====================
folder_path = StringVar()
file_name = StringVar()

# ======================== FUNCTIONS ====================
def browse():
   folder_selected = filedialog.askdirectory()
   folder_path.set(folder_selected)

def run():
   for root, dirs, files in os.walk(folder_path.get()):
      level = root.replace(folder_path.get(), '').count(os.sep)
      indent = ' ' * 4 * (level)
      subindent = ' ' * 4 * (level + 1)
      indent2 = ' ' * 4 * (level)
      subindent = indent2 + '|' + ('-' * 4 * (level))
      result.insert(END, '{}{}\n'.format(indent,root).upper())
      result.insert(END, '{}{}\n'.format(subindent,files))
      result.insert(END, '{}{}\n'.format(indent,dirs).upper())
      result.insert(END, '{}\n'.format(indent2))

def seek():
   if file_name.get() == '':
      return result.insert(END, 'No file name given')
   else:
      for root, dirs, files in os.walk(folder_path.get()):
         for file in files:
            if file_name.get() in file:
                found = os.path.join(root,file)
                result.insert(END, '\n{}'.format(found))


def save():
   filename = filedialog.asksaveasfilename(defaultextension=".json",
      filetypes=[('JSON file','.json'),('text file','.txt'), ('all files','.*')])
   if filename is None:
      return
   else:
      with open(filename,"wt",encoding='utf-8') as filesave:
         text2save = str(result.get(1.0,END))
         filesave.write(text2save)
         filesave.close()
         messagebox.showinfo('SAVED', 'File has been saved successfully!')

def clear():
    result.delete("1.0",END)
   #  dir_path.delete(0,END)
   #  file_name.delete(0,END)

def about():
   messagebox.showinfo('About','''Created by @kostyrko (GitHub) to map directory
   \n (use under under the GPLv3 license) ''')

def close():
   result = messagebox.askquestion('Directory Digger', 'Are you sure you want to exit?', icon='warning')
   if result == 'yes':
      root.destroy()
      exit()
   
# ======================== ENTRY, BUTTONS & LABELS==================
browsebt = Button(top,text="Browse",bg='dark red',fg= 'white',command=browse)
browsebt.pack(side=LEFT,padx=5,pady=5)

dir_path = Entry(top,font=font1,width=500,bd=4,textvariable=folder_path)
dir_path.pack(side=LEFT,padx=5,pady=5)

txt_file_entry = Label(top2,text="File Name: ",font=font1)
txt_file_entry.pack(side=LEFT,padx=5,pady=5)

file_entry = Entry(top2,font=font1,width=500,bd=4,textvariable=file_name)
file_entry.pack(side=LEFT,padx=5,pady=5)

runbt = Button(top3,text="Stratify Directory",command=run)
runbt.pack(side=LEFT,padx=5,pady=5)

runbt = Button(top3,width=10, text="Seek File",command=seek)
runbt.pack(side=LEFT,padx=5,pady=5)

savebt = Button(top3,text="Save result",command=save)
savebt.pack(side=LEFT,padx=5,pady=5)

clearbt = Button(top3,width=10, text="Clear Result",command=clear)
clearbt.pack(side=LEFT,padx=5,pady=5)

aboutbt = Button(top3,width=10, text="About",command=about)
aboutbt.pack(side=LEFT,padx=5,pady=5)

btn_exit = Button(top3, width=10, text="Exit", command=close)
btn_exit.pack(side=LEFT) 

# ================= RESULT_WINDOW+SCROLLBARS ==============
sb1 = Scrollbar(root)
sb1.pack(side=RIGHT,fill=Y)
sb2 = Scrollbar(root,orient=HORIZONTAL)
sb2.pack(side=BOTTOM,fill=X)
result = Text(root,font=font1,wrap=NONE,yscrollcommand=sb1.set,xscrollcommand=sb2.set)
result.pack(side=LEFT,fill=BOTH,expand=1)
sb1.config(command=result.yview )
sb2.config(command=result.xview )
# ======================== END ==========================
if __name__ == '__main__':
    root.mainloop()

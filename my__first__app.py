from tkinter import *

app = Tk()
app.title('Ifodani hisobla !')
app.iconbitmap('icon.ico')
app.geometry('400x400')
container = Frame(app,
                  highlightbackground='black',
                  highlightthickness=1,
                  width=400,
                  height=400)
container.pack(side="top", padx=10, pady=10)
app.wm_maxsize(height=400, width=400)

app.mainloop()

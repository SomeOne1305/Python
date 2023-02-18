from tkinter import *

app = Tk()
app.title('Ifodani hisobla !')
# app.iconbitmap()
app.geometry('400x400')
container = Frame(app,
                  highlightbackground='black',
                  highlightthickness=1,
                  width=400,
                  height=400)
container.pack(side="top", padx=10, pady=10)

Label(container, text="Ifodadagi birinchi sonni kiriting:", bg='#51ff5d', font=('Arial',16,'bold')).pack(side='top', padx=15,pady=5)
Entry(container,width=32, font=('consolas', 14)).pack(side="top")

Label(container, text="Ifodadagi oxirgi sonni kiriting:", bg='#51ff5d', font=('Arial',16,'bold')).pack(side='top', padx=15,pady=5)
Entry(container,width=32, font=('consolas', 14)).pack(side="top")

Label(container, text="Sonlar orasidagi farqni kiriting:", bg='#51ff5d', font=('Arial',16,'bold')).pack(side='top', padx=15,pady=5)
Entry(container,width=32, font=('consolas', 14)).pack(side="top")
app.wm_maxsize(height=400, width=400)

app.mainloop()

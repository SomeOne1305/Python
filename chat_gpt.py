import tkinter as tk
from termcolor import colored, cprint

def count():
    def calculate():
        start = int(start_entry.get())
        end = int(end_entry.get())
        dif = int(dif_entry.get())

        if dif > end:
            result_label.configure(text="Oxirgi son va sonlar ustidagi farq mos emas.")
        else:
            numbers = list(range(start, end + 1, dif))
            result = sum(numbers)
            numbers_str = "+".join(str(num) for num in numbers)
            # result_label.configure(text=f"{numbers_str} = {result}", fg="green")
            result_label.configure(text=numbers_str + " = " + str(result), fg="green")
    window = tk.Tk()
    window.title("Count Program")

    info_label = tk.Label(window, text="1+2+3+4+...+100 <= Shunga oxshash ifodalarni hisoblash dasturi.")
    info_label.pack()

    example_label = tk.Label(window, text='e.g. "1" - birinchi son\n"100" - oxirgi son\n"2 - 1 = 1" - sonlar orasidagi farq')
    example_label.pack()

    start_label = tk.Label(window, text="Birinchi son:")
    start_label.pack()
    start_entry = tk.Entry(window)
    start_entry.pack()

    end_label = tk.Label(window, text="Oxirgi son:")
    end_label.pack()
    end_entry = tk.Entry(window)
    end_entry.pack()

    dif_label = tk.Label(window, text="Farq:")
    dif_label.pack()
    dif_entry = tk.Entry(window)
    dif_entry.pack()

    calculate_button = tk.Button(window, text="Hisoblash", command=calculate)
    calculate_button.pack()

    result_label = tk.Label(window, text="")
    result_label.pack()

    window.mainloop()

count()

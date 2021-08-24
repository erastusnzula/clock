import time
from tkinter import *

root = Tk()
root.title("EMU")
root.resizable(False, False)
root.geometry("700x100")
root.config(bg='Sky Blue')

font = ('Times', 12, 'bold')
color = "Sky Blue"

time_frame = LabelFrame(root, bg=color, font=font, bd=5)
time_frame.place(x=5, y=10, width=690, height=80)

time_label = Label(time_frame, bg=color, fg="Blue", font=font)
time_label.pack(anchor=CENTER)


def get_current_time():
    time_format = time.strftime('Time: %H : %M : %S : %p')
    time_label.configure(text=time_format)
    time_label.after(1000, get_current_time)


get_current_time()

root.mainloop()

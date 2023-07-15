from tkinter import *
import time


# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
CHECK = '🗸'
reps = 0
n = 0
timer = None

# ---------------------------- TIMER RESET ------------------------------- # 

def reset_timer():
    global timer, n, reps
    canv.itemconfig(t_text, text=f'00:00')
    checks.config(text=' ')
    Tlab.config(text='Timer')
    wind.after_cancel(timer)
    n = 0
    reps = 0


# ---------------------------- TIMER MECHANISM ------------------------------- #

def start_timer():
    global reps, LONG_BREAK_MIN, SHORT_BREAK_MIN, WORK_MIN, n
    reps += 1

    if reps % 2 == 0:
        n += 1
        checks.config(text=CHECK * n)

    print(reps)
    if reps % 8 == 0:
        n = 0
        Tlab.config(text='Long break')
        count_down(LONG_BREAK_MIN * 60)
    elif reps % 2 == 1:
        if n%4==0:
            checks.config(text=CHECK * n)
        Tlab.config(text='Work')
        count_down(WORK_MIN * 60)
    else:
        Tlab.config(text='Break')
        count_down(SHORT_BREAK_MIN * 60)

# ---------------------------- COUNTDOWN MECHANISM ------------------------------- #
def count_down(count):
    global timer
    mins = int(count / 60)
    seconds = count % 60
    canv.itemconfig(t_text, text=f'{mins:02}:{seconds:02}')
    if count >= 0:
        timer = wind.after(1000, count_down, count - 1)
    else:
        start_timer()


# ---------------------------- UI SETUP ------------------------------- #
wind = Tk()
wind.config(pady=50, padx=100, bg=YELLOW)
wind.title('Pomodoro effect')

canv = Canvas(width=200, height=224, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file='tomato.png')
canv.create_image(100, 112, image=img)
t_text = canv.create_text(100, 130, text='00:00', font=(FONT_NAME, 28, 'bold'), fill='#ffffff')
canv.grid(column=1, row=1)

Tlab = Label(text="Timer", fg=GREEN, bg=YELLOW, highlightthickness=0, font=(FONT_NAME, 35, 'bold'))
Tlab.grid(column=1, row=0)

start_but = Button(text='Start', highlightthickness=0, command=start_timer)
reset_but = Button(text='Reset', highlightthickness=0, command=reset_timer)
start_but.grid(column=0, row=2)
reset_but.grid(column=2, row=2)

checks = Label(text='', font=(FONT_NAME, 30), fg=GREEN, bg=YELLOW, highlightthickness=0)
checks.grid(column=1, row=3)


wind.mainloop()



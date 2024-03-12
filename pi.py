import decimal
from tkinter import *


def binary_split(a, b):
    if b == a + 1:
        Pab = -(6*a - 5)*(2*a - 1)*(6*a - 1)
        Qab = 10939058860032000 * a**3
        Rab = Pab * (545140134*a + 13591409)
    else:
        m = (a + b) // 2
        Pam, Qam, Ram = binary_split(a, m)
        Pmb, Qmb, Rmb = binary_split(m, b)
        
        Pab = Pam * Pmb
        Qab = Qam * Qmb
        Rab = Qmb * Ram + Pam * Rmb
    return Pab, Qab, Rab


def chudnovsky(n):
    """Chudnovsky algorithm."""
    P1n, Q1n, R1n = binary_split(1, n)
    return (426880 * decimal.Decimal(10005).sqrt() * Q1n) / (13591409*Q1n + R1n)

def submit():
    text = entry.get()
    n = int(text)

    decimal.getcontext().prec = 13*n
    digits = str(chudnovsky(n))

    window1 = Tk()
    window1.geometry('1200x610')
    window1.title('Happy π day!')

    text = Text(window1,
              font=('Arial', 20, 'bold'),
              fg='#000000',
              width=1200,
              height=610,)
    text.pack()
    text.insert(END, digits)


window = Tk()
window.geometry('1200x610')
window.title('Happy π day!')
window.configure(bg="#FFFFFF")

photo = PhotoImage(file='chudonovsky.png')

label = Label(window,
              text='Digits of π calculator',
              font=('Comic sans', 60, 'bold'),
              fg='#000000',
              bg="#FFFFFF",
              bd=10,
              padx=10,
              pady=5,
              compound='bottom')
label.pack()

label = Label(window,
              font=('Arial', 40, 'italic', 'bold'),
              fg='#FFFFFF',
              bg="#FFFFFF",
              bd=10,
              padx=10,
              pady=5,
              image=photo,
              compound='bottom')
label.pack()

label = Label(window,
              text='Amount of iterations:',
              font=('Comic sans', 30, 'bold'),
              fg='#000000',
              bg="#FFFFFF",
              bd=10,
              padx=10,
              pady=5,
              compound='bottom')
label.pack()

entry = Entry(window,
              font=('Arial', 40, 'bold'),
              fg='#000000',
              )
entry.pack()

submit_button = Button(window, text='Compute',
                       command=submit,
                       font=('Arial', 25, 'italic', 'bold'),
                       fg='#000000',
                       activeforeground='#FFFFFF',
                       activebackground='green'
                       )
submit_button.pack()

window.mainloop()
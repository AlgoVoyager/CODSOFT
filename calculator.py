from tkinter import *

expr = ""

def press(num):
    global expr
    if expr == "":
        if num in ["+", "*", "/"]:
            expr = ""
        elif num == ".":
            expr += "0."
        else:
            expr = expr + str(num)
    else:

        if expr[-1] in ["-", "+", "/", "*", "."] and num in ["-", "+", "/", "*", "."]:
            expr = expr
        else:
            if expr == "0" or expr == "00":
                expr = str(num)
            else:
                expr = expr + str(num)
    equation.set(expr)


def equalpress():
    try:
        global expr
        total = str(eval(expr))
        if "0000000000004" in total:
            total = total.replace("00000000000004","")
        equation.set(total)
        expr = total
    except:
        equation.set(" error ")
        expr = ""


def clear():
    global expr
    expr = ""
    equation.set("")


if __name__ == "__main__":
    window = Tk()
    window.configure(background="#1F6E8C")
    window.title("Calculator")
    window.geometry("324x562")
    window.resizable(False, False)
    equation = StringVar()
    font_size = 19
    expr_field = Entry(window, textvariable=equation)
    expr_field.configure(background="#84A7A1", fg='#0E2954', font=("Arial", font_size))
    expr_field.grid(columnspan=4, ipadx=10, ipady=10, padx=10, pady=10)

    button1 = Button(window, text=' 1 ', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press(1), height=2, width=3, font=("Arial", font_size))
    button1.grid(row=2, column=0, ipadx=10, ipady=10, padx=2, pady=3)

    button2 = Button(window, text=' 2 ', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press(2), height=2, width=3, font=("Arial", font_size))
    button2.grid(row=2, column=1, ipadx=10, ipady=10, padx=2, pady=3)

    button3 = Button(window, text=' 3 ', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press(3), height=2, width=3, font=("Arial", font_size))
    button3.grid(row=2, column=2, ipadx=10, ipady=10, padx=2, pady=3)

    button4 = Button(window, text=' 4 ', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press(4), height=2, width=3, font=("Arial", font_size))
    button4.grid(row=3, column=0, ipadx=10, ipady=10, padx=2, pady=3)

    button5 = Button(window, text=' 5 ', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press(5), height=2, width=3, font=("Arial", font_size))
    button5.grid(row=3, column=1, ipadx=10, ipady=10, padx=2, pady=3)

    button6 = Button(window, text=' 6 ', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press(6), height=2, width=3, font=("Arial", font_size))
    button6.grid(row=3, column=2, ipadx=10, ipady=10, padx=2, pady=3)

    button7 = Button(window, text=' 7 ', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press(7), height=2, width=3, font=("Arial", font_size))
    button7.grid(row=4, column=0, ipadx=10, ipady=10, padx=2, pady=3)

    button8 = Button(window, text=' 8 ', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press(8), height=2, width=3, font=("Arial", font_size))
    button8.grid(row=4, column=1, ipadx=10, ipady=10, padx=2, pady=3)

    button9 = Button(window, text=' 9 ', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press(9), height=2, width=3, font=("Arial", font_size))
    button9.grid(row=4, column=2, ipadx=10, ipady=10, padx=2, pady=3)

    button0 = Button(window, text=' 0 ', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press(0), height=2, width=3, font=("Arial", font_size))
    button0.grid(row=5, column=0, ipadx=10, ipady=10, padx=2, pady=3)

    button00 = Button(window, text=' 00 ', fg='#0E2954', bg='#2E8A99',
                      command=lambda: press("00"), height=2, width=3, font=("Arial", font_size))
    button00.grid(row=5, column=1, ipadx=10, ipady=10, padx=2, pady=3)

    plus = Button(window, text=' + ', fg='#0E2954', bg='#2E8A99',
                  command=lambda: press("+"), height=2, width=3, font=("Arial", font_size))
    plus.grid(row=2, column=3, ipadx=10, ipady=10, padx=2, pady=3)

    minus = Button(window, text=' - ', fg='#0E2954', bg='#2E8A99',
                   command=lambda: press("-"), height=2, width=3, font=("Arial", font_size))
    minus.grid(row=3, column=3, ipadx=10, ipady=10, padx=2, pady=3)

    multiply = Button(window, text=' * ', fg='#0E2954', bg='#2E8A99',
                      command=lambda: press("*"), height=2, width=3, font=("Arial", font_size))
    multiply.grid(row=4, column=3, ipadx=10, ipady=10, padx=2, pady=3)

    divide = Button(window, text=' / ', fg='#0E2954', bg='#2E8A99',
                    command=lambda: press("/"), height=2, width=3, font=("Arial", font_size))
    divide.grid(row=5, column=3, ipadx=10, ipady=10, padx=2, pady=3)

    equal = Button(window, text=' = ', fg='#0E2954', bg='#84A7A1',
                   command=equalpress, height=1, width=8, font=("Arial", font_size))
    equal.grid(row=6, column=2, columnspan=2, ipadx=12, ipady=10, padx=2, pady=3)

    clear = Button(window, text='Clear', fg='#0E2954', bg='#D27685',
                   command=clear, height=1, width=8, font=("Arial", font_size))
    clear.grid(row=6, column=0, columnspan=2, ipadx=12, ipady=10, padx=2, pady=3)

    Decimal = Button(window, text='•', fg='#0E2954', bg='#2E8A99',
                     command=lambda: press('.'), height=2, width=3, font=("Arial", font_size))
    Decimal.grid(row=5, column=2, ipadx=10, ipady=10, padx=2, pady=3)

    window.mainloop()

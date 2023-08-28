import tkinter as tk
from tkinter import messagebox


class Calculator:
    expression = ''

    def __init__(self):
        self.root = tk.Tk()
        self.root.title('Calculator')
        self.root.geometry('300x350')
        self.root.configure(bg='#BEF3EE')

        self.frame = tk.Frame(self.root, width=300, height=110, bg='#BEF3EE')
        self.frame.grid(row=0, column=0)

        self.str_var = tk.StringVar()
        self.text = tk.Entry(self.frame, width=24, bg='#DAFFFB', font=('Arial', 16, 'bold'), fg='#001DA0',
                             justify=tk.RIGHT, textvariable=self.str_var)
        self.text.grid(row=0, column=0, padx=2, pady=10, sticky=tk.W + tk.E)

        self.clear = tk.Button(
            self.frame,
            text='Clear',
            font = ('Arial', 16, 'bold'),
            bg='#11B0FA',
            activebackground='grey',
            activeforeground='red',
            command=self.clear_text
        )
        self.clear.grid(row=1, column=0, padx=23, pady=5, sticky=tk.E + tk.W)

        self.button_frame = tk.Frame(self.root, width=300, height=240, bg='#BEF3EE')
        self.button_frame.grid(row=1, column=0)

        self.frame.grid_propagate(False)

        self.numbers_grid()

        self.root.mainloop()

    def clear_text(self):
        Calculator.expression = ''
        self.str_var.set(Calculator.expression)

    def btn_click(self, strng):
        if strng == '=':
            try:
                Calculator.expression = str(eval(Calculator.expression))
                self.str_var.set(Calculator.expression)
            except SyntaxError as e:
                messagebox.showwarning(title='Attention!', message='Not a valid expression')
        else:
            Calculator.expression += strng
            self.str_var.set(Calculator.expression)


    def add_numbers(self, btn_number):
        self.btn = tk.Button(self.button_frame,
                             text=btn_number,
                             width=4,
                             height=1,
                             font=('Arial', 16),
                             bg='black',
                             fg='white',
                             command=lambda: self.btn_click(btn_number)
                             )
        return self.btn


    def numbers_grid(self):
        NUMBERS = [
            ('7', '8', '9', '*'),
            ('4', '5', '6', '-'),
            ('1', '2', '3', '+'),
            ('%', '0', '/', '='),
        ]
        for i, item in enumerate(NUMBERS):
            for j, character in enumerate(item):
                btn = self.add_numbers(character)
                btn.grid(row=i, column=j, padx=1, pady=1)


if __name__ == '__main__':
    Calculator()

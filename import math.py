import tkinter as tk
import math

class ScientificCalculator(tk.Tk):
    def __init__(self):
        super().__init__()

        self.title("Scientific Calculator")

        self.num1 = tk.StringVar()
        self.num2 = tk.StringVar()
        self.result = tk.StringVar()

        self.create_widgets()
        self.create_layout()

    def create_widgets(self):
        # Input Entry
        self.entry = tk.Entry(self, textvariable=self.num1, font=('Arial', 14), justify='right')
        self.entry.grid(row=0, column=0, columnspan=4, sticky='nsew')

        # Output Label
        self.output_label = tk.Label(self, textvariable=self.result, font=('Arial', 14), bg='white', anchor='e')
        self.output_label.grid(row=1, column=0, columnspan=4, sticky='nsew')

        # Number Buttons
        for i in range(10):
            if i == 0:
                tk.Button(self, text=str(i), command=lambda num=i: self.add_to_input(str(num)), font=('Arial', 12)).grid(row=5, column=0, columnspan=2, sticky='nsew')
            else:
                tk.Button(self, text=str(i), command=lambda num=i: self.add_to_input(str(num)), font=('Arial', 12)).grid(row=(i-1)//3+2, column=(i-1)%3, sticky='nsew')

        # Function Buttons
        functions = ['C', 'CE', '/', '*', '-', '+', '.', '=', '√', 'x²', '1/x', 'sin', 'cos', 'tan', 'log', 'ln', 'x^y', 'x!']
        for i, function in enumerate(functions):
            tk.Button(self, text=function, command=lambda func=function: self.perform_operation(func), font=('Arial', 12)).grid(row=i//4+2, column=i%4+3, sticky='nsew')

        # Equal Button
        tk.Button(self, text='=', command=self.calculate, font=('Arial', 12), bg='orange', fg='white').grid(row=7, column=0, columnspan=4, sticky='nsew')

    def create_layout(self):
        for i in range(7):
            self.grid_rowconfigure(i, weight=1)
        for i in range(4):
            self.grid_columnconfigure(i, weight=1)

    def add_to_input(self, value):
        current_value = self.num1.get()
        if value == '.' and '.' in current_value:
            return
        self.num1.set(current_value + value)

    def perform_operation(self, operator):
        if operator == 'C':
            self.num1.set('')
        elif operator == 'CE':
            self.num1.set('')
            self.result.set('')
        elif operator == '=':
            self.calculate()
        elif operator == '√':
            self.result.set(math.sqrt(float(self.num1.get())))
        elif operator == 'x²':
            self.result.set(float(self.num1.get()) ** 2)
        elif operator == '1/x':
            self.result.set(1 / float(self.num1.get()))
        elif operator == 'sin':
            self.result.set(math.sin(math.radians(float(self.num1.get()))))
        elif operator == 'cos':
            self.result.set(math.cos(math.radians(float(self.num1.get()))))
        elif operator == 'tan':
            self.result.set(math.tan(math.radians(float(self.num1.get()))))
        elif operator == 'log':
            self.result.set(math.log10(float(self.num1.get())))
        elif operator == 'ln':
            self.result.set(math.log(float(self.num1.get())))
        elif operator == 'x!':
            self.result.set(math.factorial(int(self.num1.get())))
        else:
            self.num1.set(self.num1.get() + operator)

    def calculate(self):
        try:
            expression = self.num1.get()
            result = eval(expression)
            self.result.set(result)
        except Exception as e:
            self.result.set("Error")

if __name__ == "__main__":
    app = ScientificCalculator()
    app.mainloop()

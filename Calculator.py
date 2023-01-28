import tkinter as tk

def calculate():
    first_num = float(first_number_entry.get())
    second_num = float(second_number_entry.get())
    operator = operator_var.get()
    if operator == "+":
        result = first_num + second_num
    elif operator == "-":
        result = first_num - second_num
    elif operator == "*":
        result = first_num * second_num
    else:
        result = first_num / second_num
    result_label.config(text=result)

root = tk.Tk()
root.title("Calculator")

first_number_label = tk.Label(root, text="First Number")
first_number_label.grid(row=0, column=0)

first_number_entry = tk.Entry(root)
first_number_entry.grid(row=0, column=1)

operator_label = tk.Label(root, text="Operator")
operator_label.grid(row=1, column=0)

operator_var = tk.StringVar(root)
operator_var.set("+")

operator_dropdown = tk.OptionMenu(root, operator_var, "+", "-", "*", "/")
operator_dropdown.grid(row=1, column=1)

second_number_label = tk.Label(root, text="Second Number")
second_number_label.grid(row=2, column=0)

second_number_entry = tk.Entry(root)
second_number_entry.grid(row=2, column=1)

calculate_button = tk.Button(root, text="Calculate", command=calculate)
calculate_button.grid(row=3, column=0, columnspan=2)

result_label = tk.Label(root, text="")
result_label.grid(row=4, column=0, columnspan=2)

root.mainloop()

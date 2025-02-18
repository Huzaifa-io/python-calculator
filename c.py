import tkinter as tk

class Calculator(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Simple Calculator")
        self.geometry("400x600")
        self.configure(bg="#f4f4f9")

        self.expression = ""
        self.input_text = tk.StringVar()

        self.create_widgets()

    def create_widgets(self):
        input_frame = tk.Frame(self, width=400, height=50, bd=0, highlightbackground="black", highlightcolor="black", highlightthickness=1)
        input_frame.pack(side=tk.TOP)
        input_field = tk.Entry(input_frame, font=('arial', 18, 'bold'), textvariable=self.input_text, width=50, bg="#252525", fg="#fff", bd=0, justify=tk.RIGHT)
        input_field.grid(row=0, column=0)
        input_field.pack(ipady=10)

        button_frame = tk.Frame(self, width=400, height=450, bg="#f4f4f9")
        button_frame.pack()

        self.create_button(button_frame, "7", 1, 0)
        self.create_button(button_frame, "8", 1, 1)
        self.create_button(button_frame, "9", 1, 2)
        self.create_button(button_frame, "/", 1, 3, bg="#f9a825")

        self.create_button(button_frame, "4", 2, 0)
        self.create_button(button_frame, "5", 2, 1)
        self.create_button(button_frame, "6", 2, 2)
        self.create_button(button_frame, "*", 2, 3, bg="#4caf50")

        self.create_button(button_frame, "1", 3, 0)
        self.create_button(button_frame, "2", 3, 1)
        self.create_button(button_frame, "3", 3, 2)
        self.create_button(button_frame, "-", 3, 3, bg="#f9a825")

        self.create_button(button_frame, "0", 4, 0)
        self.create_button(button_frame, ".", 4, 1)
        self.create_button(button_frame, "=", 4, 2, 1, 2, bg="#4caf50")
        self.create_button(button_frame, "+", 4, 3, bg="#f9a825")

        self.create_button(button_frame, "AC", 5, 0, 1, 4, bg="#4caf50")

    def create_button(self, frame, text, row, col, rowspan=1, colspan=1, bg="#fff"):
        button = tk.Button(frame, text=text, fg="#000", width=10, height=3, bd=0, bg=bg, cursor="hand2",
                           command=lambda: self.on_button_click(text))
        button.grid(row=row, column=col, rowspan=rowspan, columnspan=colspan, padx=1, pady=1)

    def on_button_click(self, text):
        if text == "AC":
            self.expression = ""
            self.input_text.set("")
        elif text == "=":
            try:
                result = str(eval(self.expression))
                self.input_text.set(result)
                self.expression = result
            except:
                self.input_text.set("ERROR")
                self.expression = ""
        else:
            self.expression += str(text)
            self.input_text.set(self.expression)

if __name__ == "__main__":
    calculator = Calculator()
    calculator.mainloop()
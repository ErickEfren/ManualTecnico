import tkinter as tk

class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Calculadora")
        
        # Pantalla
        self.screen = tk.Entry(master, width=30, justify="right")
        self.screen.grid(row=0, column=0, columnspan=4, padx=5, pady=5)
        
        # Botones
        buttons = [
            "7", "8", "9", "/",
            "4", "5", "6", "*",
            "1", "2", "3", "-",
            "0", ".", "=", "+"
        ]
        
        # Funciones
        def button_click(value):
            current = self.screen.get()
            self.screen.delete(0, tk.END)
            self.screen.insert(0, str(current) + str(value))
        
        def button_clear():
            self.screen.delete(0, tk.END)
        
        def button_equal():
            result = eval(self.screen.get())
            self.screen.delete(0, tk.END)
            self.screen.insert(0, result)
        
        # Colocar botones en la interfaz
        row, col = 1, 0
        for button in buttons:
            if button == "=":
                tk.Button(master, text=button, width=5, height=2, command=button_equal).grid(row=row, column=col, rowspan=2, padx=5, pady=5)
            elif button == "0":
                tk.Button(master, text=button, width=11, height=2, command=lambda value=button: button_click(value)).grid(row=row+1, column=col, columnspan=2, padx=5, pady=5)
            elif button == ".":
                tk.Button(master, text=button, width=5, height=2, command=lambda value=button: button_click(value)).grid(row=row+1, column=col+1, padx=5, pady=5)
            elif button == "/":
                tk.Button(master, text=button, width=5, height=2, command=lambda value=button: button_click(value)).grid(row=row, column=col+3, padx=5, pady=5)
            elif button == "*":
                tk.Button(master, text=button, width=5, height=2, command=lambda value=button: button_click(value)).grid(row=row+1, column=col+3, padx=5, pady=5)
            elif button == "-":
                tk.Button(master, text=button, width=5, height=2, command=lambda value=button: button_click(value)).grid(row=row+2, column=col+3, padx=5, pady=5)
            elif button == "+":
                tk.Button(master, text=button, width=5, height=2, command=lambda value=button: button_click(value)).grid(row=row+3, column=col+3, padx=5, pady=5)
            else:
                tk.Button(master, text=button, width=5, height=2, command=lambda value=button: button_click(value)).grid(row=row, column=col, padx=5, pady=5)
            
            col += 1
            if col == 4:
                col = 0
                row += 1
                
        # Botón para limpiar pantalla
        tk.Button(master, text="C", width=5, height=2, command=button_clear).grid(row=row+1, column=0, columnspan=2, padx
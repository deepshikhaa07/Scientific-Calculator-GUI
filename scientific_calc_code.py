import math
import tkinter as tk
from tkinter import ttk, messagebox
import darkdetect
from math import *  # for advanced math functions
import re

class CalculatorGUI:
    def __init__(self):
        self.window = tk.Tk()
        self.window.title("Scientific Calculator")
        self.window.geometry("500x750")
        self.window.resizable(True, True)
        
        # Use system theme (dark/light)
        self.is_dark = darkdetect.isDark() if darkdetect else False
        self.configure_theme()
        
        self.calculator = Calculator()
        self.angle_mode = "RAD"  # Default to radians
        self.create_widgets()
        
        # Keyboard bindings
        self.bind_keys()

    def configure_theme(self):
        if self.is_dark:
            bg_color = "#1e1e1e"
            fg_color = "#ffffff"
            button_bg = "#2d2d2d"
            entry_bg = "#2b2b2b"
            accent1 = "#0179cb"  # blue
            accent2 = "#569cd6"  # lighter blue
            accent3 = "#4ec9b0"  # teal
            warning = "#ce9178"  # orange
        else:
            bg_color = "#f5f5f5"
            fg_color = "#000000"
            button_bg = "#ffffff"
            entry_bg = "#ffffff"
            accent1 = "#0179cb"
            accent2 = "#267acc"
            accent3 = "#28a745"
            warning = "#dc3545"

        self.style = {
            'bg': bg_color,
            'fg': fg_color,
            'button_bg': button_bg,
            'entry_bg': entry_bg,
            'accent1': accent1,
            'accent2': accent2,
            'accent3': accent3,
            'warning': warning
        }
        self.window.configure(bg=self.style['bg'])

    def create_widgets(self):
        # Main container with padding
        main_container = tk.Frame(self.window, bg=self.style['bg'])
        main_container.pack(padx=15, pady=15, fill=tk.BOTH, expand=True)

        # Display Frame
        display_frame = tk.Frame(main_container, bg=self.style['bg'])
        display_frame.pack(fill=tk.BOTH, padx=5, pady=5)

        # Mode indicator (RAD/DEG)
        self.mode_label = tk.Label(
            display_frame,
            text=self.angle_mode,
            font=('Arial', 12),
            bg=self.style['bg'],
            fg=self.style['accent3']
        )
        self.mode_label.pack(anchor='e', padx=10)

        # Main display
        self.display = tk.Entry(
            display_frame,
            font=('Consolas', 32),
            justify='right',
            bg=self.style['entry_bg'],
            fg=self.style['fg'],
            insertbackground=self.style['fg'],
            relief=tk.FLAT,
            bd=10
        )
        self.display.pack(fill=tk.BOTH, padx=10, pady=(0, 10))

        # History display
        self.history_display = tk.Text(
            display_frame,
            height=2,
            font=('Consolas', 12),
            bg=self.style['entry_bg'],
            fg=self.style['accent2'],
            relief=tk.FLAT,
            bd=5
        )
        self.history_display.pack(fill=tk.BOTH, padx=10)

        # Create tabs for different button sets
        self.tab_control = ttk.Notebook(main_container)
        self.tab_control.pack(fill=tk.BOTH, expand=True, padx=5, pady=5)

        # Standard calculator buttons
        standard_frame = tk.Frame(self.tab_control, bg=self.style['bg'])
        self.tab_control.add(standard_frame, text='Standard')

        # Scientific calculator buttons
        scientific_frame = tk.Frame(self.tab_control, bg=self.style['bg'])
        self.tab_control.add(scientific_frame, text='Scientific')

        # Standard buttons
        standard_buttons = [
            ('C', 'clear', 'warning'), ('⌫', 'backspace', 'warning'), 
            ('(', '(', 'accent2'), (')', ')', 'accent2'),
            ('7', '7'), ('8', '8'), ('9', '9'), ('÷', '/'),
            ('4', '4'), ('5', '5'), ('6', '6'), ('×', '*'),
            ('1', '1'), ('2', '2'), ('3', '3'), ('-', '-'),
            ('±', 'negate'), ('0', '0'), ('.', '.'), ('+', '+'),
            ('hist', 'history', 'accent1'), ('π', 'pi', 'accent2'), 
            ('e', 'e', 'accent2'), ('=', 'equals', 'accent1')
        ]

        # Scientific buttons
        scientific_buttons = [
            ('sin', 'sin(', 'accent3'), ('cos', 'cos(', 'accent3'), 
            ('tan', 'tan(', 'accent3'), ('RAD', 'toggle_mode', 'accent2'),
            ('asin', 'asin(', 'accent3'), ('acos', 'acos(', 'accent3'), 
            ('atan', 'atan(', 'accent3'), ('log', 'log(', 'accent3'),
            ('sinh', 'sinh(', 'accent3'), ('cosh', 'cosh(', 'accent3'), 
            ('tanh', 'tanh(', 'accent3'), ('ln', 'ln(', 'accent3'),
            ('x²', '**2', 'accent2'), ('x³', '**3', 'accent2'), 
            ('xʸ', '**', 'accent2'), ('√', 'sqrt(', 'accent2'),
            ('∛', 'cbrt(', 'accent2'), ('|x|', 'abs(', 'accent2'),
            ('1/x', '1/', 'accent2'), ('mod', '%', 'accent2'),
            ('⌊x⌋', 'floor(', 'accent2'), ('⌈x⌉', 'ceil(', 'accent2'),
            ('rand', 'random()', 'accent2'), ('fact', 'factorial(', 'accent2')
        ]

        self._create_button_grid(standard_frame, standard_buttons, 6, 4)
        self._create_button_grid(scientific_frame, scientific_buttons, 6, 4)

    def _create_button_grid(self, parent, buttons, rows, cols):
        for i, (text, command, *args) in enumerate(buttons):
            color = args[0] if args else None
            btn = tk.Button(
                parent,
                text=text,
                width=6,
                height=2,
                font=('Arial', 12, 'bold'),
                bg=self.style['button_bg'],
                fg=self.style[color] if color else self.style['fg'],
                activebackground=self.style['accent1'],
                relief=tk.FLAT,
                bd=0,
                command=lambda x=command: self.button_click(x)
            )
            btn.grid(row=i//cols, column=i%cols, padx=5, pady=5, sticky='nsew')
            
            # Hover effect
            btn.bind('<Enter>', lambda e, b=btn: b.configure(
                bg=self.style['accent1'], 
                fg=self.style['fg']
            ))
            btn.bind('<Leave>', lambda e, b=btn, c=color: b.configure(
                bg=self.style['button_bg'],
                fg=self.style[c] if c else self.style['fg']
            ))

        # Configure grid weights
        for i in range(rows):
            parent.grid_rowconfigure(i, weight=1)
        for i in range(cols):
            parent.grid_columnconfigure(i, weight=1)

    def bind_keys(self):
        self.window.bind('<Return>', lambda e: self.button_click('equals'))
        self.window.bind('<BackSpace>', lambda e: self.button_click('backspace'))
        self.window.bind('<Delete>', lambda e: self.button_click('clear'))
        self.window.bind('<Escape>', lambda e: self.button_click('clear'))
        
        # Bind number keys and operators
        for key in '0123456789+-*/.()':
            self.window.bind(key, lambda e, k=key: self.display.insert(tk.END, k))

    def button_click(self, command):
        current = self.display.get()

        if command == 'clear':
            self.display.delete(0, tk.END)
        elif command == 'backspace':
            self.display.delete(len(current) - 1)
        elif command == 'equals':
            try:
                # Replace special functions and constants
                expression = self._prepare_expression(current)
                result = eval(expression)
                self.calculator.history.append(f"{current} = {result}")
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, str(result))
                self.update_history()
            except Exception as e:
                self.display.delete(0, tk.END)
                self.display.insert(tk.END, "Error")
                messagebox.showerror("Error", str(e))
        elif command == 'toggle_mode':
            self.angle_mode = "DEG" if self.angle_mode == "RAD" else "RAD"
            self.mode_label.config(text=self.angle_mode)
        elif command == 'history':
            self.show_history_window()
        elif command == 'negate':
            if current and current[0] == '-':
                self.display.delete(0)
            else:
                self.display.insert(0, '-')
        elif command in ['pi', 'e']:
            self.display.insert(tk.END, 'π' if command == 'pi' else 'e')
        else:
            self.display.insert(tk.END, command)

    def _prepare_expression(self, expr):
        # Replace mathematical constants
        expr = expr.replace('π', str(pi))
        expr = expr.replace('e', str(e))
        
        # Handle trigonometric functions based on mode
        if self.angle_mode == "DEG":
            for func in ['sin', 'cos', 'tan']:
                expr = re.sub(f'{func}\((.*?)\)', 
                            f'{func}(radians(\\1))', 
                            expr)

        return expr

    def update_history(self):
        self.history_display.delete(1.0, tk.END)
        recent_history = self.calculator.history[-2:]
        for entry in recent_history:
            self.history_display.insert(tk.END, f"{entry}\n")

    def show_history_window(self):
        history_window = tk.Toplevel(self.window)
        history_window.title("Calculation History")
        history_window.geometry("400x500")
        history_window.configure(bg=self.style['bg'])

        # Add a scrollbar
        scrollbar = tk.Scrollbar(history_window)
        scrollbar.pack(side=tk.RIGHT, fill=tk.Y)

        history_text = tk.Text(
            history_window,
            font=('Consolas', 12),
            bg=self.style['entry_bg'],
            fg=self.style['fg'],
            yscrollcommand=scrollbar.set
        )
        history_text.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        
        scrollbar.config(command=history_text.yview)

        for entry in self.calculator.history:
            history_text.insert(tk.END, f"{entry}\n")

    def run(self):
        self.window.mainloop()

class Calculator:
    def __init__(self):
        self.history = []

if __name__ == "__main__":
    app = CalculatorGUI()
    app.run()

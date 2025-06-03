🧮 Scientific Calculator GUI
A modern, feature-rich scientific calculator built with Python and tkinter, supporting both standard and scientific operations. It adapts automatically to your system's light or dark mode using the darkdetect module and includes a history view, angle mode switching (RAD/DEG), and keyboard input support.

✨ Features
Standard & Scientific Modes with tabbed UI

Light/Dark Theme detection using darkdetect

Keyboard Input Support for smooth usage

Trigonometric Functions in RAD/DEG mode

Calculation History Viewer

Hover Effects and customizable themes

Error Handling with user-friendly messages

🧩 Requirements
Python 3.6+

Required packages:

bash
Copy
Edit
pip install darkdetect
📦 File Structure
bash
Copy
Edit
calculator_gui.py     # Main Python script containing all GUI logic
README.md             # This file
🛠 How to Run
Make sure darkdetect is installed:

bash
Copy
Edit
pip install darkdetect
Run the calculator:

bash
Copy
Edit
python calculator_gui.py
🎛 Functionality Overview
🖱 Buttons
Standard Buttons: Digits, basic operators, parentheses, history, clear, backspace, etc.

Scientific Buttons: Trigonometric (sin, cos, etc.), logarithmic (log, ln), power & roots, abs, mod, factorial, and more.

Special Controls:

RAD/DEG: Toggle angle mode for trigonometric calculations

hist: Show full calculation history

⌨ Keyboard Shortcuts
Key	Action
Enter	Evaluate (=)
Backspace	Delete last char
Delete / Escape	Clear display
0-9, +, -, *, /, .	Insert into display

🧠 Internals
Expression Parsing: Supports constants like π, e and dynamic conversion of angles using radians() when in DEG mode.

Safe eval(): Preprocessed input string ensures Python-safe evaluation.

Hover Effects: Buttons change style on hover for better UX.

History Management: Keeps a log of previous expressions and results (recent two shown inline, full history in separate window).

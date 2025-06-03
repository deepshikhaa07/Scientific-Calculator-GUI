# Scientific Calculator GUI (Python + Tkinter)

This project is a fully functional **scientific calculator** built using Python’s `tkinter` library for the graphical user interface (GUI). It combines both standard and scientific calculator features in a modern tabbed layout with adaptive theming based on your system’s light/dark mode. Designed to be intuitive and user-friendly, this calculator supports keyboard input, angle mode switching (Radians/Degrees), expression evaluation, and real-time history tracking.

---

## Overview

The calculator is divided into two main functional tabs:

- **Standard Mode**: Includes basic arithmetic operations (`+`, `-`, `×`, `÷`), number entry, brackets, and commonly used constants like `π` and `e`.
  
- **Scientific Mode**: Adds support for advanced mathematical operations such as trigonometric functions (`sin`, `cos`, `tan`, and their inverses), logarithmic and exponential functions, powers and roots, factorial, modulus, absolute value, and more.

It also includes an **angle mode switcher** (RAD/DEG), a **dedicated history display**, and dynamic evaluation with error handling.

---

## Key Features

### 🧑‍💻 GUI & Usability
- Built using `tkinter`, offering a native desktop experience.
- Organized using a **tabbed interface** for clear separation between standard and scientific functions.
- Automatically adapts to **dark or light theme** based on the user's system preferences using the `darkdetect` module.
- **Responsive design** with resizable layout and smart button grids.

### 🎯 Functional Highlights
- **Keyboard Binding Support**: Common keys (0-9, operators, Enter, Backspace) are mapped for quick input.
- **Angle Mode Toggle**: Trigonometric functions interpret input in degrees or radians based on toggle state.
- **History Tracking**: Maintains a running history of past calculations with the ability to view full history in a separate window.
- **Hover Effects**: Buttons highlight dynamically to enhance user experience and improve accessibility.
- **Error Handling**: Displays error messages for invalid expressions or math errors like division by zero.

### 🔬 Scientific Support
- Trigonometric: `sin`, `cos`, `tan`, `asin`, `acos`, `atan`
- Hyperbolic: `sinh`, `cosh`, `tanh`
- Logs and Exponentials: `log`, `ln`, `exp`, `x²`, `x³`, `xʸ`
- Roots and Powers: `√`, `∛`, `mod`, `abs`, `1/x`, `⌊x⌋`, `⌈x⌉`
- Constants: `π`, `e`
- Miscellaneous: `factorial`, `random`

---

## Internal Architecture

- **CalculatorGUI Class**: Handles all UI elements, input logic, display rendering, and event handling.
- **Calculator Class**: Maintains a history list and separates the logic from the GUI.
- **Expression Parser**: Prepares mathematical expressions before evaluation. For example, trigonometric functions are converted into radians when in DEG mode using regex replacements.
- **Theme System**: A dictionary-driven color scheme defines appearance dynamically based on system theme.

---

## Ideal Use Cases

- Desktop users needing a lightweight and capable scientific calculator.
- Students and educators looking for a customizable open-source math tool.
- Python learners exploring GUI development with `tkinter`.

---

## Getting Started

To run the application:

1. Install Python 3.6 or later.
2. Install the `darkdetect` module:
   ```bash
   pip install darkdetect
   ```
3. Run the script:
   ```bash
   python calculator_gui.py
   ```

---

## Final Thoughts

This calculator blends functionality and aesthetics into a single Python application that showcases the power of `tkinter` for desktop GUI development. It’s a great starting point for learners or a handy tool for daily calculations.

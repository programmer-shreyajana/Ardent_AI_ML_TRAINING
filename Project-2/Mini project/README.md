# 🧮 Advanced Python Calculator

A feature-rich command-line calculator built with Python, supporting both basic arithmetic and statistical operations — with clean input validation and an interactive menu interface.

---

## 📌 Project Overview

This mini project implements an **interactive CLI calculator** using core Python concepts including functions, loops, conditionals, type casting, and exception handling. It uses Python's built-in `statistics` module to support statistical operations beyond standard arithmetic.

---

## 🎯 Objective

> Build a user-friendly terminal calculator that handles arithmetic operations, statistical computations, edge cases (like division by zero), and invalid inputs — all through a clean, menu-driven interface.

---

## 📂 Repository Structure

```
├── calculator.py     # Main calculator script
└── README.md
```

---

## ⚙️ Features

| Category | Operations |
|---|---|
| **Basic Arithmetic** | Addition `+`, Subtraction `-`, Multiplication `*`, Division `/` |
| **Advanced Arithmetic** | Modulus `%` |
| **Statistical** | Mean, Median, Mode, Average |
| **Error Handling** | Division by zero, Modulus by zero, invalid input, no-mode detection |
| **Multi-number Input** | Space-separated number lists for statistical functions |

---

## 🔧 Tech Stack

- **Language:** Python 3
- **Environment:** Terminal / VS Code / Any Python IDE
- **Libraries:**
  - `statistics` — mean, median, mode, multimode (standard library)
  - No external dependencies required

---

## 🧪 Program Workflow

The calculator follows a clean modular design with 4 dedicated functions:

1. **`display_menu()`** — Renders the formatted options menu
2. **`get_two_numbers()`** — Prompts and validates two numeric inputs for arithmetic
3. **`get_numbers()`** — Prompts and validates a list of space-separated numbers for statistics
4. **`run_calculator()`** — Main loop that drives the entire program with choice routing

---

## 📋 Menu Options

```
========================================
       🧮  PYTHON CALCULATOR
========================================
  Basic Operations:
   1. Addition       (+)
   2. Subtraction    (-)
   3. Multiplication (*)
   4. Division       (/)
   5. Modulus        (%)

  Statistical Operations:
   6. Mean
   7. Median
   8. Mode
   9. Average (same as Mean)

   0. Exit
========================================
```

---

## 📈 Sample Output

The screenshot below shows the calculator running live in the terminal — menu display followed by an Addition operation:

![Calculator Terminal Output](https://github.com/user-attachments/assets/e65864d2-3f9e-41fb-9536-f0390399ce15)

**Additional example outputs:**

```
========================================
       🧮  PYTHON CALCULATOR
========================================
  Basic Operations:
   1. Addition       (+)
   2. Subtraction    (-)
   3. Multiplication (*)
   4. Division       (/)
   5. Modulus        (%)

  Statistical Operations:
   6. Mean
   7. Median
   8. Mode
   9. Average (same as Mean)

   0. Exit
========================================
Select an option (0-9): 1
Enter first number : 10
Enter second number: 5

  10.0 + 5.0 = 15.0

Press Enter to continue...
```

```
Select an option (0-9): 8
Enter numbers separated by spaces: 3 3 5 7 7 7

  Numbers : [3.0, 3.0, 5.0, 7.0, 7.0, 7.0]
  Mode    : 7.0

Press Enter to continue...
```

```
Select an option (0-9): 4
Enter first number : 9
Enter second number: 0

  ❌ Error: Division by zero is not allowed.

Press Enter to continue...
```

```
Select an option (0-9): 0

  👋 Goodbye! Thanks for using the calculator.
```

---

## 🔍 Key Concepts Used

- **Functions** — Modular design with four reusable helper functions
- **while True loop with break** — Keeps the calculator running until the user exits
- **try / except** — Catches invalid (non-numeric) input gracefully
- **Type casting** — `float()` conversion via `map()` for multi-number input
- **f-Strings** — Clean formatted output for results
- **list() + map()** — Parsing space-separated number input into a float list
- **multimode()** — Handles datasets with multiple modes or no mode correctly
- **`if __name__ == "__main__"`** — Entry point guard for safe module importing

---

## 🚀 Getting Started

### Run Locally

```bash
# Clone the repository
git clone https://github.com/your-username/python-calculator.git
cd python-calculator

# Run the calculator
python calculator.py
```

> No pip installs needed — uses Python's standard library only.

---

## 📋 Requirements

```
Python 3.x (no external libraries required)
```

---

## 🤝 Contributing

Pull requests are welcome. For major changes, please open an issue first to discuss what you'd like to change.

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).

---

*Built with ❤️ using Python*

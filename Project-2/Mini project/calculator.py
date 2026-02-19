"""
╔══════════════════════════════════════════════════════════╗
║         PYTHON ADVANCED CALCULATOR                       ║
║   Operations: + - * /  |  Stats: Mean, Median, Mode     ║
║                Average, Percentage                       ║
╚══════════════════════════════════════════════════════════╝
"""

from statistics import mean, median, mode, multimode


# ─────────────────────────────────────────────
#  DISPLAY HELPERS
# ─────────────────────────────────────────────

def print_banner():
    print("\n" + "═" * 52)
    print("         🧮  ADVANCED PYTHON CALCULATOR")
    print("═" * 52)

def print_menu():
    print("""
  ┌─────────────────────────────────────────┐
  │  BASIC OPERATIONS                       │
  │   1. Addition          ( a + b )        │
  │   2. Subtraction       ( a - b )        │
  │   3. Multiplication    ( a * b )        │
  │   4. Division          ( a / b )        │
  │                                         │
  │  STATISTICS  (enter a list of numbers)  │
  │   5. Mean (Average)                     │
  │   6. Median                             │
  │   7. Mode                               │
  │   8. All Stats at Once                  │
  │                                         │
  │  PERCENTAGE                             │
  │   9. Percentage Calculator              │
  │                                         │
  │   0. Exit                               │
  └─────────────────────────────────────────┘""")


# ─────────────────────────────────────────────
#  INPUT HELPERS  (type casting)
# ─────────────────────────────────────────────

def get_float(prompt: str) -> float:
    """Prompt until the user enters a valid number (int or float)."""
    while True:
        raw = input(prompt).strip()
        try:
            return float(raw)          # type casting: str → float
        except ValueError:
            print(f"  ⚠  '{raw}' is not a valid number. Try again.")


def get_number_list(prompt: str) -> list[float]:
    """
    Prompt for a comma/space-separated list of numbers.
    Returns a list of floats (type casting applied to each element).
    """
    while True:
        raw = input(prompt).strip()
        try:
            # Replace commas with spaces, then split and cast each token
            tokens = raw.replace(",", " ").split()
            if len(tokens) < 2:
                print("  ⚠  Please enter at least 2 numbers.")
                continue
            numbers = [float(t) for t in tokens]   # type casting list
            return numbers
        except ValueError:
            print("  ⚠  Invalid input. Use numbers separated by spaces or commas.")


# ─────────────────────────────────────────────
#  BASIC OPERATIONS
# ─────────────────────────────────────────────

def do_addition():
    a = get_float("  Enter first number  : ")
    b = get_float("  Enter second number : ")
    result = a + b
    print(f"\n  ✅  {a} + {b} = {result}")

def do_subtraction():
    a = get_float("  Enter first number  : ")
    b = get_float("  Enter second number : ")
    result = a - b
    print(f"\n  ✅  {a} - {b} = {result}")

def do_multiplication():
    a = get_float("  Enter first number  : ")
    b = get_float("  Enter second number : ")
    result = a * b
    print(f"\n  ✅  {a} × {b} = {result}")

def do_division():
    a = get_float("  Enter first number  : ")
    b = get_float("  Enter second number : ")
    if b == 0:
        print("  ❌  Error: Cannot divide by zero!")
    else:
        result = a / b
        print(f"\n  ✅  {a} ÷ {b} = {result:.6g}")


# ─────────────────────────────────────────────
#  STATISTICS
# ─────────────────────────────────────────────

def fmt(n: float) -> str:
    """Format a float nicely (remove trailing zeros)."""
    return f"{n:.6g}"


def do_mean():
    nums = get_number_list("  Enter numbers (e.g. 4 8 15 16 23 42): ")
    result = mean(nums)
    print(f"\n  ✅  Mean  =  {fmt(result)}")
    print(f"       (Sum {sum(nums)} ÷ Count {len(nums)})")


def do_median():
    nums = get_number_list("  Enter numbers: ")
    sorted_nums = sorted(nums)
    result = median(nums)
    print(f"\n  Sorted : {sorted_nums}")
    print(f"  ✅  Median = {fmt(result)}")


def do_mode():
    nums = get_number_list("  Enter numbers: ")
    modes = multimode(nums)       # handles multiple modes
    if len(modes) == len(set(nums)):
        print("\n  ℹ  No mode — all values appear equally often.")
    else:
        print(f"\n  ✅  Mode = {modes if len(modes) > 1 else modes[0]}")


def do_all_stats():
    nums = get_number_list("  Enter numbers: ")
    sorted_nums = sorted(nums)
    n       = len(nums)
    total   = sum(nums)
    avg     = mean(nums)
    med     = median(nums)
    modes   = multimode(nums)
    minimum = min(nums)
    maximum = max(nums)

    print(f"""
  ┌─────────────────────────────────────┐
  │  STATISTICAL SUMMARY                │
  ├─────────────────────────────────────┤
  │  Count   : {n:<27}│
  │  Numbers : {str(sorted_nums):<27}│
  │  Sum     : {fmt(total):<27}│
  │  Mean    : {fmt(avg):<27}│
  │  Median  : {fmt(med):<27}│
  │  Mode    : {str(modes if len(modes)>1 else modes[0]) if len(modes)<len(set(nums)) else "No mode":<27}│
  │  Min     : {fmt(minimum):<27}│
  │  Max     : {fmt(maximum):<27}│
  └─────────────────────────────────────┘""")


# ─────────────────────────────────────────────
#  PERCENTAGE
# ─────────────────────────────────────────────

def do_percentage():
    print("""
  Percentage options:
   a. What is X% of Y?          (e.g. 20% of 150)
   b. X is what % of Y?         (e.g. 30 is what % of 200)
   c. % change from X to Y      (e.g. 50 → 75)
""")
    choice = input("  Choose (a/b/c): ").strip().lower()

    if choice == "a":
        pct = get_float("  Enter percentage X : ")
        val = get_float("  Enter value Y      : ")
        result = (pct / 100) * val
        print(f"\n  ✅  {pct}% of {val} = {fmt(result)}")

    elif choice == "b":
        part = get_float("  Enter part  X : ")
        whole = get_float("  Enter whole Y : ")
        if whole == 0:
            print("  ❌  Cannot divide by zero!")
        else:
            result = (part / whole) * 100
            print(f"\n  ✅  {part} is {fmt(result)}% of {whole}")

    elif choice == "c":
        old = get_float("  Enter original value : ")
        new = get_float("  Enter new value      : ")
        if old == 0:
            print("  ❌  Cannot divide by zero!")
        else:
            change = ((new - old) / abs(old)) * 100
            direction = "increase" if change >= 0 else "decrease"
            print(f"\n  ✅  {fmt(abs(change))}% {direction}  ({old} → {new})")
    else:
        print("  ⚠  Invalid option.")


# ─────────────────────────────────────────────
#  MAIN LOOP
# ─────────────────────────────────────────────

def main():
    print_banner()

    dispatch = {
        "1": do_addition,
        "2": do_subtraction,
        "3": do_multiplication,
        "4": do_division,
        "5": do_mean,
        "6": do_median,
        "7": do_mode,
        "8": do_all_stats,
        "9": do_percentage,
    }

    while True:
        print_menu()
        choice = input("  ➤  Choose an option (0–9): ").strip()

        if choice == "0":
            print("\n  👋  Goodbye!\n")
            break
        elif choice in dispatch:
            print()
            dispatch[choice]()
            input("\n  Press Enter to continue...")
        else:
            print("  ⚠  Invalid choice. Enter a number from 0 to 9.")


if __name__ == "__main__":
    main()

import tkinter as tk
from tkinter import ttk

exchange_rates = {
    'USD': {'INR': 83.2, 'EUR': 0.92},
    'INR': {'USD': 0.012, 'EUR': 0.011},
    'EUR': {'USD': 1.09, 'INR': 90.5}
}

def convert_currency(amount, source, target):
    if source == target:
        return round(amount, 2)
    try:
        rate = exchange_rates[source][target]
        return round(amount * rate, 2)
    except KeyError:
        return None

def run_cli():
    print("=== Currency Converter (CLI Mode) ===")
    try:
        amount = float(input("Enter amount: "))
        source = input("From currency (e.g., INR, USD, EUR): ").upper()
        target = input("To currency (e.g., INR, USD, EUR): ").upper()

        result = convert_currency(amount, source, target)
        if result is None:
            print("Conversion not available for selected currencies.")
        else:
            print(f"{amount} {source} = {result} {target}")
    except Exception as e:
        print("Invalid input. Please try again.")

def run_gui():
    def convert():
        try:
            amount = float(entry_amount.get())
            from_curr = combo_from.get()
            to_curr = combo_to.get()
            result_value = convert_currency(amount, from_curr, to_curr)
            if result_value is None:
                result.set("Conversion not available")
            else:
                result.set(f"{result_value:.2f} {to_curr}")
        except:
            result.set("Invalid input")

    window = tk.Tk()
    window.title("Currency Converter")
    window.geometry("300x250")

    tk.Label(window, text="Amount").pack()
    entry_amount = tk.Entry(window)
    entry_amount.pack()

    tk.Label(window, text="From").pack()
    combo_from = ttk.Combobox(window, values=list(exchange_rates.keys()))
    combo_from.pack()

    tk.Label(window, text="To").pack()
    combo_to = ttk.Combobox(window, values=list(exchange_rates.keys()))
    combo_to.pack()

    tk.Button(window, text="Convert", command=convert).pack(pady=10)

    result = tk.StringVar()
    tk.Label(window, textvariable=result, font=("Arial", 12, "bold")).pack()

    window.mainloop()

def main():
    print("Select Mode:")
    print("1. CLI (Command Line)")
    print("2. GUI (Tkinter)")
    choice = input("Enter 1 or 2: ").strip()

    if choice == '1':
        run_cli()
    elif choice == '2':
        run_gui()
    else:
        print("Invalid choice. Exiting...")

if __name__ == "__main__":
    main()

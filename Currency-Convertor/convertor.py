import tkinter as tk
from tkinter import ttk

exchange_rates = {
    'USD': {'INR': 83.2, 'EUR': 0.92, 'GBP': 0.78, 'JPY': 150.3, 'AUD': 1.54, 'CAD': 1.37, 'CNY': 7.11},
    'INR': {'USD': 0.012, 'EUR': 0.011, 'GBP': 0.0094, 'JPY': 1.81, 'AUD': 0.018, 'CAD': 0.016, 'CNY': 0.085},
    'EUR': {'USD': 1.09, 'INR': 90.5, 'GBP': 0.85, 'JPY': 163.7, 'AUD': 1.67, 'CAD': 1.49, 'CNY': 7.77},
    'GBP': {'USD': 1.28, 'INR': 106.6, 'EUR': 1.17, 'JPY': 192.5, 'AUD': 1.96, 'CAD': 1.75, 'CNY': 9.1},
    'JPY': {'USD': 0.0067, 'INR': 0.55, 'EUR': 0.0061, 'GBP': 0.0052, 'AUD': 0.010, 'CAD': 0.0091, 'CNY': 0.047},
    'AUD': {'USD': 0.65, 'INR': 55.3, 'EUR': 0.60, 'GBP': 0.51, 'JPY': 100.2, 'CAD': 0.89, 'CNY': 4.6},
    'CAD': {'USD': 0.73, 'INR': 61.8, 'EUR': 0.67, 'GBP': 0.57, 'JPY': 111.9, 'AUD': 1.12, 'CNY': 5.18},
    'CNY': {'USD': 0.14, 'INR': 11.7, 'EUR': 0.13, 'GBP': 0.11, 'JPY': 21.1, 'AUD': 0.22, 'CAD': 0.19}
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


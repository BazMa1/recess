import tkinter as tk

def print_receipt():
    items = []
    total = 0

    # Get items and prices from the input fields
    for i in range(len(item_entries)):
        item = item_entries[i].get()
        price = price_entries[i].get()
        if item and price:
            items.append((item, float(price)))
            total += float(price)

    # Generate the receipt string
    receipt = "===== Receipt =====\n"
    for item, price in items:
        receipt += f"{item}: ${price:.2f}\n"
    receipt += "===================\n"
    receipt += f"Total: ${total:.2f}"

    receipt_text.delete(1.0, tk.END)  # Clear previous receipt
    receipt_text.insert(tk.END, receipt)

# Create the main window
window = tk.Tk()
window.title("Receipt Printing Program")

# Create lists to store the input fields
item_entries = []
price_entries = []

# Create the item and price input fields
for i in range(5):
    item_label = tk.Label(window, text="Item:")
    item_label.grid(row=i, column=0, padx=5, pady=5)

    item_entry = tk.Entry(window)
    item_entry.grid(row=i, column=1, padx=5, pady=5)
    item_entries.append(item_entry)

    price_label = tk.Label(window, text="Price:")
    price_label.grid(row=i, column=2, padx=5, pady=5)

    price_entry = tk.Entry(window)
    price_entry.grid(row=i, column=3, padx=5, pady=5)
    price_entries.append(price_entry)

# Create the print button
print_button = tk.Button(window, text="Print Receipt", command=print_receipt)
print_button.grid(row=5, column=0, columnspan=4, padx=5, pady=10)

# Create the receipt text area
receipt_text = tk.Text(window, height=10, width=40)
receipt_text.grid(row=6, column=0, columnspan=4, padx=5, pady=10)

# Run the GUI event loop
window.mainloop()


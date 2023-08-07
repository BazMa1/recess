import tkinter as tk

class ReceiptPrintingApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Bazziwe Receipt Printing App")
        
        self.items = []
        
        self.item_label = tk.Label(root, text="Item:")
        self.item_label.grid(row=0, column=0, padx=10, pady=10)
        
        self.item_entry = tk.Entry(root)
        self.item_entry.grid(row=0, column=1, padx=10, pady=10)
        
        self.quantity_label = tk.Label(root, text="Quantity:")
        self.quantity_label.grid(row=1, column=0, padx=10, pady=10)
        
        self.quantity_entry = tk.Entry(root)
        self.quantity_entry.grid(row=1, column=1, padx=10, pady=10)
        
        self.unit_price_label = tk.Label(root, text="Unit Price:")
        self.unit_price_label.grid(row=2, column=0, padx=10, pady=10)
        
        self.unit_price_entry = tk.Entry(root)
        self.unit_price_entry.grid(row=2, column=1, padx=10, pady=10)
        
        self.add_button = tk.Button(root, text="Add Item", command=self.add_item)
        self.add_button.grid(row=3, column=0, padx=10, pady=10)
        
        self.print_button = tk.Button(root, text="Print Receipt", command=self.print_receipt)
        self.print_button.grid(row=3, column=1, padx=10, pady=10)
        
        self.receipt_text = tk.Text(root, height=10, width=40)
        self.receipt_text.grid(row=4, columnspan=2, padx=10, pady=10)
        
    def add_item(self):
        item = self.item_entry.get()
        quantity = int(self.quantity_entry.get())
        unit_price = float(self.unit_price_entry.get())
        total_price = quantity * unit_price
        
        self.items.append((item, quantity, unit_price, total_price))
        
        self.receipt_text.insert(tk.END, f"Item: {item}\n")
        self.receipt_text.insert(tk.END, f"Quantity: {quantity}\n")
        self.receipt_text.insert(tk.END, f"Unit Price: ${unit_price}\n")
        self.receipt_text.insert(tk.END, f"Total Price: ${total_price}\n")
        self.receipt_text.insert(tk.END, "-"*20 + "\n")
        
        self.clear_entries()
        
    def print_receipt(self):
        receipt = "Receipt\n\n"
        total_amount = 0
        
        for item, quantity, unit_price, total_price in self.items:
            receipt += f"Item: {item}\n"
            receipt += f"Quantity: {quantity}\n"
            receipt += f"Unit Price: ${unit_price}\n"
            receipt += f"Total Price: ${total_price}\n"
            receipt += "-"*20 + "\n"
            
            total_amount += total_price
        
        receipt += f"Total Amount: ${total_amount}"
        
        self.receipt_text.delete(1.0, tk.END)
        self.receipt_text.insert(tk.END, receipt)
        
    def clear_entries(self):
        self.item_entry.delete(0, tk.END)
        self.quantity_entry.delete(0, tk.END)
        self.unit_price_entry.delete(0, tk.END)

root = tk.Tk()
app = ReceiptPrintingApp(root)
root.mainloop()

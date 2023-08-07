# Import the necessary modules.
import tkinter as tk
from tkinter import ttk
# Create the main window.
root = tk.Tk()
root.title("Receipt Printer")
# Create the frame for the input fields.
input_frame = tk.Frame(root)
input_frame.pack()
# Create the label for the product name.
product_name_label = tk.Label(input_frame, text="Product Name")
product_name_label.grid(row=0, column=0)
# Create the entry field for the product name.
product_name_entry = tk.Entry(input_frame)
product_name_entry.grid(row=0, column=1)
# Create the label for the price.
price_label = tk.Label(input_frame, text="Price")
price_label.grid(row=1, column=0)
# Create the entry field for the price.
price_entry = tk.Entry(input_frame)
price_entry.grid(row=1, column=1)
# Create the frame for the buttons.
button_frame = tk.Frame(root)
button_frame.pack()
# Create the print button.
print_button = tk.Button(button_frame, text="Print Receipt")
print_button["command"] = lambda : print_receipt()
print_button.grid(row=0, column=0)

# Create the quit button.
quit_button = tk.Button(button_frame, text="Quit", command=root.quit)
quit_button.grid(row=0, column=1)
# Create the function to print the receipt.
def print_receipt():
  # Get the product name and price from the entry fields.
  product_name = product_name_entry.get().strip()
  if not product_name or len(product_name)==0:
      return
  try:
      float(price_entry.get())
  except ValueError:
      
    
  
  # Create the receipt text.
   receipt_text = "Thank you! Here is your receipt:\n" + \
      "\t\t{0}\n".format(product_name)+ \
          "\t\t${0:.2f}".format(float(price_entry.get
                                      ()))+ "\n"
          
  
  # Print the receipt text to the console.
  print(receipt_text)
# Start the main loop.
root.mainloop()
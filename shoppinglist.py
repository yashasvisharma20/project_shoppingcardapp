import tkinter as tk
from tkinter import ttk
root = tk.Tk()
root.title("Shopping List App")
root.geometry("850x450")
root['bg']="Pink"

l1 = tk.Label(root,text="Take Your Bucket",bg="Brown",fg="White",font=("Times New Roman",20,"italic"))
l1.pack()
error_label =tk.Label(root,text ="Please select an item to remove.",bg="Red",fg="White")
def add_item():
    item = entry.get()
    quantity = quantity_entry.get()
    unit = selected_unit.get()
    category = selected_category.get()
    
    if item and quantity and unit and category:
        formatted_item = f"{quantity} {unit} of {item} ({category})"
        shopping_list.append(formatted_item)
        list_box.insert(tk.END, formatted_item)
        if item:
            list_box.insert(tk.END, item)
            entry.delete(0, tk.END)
        else:
            return error_label

def remove_item():
    selected_indices = list_box.curselection()
    if selected_indices:
        for index in selected_indices:
            list_box.delete(index)
    else:
        return error_label

categories = ["Groceries", "Household", "Electronics","Cosmetic"]
selected_category = tk.StringVar()
category_menu = ttk.Combobox(root, textvariable=selected_category, values=categories)
category_menu.pack(pady=10)
    

entry = tk.Entry(root)
entry.pack(pady=10)

quantity_label = tk.Label(root, text="Quantity:",font=("Arial Bold",16))
quantity_label.pack()

quantity_entry = tk.Entry(root)
quantity_entry.pack()

units = ["lbs", "oz", "g", "kg", "pieces", "gallons", "liters", "units"]
selected_unit = tk.StringVar()
unit_menu = ttk.Combobox(root, textvariable=selected_unit, values=units)
unit_menu.pack()


add_button = tk.Button(root, text="Add", command=add_item,bg="Sky Blue",fg="White",font=("Arial Bold",16))
add_button.pack()

remove_button = tk.Button(root, text="Remove Selected", command=remove_item,bg="Grey",fg="White",font=("Arial Bold",16))
remove_button.pack()


list_box = tk.Listbox(root,height=20,width=40)
list_box.pack()

shopping_list =[]

root.mainloop()

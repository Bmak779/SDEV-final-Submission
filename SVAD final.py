import tkinter as tk
from tkinter import messagebox, Toplevel
from PIL import Image, ImageTk

class InventoryManager:
    def __init__(self):
        self.inventory = {}

    def add_item(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] += quantity
        else:
            self.inventory[item] = quantity

    def remove_item(self, item):
        if item in self.inventory:
            del self.inventory[item]
        else:
            messagebox.showerror("Error", "Item not found in inventory.")

    def update_quantity(self, item, quantity):
        if item in self.inventory:
            self.inventory[item] = quantity
        else:
            messagebox.showerror("Error", "Item not found in inventory.")

    def view_inventory(self):
        inventory_list = "\n".join([f"{item}: {quantity}" for item, quantity in self.inventory.items()])
        return inventory_list

class InventoryApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Inventory Management System")

        self.inventory_manager = InventoryManager()

        self.item_label = tk.Label(master, text="Item:")
        self.item_label.grid(row=0, column=0)

        self.item_entry = tk.Entry(master)
        self.item_entry.grid(row=0, column=1)

        self.quantity_label = tk.Label(master, text="Quantity:")
        self.quantity_label.grid(row=1, column=0)

        self.quantity_entry = tk.Entry(master)
        self.quantity_entry.grid(row=1, column=1)

        self.add_button = tk.Button(master, text="Add Item", command=self.add_item)
        self.add_button.grid(row=2, column=0, columnspan=2, pady=10)

        self.remove_button = tk.Button(master, text="Remove Item", command=self.remove_item)
        self.remove_button.grid(row=3, column=0, columnspan=2, pady=5)

        self.update_button = tk.Button(master, text="Update Quantity", command=self.update_quantity)
        self.update_button.grid(row=4, column=0, columnspan=2, pady=5)

        self.view_button = tk.Button(master, text="View Inventory", command=self.view_inventory_window)
        self.view_button.grid(row=5, column=0, columnspan=2, pady=5)

        # Load and display an image
        image_path_1 = "image 1.jpg"  # Adjust the path as needed
        self.image_1 = Image.open(image_path_1)
        self.photo_1 = ImageTk.PhotoImage(self.image_1)
        self.image_label_1 = tk.Label(master, text="A Large Warehouse Aisle", image=self.photo_1, compound=tk.TOP)
        self.image_label_1.grid(row=0, column=2, rowspan=3, padx=10)

    def add_item(self):
        item = self.item_entry.get()
        quantity = self.quantity_entry.get()
        if not item or not quantity:
            messagebox.showerror("Error", "Both item and quantity fields must be filled.")
            return
        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be a positive integer.")
            return
        quantity = int(quantity)
        self.inventory_manager.add_item(item, quantity)
        messagebox.showinfo("Success", "Item added to inventory.")

    def remove_item(self):
        item = self.item_entry.get()
        if not item:
            messagebox.showerror("Error", "Item field must be filled.")
            return
        self.inventory_manager.remove_item(item)

    def update_quantity(self):
        item = self.item_entry.get()
        quantity = self.quantity_entry.get()
        if not item or not quantity:
            messagebox.showerror("Error", "Both item and quantity fields must be filled.")
            return
        if not quantity.isdigit():
            messagebox.showerror("Error", "Quantity must be a positive integer.")
            return
        quantity = int(quantity)
        self.inventory_manager.update_quantity(item, quantity)

    def view_inventory_window(self):
        inventory = self.inventory_manager.view_inventory()
        view_window = Toplevel(self.master)
        view_window.title("View Inventory")

        # Display inventory text
        inventory_label = tk.Label(view_window, text=inventory)
        inventory_label.pack()

        # Load and display an image with ALT text
        image_path_2 = "image 2.jpg"  # Adjust the path as needed
        self.image_2 = Image.open(image_path_2)
        self.photo_2 = ImageTk.PhotoImage(self.image_2)
        image_label_2 = tk.Label(view_window, text="A Worker Attempting to Identify a Pallet of Product", image=self.photo_2, compound=tk.TOP)
        image_label_2.pack()

if __name__ == "__main__":
    root = tk.Tk()
    app = InventoryApp(root)
    root.mainloop()

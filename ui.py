#!/usr/bin/env python3
import db
import tkinter as tk
from tkinter import ttk
import locale
from business import Product, LineItem, Cart
import shopping_cart

class shoppingIndex(ttk.Frame):
    def __init__(self, parent):
        ttk.Frame.__init__(self, parent, padding="10 10 10 10")
        self.parent = parent
        self.product = Product()

        # Set locale
        result = locale.setlocale(locale.LC_ALL, '')
        if result == 'C':
            locale.setlocale(locale.LC_ALL, 'en_US')

        # Define string variables for text entry fields
        self.product0 = tk.StringVar()
        self.product1 = tk.StringVar()
        self.product2 = tk.StringVar()
        self.product3 = tk.StringVar()
        self.product4 = tk.StringVar()
        self.product5 = tk.StringVar()
        self.product6 = tk.StringVar()
        self.product7 = tk.StringVar()
        self.product8 = tk.StringVar()
        self.product9 = tk.StringVar()
        self.product10 = tk.StringVar()
        self.product11 = tk.StringVar()
        self.product12 = tk.StringVar()
        self.product13 = tk.StringVar()

        self.initComponents()


    def initComponents(self):
        self.pack()

        # Display the grid of labels and text entry fields
        ttk.Label(self, text="Cucumber:").grid(
            column=0, row=0, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product0).grid(
            column=1, row=0)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=0, sticky=tk.E)

        ttk.Label(self, text="Gherkins:").grid(
            column=0, row=1, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product1).grid(
            column=1, row=1)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=1, sticky=tk.E)

        ttk.Label(self, text="Cornichon:").grid(
            column=0, row=2, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product2).grid(
            column=1, row=2)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=2, sticky=tk.E)

        ttk.Label(self, text="Brined pickles:").grid(
            column=0, row=3, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product3).grid(
            column=1, row=3)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=3, sticky=tk.E)

        ttk.Label(self, text="Kosher Dill:").grid(
            column=0, row=4, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product4).grid(
            column=1, row=4)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=4, sticky=tk.E)

        ttk.Label(self, text="Dill:").grid(
            column=0, row=5, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product5).grid(
            column=1, row=5)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=5, sticky=tk.E)

        ttk.Label(self, text="Lime Pickles:").grid(
            column=0, row=6, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product6).grid(
            column=1, row=6)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=6, sticky=tk.E)

        ttk.Label(self, text="Bread-and-butter Pickles:").grid(
            column=0, row=7, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product7).grid(
            column=1, row=7)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=7, sticky=tk.E)

        ttk.Label(self, text="cinnamon pickles:").grid(
            column=0, row=8, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product8).grid(
            column=1, row=8)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=8, sticky=tk.E)

        ttk.Label(self, text="pressgurka:").grid(
            column=0, row=9, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product9).grid(
            column=1, row=9)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=9, sticky=tk.E)

        ttk.Label(self, text="kool-aid pickles (i swear this is a real thing):").grid(
            column=0, row=10, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product10).grid(
            column=1, row=10)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=10, sticky=tk.E)

        ttk.Label(self, text="Pickle:").grid(
            column=0, row=11, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product11).grid(
            column=1, row=11)
        ttk.Label(self, text="$2.99").grid(
            column=3, row=11, sticky=tk.E)

        ttk.Label(self, text="Cart total:").grid(
            column=0, row=12, sticky=tk.E)
        ttk.Entry(self, width=25, textvariable=self.product12).grid(
            column=1, row=12)
        ttk.Entry(self, width=25, textvariable=self.product13).grid(
            column=2, row=12)

        self.makeButtons()



        for child in self.winfo_children():
            child.grid_configure(padx=5, pady=3)

    def makeButtons(self):
        # Create a frame to store the two buttons
        buttonFrame = ttk.Frame(self)

        # Add the button frame to the bottom row of the main grid
        buttonFrame.grid(column=4, row=12, columnspan=1, sticky=tk.E)

        # Add two buttons to the button frame
        ttk.Button(buttonFrame, text="Add to Cart",) \
            .grid(column=0, row=0, padx=5)

    def checkout(self):

        db.updateproducts()


if __name__ == "__main__":
    cart = Cart()
    root = tk.Tk()
    root.title("Harry Pickle's Delightful Surprise")
    shoppingIndex(root)
    root.mainloop()


from wrapper import Wrapper
import tkinter as tk
from logo import serve_logo

'''
Application builder for Baker Tech Services Item checkout (release-v1.0.1)
Author: Marcus Andrist marcus.andrist@drake.edu
Date: 6/09/23
Desc:
This file utilizes a GUI application using tkiner and the ConnectWise api wrapper (wrapper.py) to send GET, POST, and PUT requests to the ConnectWise PSA database integrated through their RESTful api, their documentation can be found here: https://developer.connectwise.com/
'''


class App:
    # Tkinter class constructor
    def __init__(self, root: object):
        # Instance variables
        self.root = root
        self.wrapper = Wrapper()
        self.root.iconphoto(True, serve_logo())
        self.root.title("BakerTS Checkout Application")
        self.root.geometry("600x700")
        self.root.configure(bg="#003C5E")

        self.first_page()
    
    # Entry-point function
    def first_page(self):
        self.clear_root()
        label = self.create_label("UPC #")
        entry = self.create_entry()

        def on_return(event=None):
            val = entry.get()
            # Attempt to fetch an item/configuration based on the provided tag
            try:
                config_name = self.wrapper.fetch_config_from_tag(val)["name"]
                self.second_page(val, config_name)
            # Redirect to page with more pointers on errors
            except:
                self.non_happy_first_page()

        self.root.bind("<Return>", on_return)
    
    # Function to resolve initial page exception encountered
    def non_happy_first_page(self):
        self.clear_root()
        label = self.create_label("UPC #")
        entry = self.create_entry()
        error_label = self.create_label("UPC Not Found \n(e.g. 00000000273)",
                                        font=("Arial", 15))

        def on_return(event=None):
            val = entry.get()
            # Another check for item/configuration
            try:
                config_name = self.wrapper.fetch_config_from_tag(val)["name"]
                self.second_page(val, config_name)
            except:
                self.non_happy_first_page()

        self.root.bind("<Return>", on_return)
    
    def second_page(self, upc, config_name):
        self.clear_root()
        
        # Finds user based on open tickets for given item/configuration and creates check in instance
        owner = self.wrapper.fetch_ticket_owner_by_name(config_name)
        if owner != "":
            self.check_in_second_page(upc, config_name, owner)
            return

        label = self.create_label(f"Would you like to Check Out \n{config_name}?", font=("Arial", 20))
        
        # Control flow point function for submission
        def goto_third():
            self.third_page(upc)

        cancel_button = self.create_button("Cancel", self.first_page, apadx=100)
        submit_button = self.create_button("Submit", third, aside="right", apadx=100)
    
    # Create ticket rather than resolve previous tickets (no tickets found in second page)
    def third_page(self, upc):
        self.clear_root()
        
        label = self.create_label(text="Please provide your name and\nan optional description \nbelow.")

        frame = tk.Frame(self.root)
        frame.pack()

        listbox = tk.Listbox(frame)
        listbox.pack(side='left', fill='both', expand=True)
        
        text = tk.Text(frame, height=20, width=50)
        text.pack(side='left', fill='both', expand=True)

        # Current session's active employee list
        items = self.wrapper.fetch_employees()

        # Populate the listbox
        for item in items:
            listbox.insert(tk.END, item)

        def retrieve_input():
            return text.get('1.0', tk.END)




        
        def submit():
            index = listbox.curselection()[0]
            selected = listbox.get(index)

            id = self.wrapper.fetch_id_from_name(selected)
            text = retrieve_input()

            self.wrapper.config_create_ticket(upc, id, text, 466)

            self.final_page(False)

        cancel_button = self.create_button("Cancel", self.first_page, apadx=100)
        submit_button = self.create_button("Submit", submit, aside="right", apadx=100)

    def check_in_second_page(self, upc, config_name, owner):
        self.clear_root()
        label = self.create_label(f"{config_name} is checked out \nby {owner}.\nCheck it in?", font=("Arial", 20))

        def check_in():
            list_of_tickets = self.wrapper.fetch_open_tickets_by_name(config_name)
            
            # Closes active tickets for item/configuration provided, regardless of user
            for ticket in list_of_tickets:
                self.wrapper.close_ticket(ticket["id"])

            self.final_page(True)

        cancel_button = self.create_button("Cancel", self.first_page, apadx=100)
        submit_button = self.create_button("Submit", check_in, aside="right", apadx=100)

    def final_page(self, checked_in):
        self.clear_root()
        if checked_in:
            label = self.create_label("Successful Check In!", font=("Arial", 20))
        else:
            label = self.create_label("Successful Check Out!", font=("Arial", 20))
        
        # Sleep then recursively call and rebuild the initial page
        self.root.after(2500, self.first_page)

    # Widget creation methods

    def create_label(self, text, font=("Arial", 20, "bold"), fg="white", bg="#003C5E", ypad=20, side="top"):
        label = tk.Label(self.root, text=text, fg=fg, bg=bg, font=font)
        label.pack(pady=ypad, side=side)
        return label

    def create_entry(self, font=("Arial", 15)):
        entry = tk.Entry(self.root, font=font)
        entry.pack(pady=20)
        entry.focus()
        return entry

    def create_button(self, text, command, aside="left", apadx=10):
        button = tk.Button(self.root, text=text, command=command)
        button.pack(padx=apadx, side=aside)
        return button

    def clear_root(self):
        for widget in self.root.winfo_children():
            widget.destroy()

# RUN
if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()


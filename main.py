import customtkinter
from tkinter import messagebox
import tkinter
import csv
import datetime

global num_rows
global num_rows2
num_rows = 0
num_rows2 = 0

# calculates the registration number
def reg_no():
    global num_rows # Makes the variable 'num_rows' be affected by any actions in a function and the main program
    for row in open("customers.csv"): # opens the csv file, and the number of rows in the csv are stored in the variable 'num_rows'
        num_rows += 1 # for each row num_rows has 1 added to it

def quote_reg():
    global num_rows2  # Makes the variable 'num_rows' be affected by any actions in a function and the main program
    for row in open("quotes.csv"):  # opens the csv file, and the number of rows in the csv are stored in the variable 'num_rows2'
        num_rows2 += 1  # for each row num_rows has 1 added to it

def add_c():
    global num_rows
    with open("customers.csv", 'a', newline="") as f:
        fieldnames = ['Firstname', 'Surname', 'Town', "Street", "Postcode", "PhoneNumber", 'RegNo']
        writer_module = csv.DictWriter(f, fieldnames=fieldnames)
        fn = e1.get()
        if fn == "":
            messagebox.showwarning("First Name", 'No First Name has been entered!')
        elif any(c.isalpha() for c in fn) != True:
            messagebox.showwarning("First Name", 'The given First name contains numbers!')
        else:
            sn = e2.get()
            if sn == "":
                messagebox.showwarning("Last Name", 'No Last Name has been entered!')
            elif any(c.isalpha() for c in sn) != True:
                messagebox.showwarning("Last Name", 'The given Last Name contains numbers!')
            else:
                town = e3.get()
                if town == "":
                    messagebox.showwarning("Town", 'No Town has been entered!')
                elif any(c.isalpha() for c in sn) != True:
                    messagebox.showwarning("Town", 'The given Town contains numbers!')
                else:
                    street = e4.get()
                    if street == "":
                        messagebox.showwarning("Street", 'No Street has been entered!')
                    else:
                        postcode = e5.get()
                        if postcode == "":
                            messagebox.showwarning("PostCode", 'No PostCode has been entered!')
                        elif len(postcode) != 7:
                            messagebox.showwarning("Postcode", 'The given Postcode does not exist!')
                        else:
                            phone_no = e6.get()
                            if phone_no == "":
                                messagebox.showwarning("Phone Number", 'No Phone Number has been entered!')
                            elif len(phone_no) != 11:
                                messagebox.showwarning("Phone Number", 'Phone Number is not Uk standard!')
                            elif any(c.isdigit() for c in phone_no) != True:
                                messagebox.showwarning("Phone Number", 'Phone Number does not exist!')
                            else:
                                reg_no()
                                regno = num_rows
                                writer_module.writerow({'Firstname': fn, 'Surname': sn, 'Town': town, "Street": street, "Postcode": postcode, "PhoneNumber": phone_no, 'RegNo': regno})

                                num_rows = 0

def add_customer():
    global e1
    global e2
    global e3
    global e4
    global e5
    global e6
    global screen2

    screen2 = customtkinter.CTkToplevel(screen)
    screen2.title("Add Customer:")
    screen2.geometry('880x880')

    screen2.resizable(False,False)

    for row in range(100):
        screen2.grid_rowconfigure(row, minsize=10)
        for col in range(100):
            screen2.grid_columnconfigure(col, minsize=10)

    l1 = customtkinter.CTkLabel(master=screen2, text="FirstName:", width=200, height=30, font=(('arial', 20)), corner_radius=8)
    l1.grid(row=0, column=30, padx=5, pady=5)
    e1 = customtkinter.CTkEntry(master=screen2, placeholder_text="Enter Firstname!", width=200, height=20, font=(('arial', 15)))
    e1.grid(row=1, column=30, padx=5, pady=5)

    l2 = customtkinter.CTkLabel(master=screen2, text="LastName:", width=200, height=30, font=(('arial', 20)), corner_radius=8)
    l2.grid(row=5, column=30, padx=5, pady=5)
    e2 = customtkinter.CTkEntry(master=screen2, placeholder_text="Enter LastName!", width=200, height=20, font=(('arial', 15)))
    e2.grid(row=6, column=30, padx=5, pady=5)

    l3 = customtkinter.CTkLabel(master=screen2, text="Town", width=200, height=30, font=(('arial', 20)),corner_radius=8)
    l3.grid(row=10, column=30, padx=5, pady=5)
    e3 = customtkinter.CTkEntry(master=screen2, placeholder_text="Enter Town!", width=200, height=20,font=(('arial', 15)))
    e3.grid(row=11, column=30, padx=5, pady=5)

    l4 = customtkinter.CTkLabel(master=screen2, text="Street", width=200, height=30, font=(('arial', 20)), corner_radius=8)
    l4.grid(row=15, column=30, padx=5, pady=5)
    e4 = customtkinter.CTkEntry(master=screen2, placeholder_text="Enter Street!", width=200, height=20, font=(('arial', 15)))
    e4.grid(row=16, column=30, padx=5, pady=5)

    l5 = customtkinter.CTkLabel(master=screen2, text="Postcode:", width=200, height=30, font=(('arial', 20)), corner_radius=8)
    l5.grid(row=20, column=30, padx=5, pady=5)
    e5 = customtkinter.CTkEntry(master=screen2, placeholder_text="Enter Postcode!", width=200, height=20, font=(('arial', 15)))
    e5.grid(row=21, column=30, padx=5, pady=5)

    l6 = customtkinter.CTkLabel(master=screen2, text="Telephone NUmber:", width=200, height=30, font=(('arial', 20)), corner_radius=8)
    l6.grid(row=25, column=30, padx=5, pady=5)
    e6 = customtkinter.CTkEntry(master=screen2, placeholder_text="Enter Telephone NUmber!", width=200, height=20, font=(('arial', 15)))
    e6.grid(row=26, column=30, padx=5, pady=5)

    b5 = customtkinter.CTkButton(master=screen2, width=170, height=32, corner_radius=8, text='Add Customer', command=add_c)
    b5.grid(row=35, column=30, padx=5, pady=5)

def add_q_2():
    global num_rows
    with open("customers.csv", 'a', newline="") as f:
        fieldnames = ['Firstname', 'Surname', 'Town', "Street", "Postcode", "PhoneNumber", 'RegNo']
        writer_module = csv.DictWriter(f, fieldnames=fieldnames)

        fn = e7.get()
        if fn == "":
            messagebox.showwarning("First Name", "No First Name has been entered!")
        elif any(c.isalpha() for c in fn) != True:
            messagebox.showwarning("First Name", "The Given First name contains numbers!")
        else:
            sn = e8.get()
            if sn == "":
                messagebox.showwarning("Last Name", "No Last Name has been entered!")
            elif any(c.isalpha() for c in fn) != True:
                messagebox.showwarning("Last Name", "The given Last contains numbers!")
            else:
                town = e9.get()
                if town == "":
                    messagebox.showwarning("Town", "No Town has been entered!")
                elif any(c.isalpha() for c in fn) != True:
                    messagebox.showwarning("Town", "The Town given contains numbers!")
                else:
                    street = e10.get()
                    if street == "":
                        messagebox.showwarning("Street", "No Street has been entered!")
                    else:
                        postcode = e11.get()
                        if postcode == "":
                            messagebox.showwarning("Postcode", "No Postcode has been entered!")
                        elif len(postcode) != 7:
                            messagebox.showwarning("Postcode", "The Postcode does not exist!")
                        else:
                            phone_no = e12.get()
                            if phone_no == "":
                                messagebox.showwarning("Phone Number", "No Phone Number has been entered!")
                            elif len(phone_no) != 11:
                                messagebox.showwarning("Phone Number", 'Phone Number is not Uk standard!')
                            elif any(c.isdigit() for c in phone_no) != True:
                                messagebox.showwarning("Phone Number", 'Phone Number does not exist!')
                            else:
                                reg_no()
                                regno = num_rows

                                writer_module.writerow({'Firstname': fn, 'Surname': sn, 'Town': town, "Street": street, "Postcode": postcode, "PhoneNumber": phone_no, 'RegNo': regno})

                                num_rows = 0

def add_q():
    global num_rows2, num_rows
    with open("quotes.csv", 'a', newline="") as f:
        fieldnames = ['Firstname', 'Surname', 'Length(m)', 'Width(m)', 'Area(m^2)', 'Carpet(Price)', 'Underlay(Type)', 'Underlay(Price)', 'Gripper(m)', 'Gripper(Price)', 'Labour(Hrs)', 'Labour(Price)', "T_Price", 'QuoteNo']
        writer_module = csv.DictWriter(f, fieldnames=fieldnames)
        fn = e7.get()
        if fn == "":
            messagebox.showwarning("First Name", "No First Name has been entered!")
        elif any(c.isalpha() for c in fn) != True:
            messagebox.showwarning("First Name", "The Given First name contains numbers!")
        else:
            sn = e8.get()
            if sn == "":
                messagebox.showwarning("Last Name", "No Last Name has been entered!")
            elif any(c.isalpha() for c in fn) != True:
                messagebox.showwarning("Last Name", "The given Last contains numbers!")
            else:
                l = e13.get()
                if l == "":
                    messagebox.showwarning("Length", "No Length has been entered!")
                elif any(c.isdigit for c in l) != True:
                    messagebox.showwarning("Length", "The given Length must only contain numbers!")
                else:
                    l = float(e13.get())
                    w = e14.get()
                    if w == "":
                        messagebox.showwarning("Width", "No Width has been entered!")
                    elif any(c.isdigit for c in w) != True:
                        messagebox.showwarning("Width", "The given Width must only contain numbers!")
                    else:
                        w = float(e14.get())
                        area = l * w
                        perimeter = (2*l) + (2*w)
                        underlay = e15.get()
                        if any(c.isdigit for c in underlay) != True:
                            messagebox.showwarning("Underlay", "The given Underlay Type must only contain numbers!")
                        else:
                            underlay = int(e15.get())
                            if underlay > 3 :
                                messagebox.showwarning("Underlay", "Underlay does not exist!")
                            elif underlay <= 0:
                                messagebox.showwarning("Underlay", "Underlay does not exist!")
                            else:
                                quote_reg()
                                quote_no = num_rows2

                                if underlay == 1:
                                    p_u = area * 5.99
                                    u_t = "First Step"
                                elif underlay == 2:
                                    p_u = area * 7.99
                                    u_t = "Monarch"
                                elif underlay == 3:
                                    p_u = area * 60
                                    u_t = "Royal"

                                g_p = perimeter * 1.10
                                c_p = area * 22.50
                                l_b = 65
                                l_e = area / 16

                                if l_e <= 1:
                                    l_e = 0

                                l_t = (l_e * 65) + l_b
                                t_c = g_p + c_p + l_b + l_t

                                writer_module.writerow({'Firstname': fn, 'Surname': sn, 'Length(m)': l, 'Width(m)': w, 'Area(m^2)': area, 'Carpet(Price)': c_p, 'Underlay(Type)': u_t, 'Underlay(Price)': p_u, 'Gripper(m)': perimeter, 'Gripper(Price)': g_p, 'Labour(Hrs)': l_e, 'Labour(Price)': l_t, "T_Price": t_c, 'QuoteNo': quote_no})

                                num_rows2=0

                                add_q_2()

def add_quotation():
    global e7, e8, e9, e10, e11, e12, e13, e14, e15

    screen3 = customtkinter.CTkToplevel(screen)
    screen3.title("Add Quote:")
    screen3.geometry('550x550')

    screen3.resizable(False, False)

    for row in range(100):
        screen3.grid_rowconfigure(row, minsize=8)
        for col in range(100):
            screen3.grid_columnconfigure(col, minsize=8)

    l1 = customtkinter.CTkLabel(master=screen3, text="FirstName:", width=200, height=32, font=(('arial', 23)), corner_radius=8)
    l1.grid(row=0, column=5, padx=5, pady=5)
    e7 = customtkinter.CTkEntry(master=screen3, placeholder_text="Enter Firstname!", width=200, height=20, font=(('arial', 15)))
    e7.grid(row=1, column=5, padx=5, pady=5)

    l2 = customtkinter.CTkLabel(master=screen3, text="LastName:", width=200, height=32, font=(('arial', 23)), corner_radius=8)
    l2.grid(row=5, column=5, padx=5, pady=5)
    e8 = customtkinter.CTkEntry(master=screen3, placeholder_text="Enter LastName!", width=200, height=20, font=(('arial', 15)))
    e8.grid(row=6, column=5, padx=5, pady=5)

    l3 = customtkinter.CTkLabel(master=screen3, text="Town", width=200, height=32, font=(('arial', 23)), corner_radius=8)
    l3.grid(row=10, column=5, padx=5, pady=5)
    e9 = customtkinter.CTkEntry(master=screen3, placeholder_text="Enter Town!", width=200, height=20, font=(('arial', 15)))
    e9.grid(row=11, column=5, padx=5, pady=5)

    l4 = customtkinter.CTkLabel(master=screen3, text="Street", width=200, height=32, font=(('arial', 23)), corner_radius=8)
    l4.grid(row=15, column=5, padx=5, pady=5)
    e10 = customtkinter.CTkEntry(master=screen3, placeholder_text="Enter Street!", width=200, height=20, font=(('arial', 15)))
    e10.grid(row=16, column=5, padx=5, pady=5)

    l5 = customtkinter.CTkLabel(master=screen3, text="Postcode", width=200, height=32, font=(('arial', 23)), corner_radius=8)
    l5.grid(row=20, column=5, padx=5, pady=5)
    e11 = customtkinter.CTkEntry(master=screen3, placeholder_text="Enter Postcode!", width=200, height=20, font=(('arial', 15)))
    e11.grid(row=21, column=5, padx=5, pady=5)

    l8 = customtkinter.CTkLabel(master=screen3, text="Telephone Number", width=200, height=32, font=(('arial', 23)), corner_radius=8)
    l8.grid(row=0, column=10, padx=5, pady=5)
    e12 = customtkinter.CTkEntry(master=screen3, placeholder_text="Enter Telephone Number!", width=200, height=20, font=(('arial', 15)))
    e12.grid(row=1, column=10, padx=5, pady=5)

    l9 = customtkinter.CTkLabel(master=screen3, text="Length of room(m)", width=200, height=32, font=(('arial', 23)), corner_radius=8)
    l9.grid(row=5, column=10, padx=5, pady=5)
    e13 = customtkinter.CTkEntry(master=screen3, placeholder_text="Enter Length(m)!", width=200, height=20, font=(('arial', 15)))
    e13.grid(row=6, column=10, padx=5, pady=5)

    l10 = customtkinter.CTkLabel(master=screen3, text="Width of room(m)", width=200, height=32, font=(('arial', 23)), corner_radius=8)
    l10.grid(row=10, column=10, padx=5, pady=5)
    e14 = customtkinter.CTkEntry(master=screen3, placeholder_text="Enter Width(m)!", width=200, height=20, font=(('arial', 15)))
    e14.grid(row=11, column=10, padx=5, pady=5)

    l11 = customtkinter.CTkLabel(master=screen3, text="Underlay Type [1-3]", width=200, height=32, font=(('arial', 23)), corner_radius=8)
    l11.grid(row=15, column=10, padx=5, pady=5)
    e15 = customtkinter.CTkEntry(master=screen3, placeholder_text="Enter Underlay: [1-3]!", width=200, height=20, font=(('arial', 15)))
    e15.grid(row=16, column=10, padx=5, pady=5)

    b6 = customtkinter.CTkButton(master=screen3, width=170, height=32, corner_radius=8, text='Add Quote', command=add_q)
    b6.grid(row=21, column=10, padx=5, pady=5)

def view():
    global textbox1
    with open("quotes.csv") as f:
        fieldnames = ['Firstname', 'Surname', 'Length(m)', 'Width(m)', 'Area(m^2)', 'Carpet(Price)', 'Underlay(Type)', 'Underlay(Price)', 'Gripper(m)', 'Gripper(Price)', 'Labour(Hrs)', 'Labour(Price)', "T_Price", 'QuoteNo']
        reader_module = csv.DictReader(f, fieldnames=fieldnames)

        x = e18.get()
        if x == "":
            messagebox.showwarning("First Name", 'No First Name has been Entered!')
        elif any(c.isalpha() for c in x) != True:
            messagebox.showwarning("First Name", 'The given First Name contains numbers!')
        else:
            y = e19.get()
            if y == "":
                messagebox.showwarning("Last Name", 'No Last Name has been Entered!')
            elif any(c.isalpha() for c in x) != True:
                messagebox.showwarning("Last Name", 'The given Last Name contains numbers!')
            else:
                for row in reader_module:
                    if row['Firstname'] == x and row['Surname'] == y:
                        a = row
                        textbox1.configure(state="normal")
                        textbox1.delete("1.0", "end")
                        for key, value in a.items():
                            textbox1.insert("end", f'{key}: {value}\n')

        textbox1.configure(state="disabled")

def view_c():
    global textbox1, e18, e19

    screen5 = customtkinter.CTkToplevel(screen)
    screen5.title("Customer View")
    screen5.geometry("635x750")

    screen5.resizable(False, False)

    for row in range(100):
        screen5.grid_rowconfigure(row, minsize=8)
        for col in range(100):
            screen5.grid_columnconfigure(col, minsize=8)

    with open("customers.csv") as f:
        fieldnames = ['Firstname', 'Surname', 'Town', "Street", "Postcode", "PhoneNumber", 'RegNo']
        reader_module = csv.DictReader(f, fieldnames=fieldnames)

        l1 = customtkinter.CTkLabel(master=screen5, text="Customers View", width=100, height=32, font=(('arial', 26)),corner_radius=8)
        l1.grid(row=0, column=5, padx=3, pady=3)

        textbox1 = customtkinter.CTkTextbox(master=screen5, height=550, width=550)
        textbox1.grid(row=3, column=5)

        e18 = customtkinter.CTkEntry(master=screen5, placeholder_text="Enter Customer Name!", width=200, height=20, font=(('arial', 15)))
        e18.grid(row=7, column=5, padx=5, pady=5)

        e19 = customtkinter.CTkEntry(master=screen5, placeholder_text="Enter Customer surname!", width=200, height=20, font=(('arial', 15)))
        e19.grid(row=8, column=5, padx=5, pady=5)

        b1 = customtkinter.CTkButton(master=screen5, width=130, height=32, corner_radius=8, text="view", command=view)
        b1.grid(row=10, column=5, padx=5, pady=5)

def rm_customer():
    b = str(e20.get())
    c = str(e21.get())

    with open("customers.csv", "r") as f, open("quotes.csv", "r") as x:
        fieldnames1 = ['Firstname', 'Surname', 'Town', "Street", "Postcode", "PhoneNumber", 'RegNo']
        fieldnames2 = ['Firstname', 'Surname', 'Length(m)', 'Width(m)', 'Area(m^2)', 'Carpet(Price)', 'Underlay(Type)', 'Underlay(Price)', 'Gripper(m)', 'Gripper(Price)', 'Labour(Hrs)', 'Labour(Price)', "T_Price", 'QuoteNo']
        reader_mod1 = csv.DictReader(f, fieldnames1)
        reader_mod2 = csv.DictReader(x, fieldnames=fieldnames2)

        data1 = list(reader_mod1)
        data2 = list(reader_mod2)

        for row in data1:
            if row["Firstname"] == b and row["Surname"] == c:
                data1.remove(row)
                with open("customers.csv", 'w', newline="") as fx:
                    writer_mod1 = csv.DictWriter(fx, fieldnames=fieldnames1)
                    writer_mod1.writerows(data1)

        for row in data2:
            if row["Firstname"] == b and row["Surname"] == c:
                data2.remove(row)
                with open("quotes.csv", 'w', newline="") as fz:
                    writer_mod1 = csv.DictWriter(fz, fieldnames=fieldnames1)
                    writer_mod1.writerows(data2)


def remove_customer():
    global e20, e21
    screen6 = customtkinter.CTkToplevel(screen)
    screen6.title("Remove Customer")
    screen6.geometry("300x200")

    screen6.resizable(False, False)

    for row in range(100):
        screen6.grid_rowconfigure(row, minsize=8)
        for col in range(100):
            screen6.grid_columnconfigure(col, minsize=8)

    l1 = customtkinter.CTkLabel(master=screen6, text="Remove Customer", width=100, height=32, font=(('arial', 26)), corner_radius=8)
    l1.grid(row=0, column=5, padx=3, pady=3)

    e20 = customtkinter.CTkEntry(master=screen6, placeholder_text="Enter First Name!", width=200, height=20, font=(('arial', 15)))
    e20.grid(row=5, column=5, padx=5, pady=5)

    e21 = customtkinter.CTkEntry(master=screen6, placeholder_text="Enter Last Name!", width=200, height=20, font=(('arial', 15)))
    e21.grid(row=7, column=5, padx=5, pady=5)

    b1 = customtkinter.CTkButton(master=screen6, width=130, height=32, corner_radius=8, text="Remove", command=rm_customer)
    b1.grid(row=9, column=5, padx=5, pady=5)

def list_customers():

    screen4 = customtkinter.CTkToplevel(screen)
    screen4.title("Customer List:")
    screen4.geometry('900x885')

    screen4.resizable(False, False)

    for row in range(100):
        screen4.grid_rowconfigure(row, minsize=8)
        for col in range(100):
            screen4.grid_columnconfigure(col, minsize=8)

    with open("customers.csv") as f:
        fieldnames = ['Firstname', 'Surname', 'Town', "Street", "Postcode", "PhoneNumber", 'RegNo']
        reader_module = csv.DictReader(f, fieldnames=fieldnames)

        l1 = customtkinter.CTkLabel(master=screen4, text="Customers List", width=150, height=32, font=(('arial', 45)), corner_radius=8)
        l1.grid(row=1, column=0, padx=3, pady=3)

        textbox = customtkinter.CTkTextbox(master=screen4, height=750, width=750)
        textbox.grid(row=4, column=0, padx=1, pady=1)

        b6 = customtkinter.CTkButton(master=screen4, text="View Customer", width=130, height=32, corner_radius=8, command=view_c)
        b6.grid(row=0, column=2, padx=1, pady=1)

        b7 = customtkinter.CTkButton(master=screen4, text="Add New Customer", width=130, height=32, corner_radius=8, command=add_customer)
        b7.grid(row=1, column=2)

        b8 = customtkinter.CTkButton(master=screen4, text="Delete Customer", width=130, height=32, corner_radius=8, command=remove_customer)
        b8.grid(row=2, column=2)

        for row in reader_module:
            textbox.insert('1.0', f'{row}\n\n')

        with open('customers.csv', 'r') as f:
            reader = csv.reader(f)
            csv_data = "\n".join([",".join(row) for row in reader])
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("end", f'{csv_data}\n')
        textbox.configure(state="disabled")

def list_quotations():
    screen7 = customtkinter.CTkToplevel(screen)
    screen7.title("Quotations List:")
    screen7.geometry('1000x600')

    screen7.resizable(False, False)

    for row in range(100):
        screen7.grid_rowconfigure(row, minsize=8)
        for col in range(100):
            screen7.grid_columnconfigure(col, minsize=8)

    with open("quotes.csv") as f:
        fieldnames = ['Firstname', 'Surname', 'Town', "Street", "Postcode", "PhoneNumber", 'RegNo']
        reader_module = csv.DictReader(f, fieldnames=fieldnames)

        l1 = customtkinter.CTkLabel(master=screen7, text="Quotations List", width=150, height=32, font=(('arial', 45)), corner_radius=8)
        l1.grid(row=1, column=0, padx=3, pady=3)

        textbox = customtkinter.CTkTextbox(master=screen7, height=750, width=990)
        textbox.grid(row=4, column=0, padx=1, pady=1)

        for row in reader_module:
            textbox.insert('1.0', f'{row}\n\n')

        with open('quotes.csv', 'r') as f:
            reader = csv.reader(f)
            csv_data = "\n".join([",".join(row) for row in reader])
        textbox.configure(state="normal")
        textbox.delete("1.0", "end")
        textbox.insert("end", f'{csv_data}\n')
        textbox.configure(state="disabled")

def main_screen():
    # Make main window
    global screen
    screen = customtkinter.CTk()
    screen.title("System:")
    screen.geometry(f'{180}x{205}')

    screen.resizable(False, False)

    customtkinter.set_appearance_mode("dark")
    customtkinter.set_default_color_theme("green")

    l1 = customtkinter.CTkLabel(master=screen, text="Management System:", width=160, height=32, font=(('arial', 16)))
    l1.grid(row=0, column=0)

    b1 = customtkinter.CTkButton(master=screen, width=170, height=32, corner_radius=8, text='Add Customer', command=add_customer)
    b1.grid(row=1, column=0, padx=5, pady=5)

    b2 = customtkinter.CTkButton(master=screen, width=170, height=32, corner_radius=8, text="Add Quotation", command=add_quotation)
    b2.grid(row=2, column=0, padx=5, pady=5)

    b3 = customtkinter.CTkButton(master=screen, width=170, height=32, corner_radius=8, text="List Customer", command=list_customers)
    b3.grid(row=3, column=0, padx=5, pady=5)

    b4 = customtkinter.CTkButton(master=screen, width=170, height=32, corner_radius=8, text="List Quotation",command=list_quotations)
    b4.grid(row=4, column=0, padx=5, pady=5)

    screen.mainloop()

main_screen()
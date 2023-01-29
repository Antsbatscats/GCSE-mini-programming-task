# Setup system:
import csv

# Adding a new member
def setup():
    with open('quotes.csv', 'w', newline='') as f:
        write_module = csv.writer(f)
        write_module.writerow(['Firstname', 'Surname', 'Length(m)', 'Width(m)', 'Area(m^2)', 'Carpet(Price)', 'Underlay(Type)', 'Underlay(Price)', 'Gripper(m)', 'Gripper(Price)', 'Labour(Hrs)', 'Labour(Price)', "T_Price", 'QuoteNo'])

setup()
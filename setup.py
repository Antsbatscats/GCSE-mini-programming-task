# Setup system:
import csv

# Adding a new member
def setup():
    with open('customers.csv', 'w', newline='') as f:
        write_module = csv.writer(f)
        write_module.writerow(['Firstname', 'Surname', 'Town', "Street", "Postcode", "PhoneNumber", 'RegNo'])

setup()
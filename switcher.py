# Switcher for implementing switch case options
def employee_details(ID):
    switcher = {
        "1004": "Employee Name: MD. Mehrab",
        "1009": "Employee Name: Mita Rahman",  
        "1010": "Employee Name: Dr. John Roberts",
    }
    return switcher.get(ID, "No info for this employee ID")

ID = input("Enter the employee ID: ")
print(employee_details(ID))

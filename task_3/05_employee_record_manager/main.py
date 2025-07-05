from employee_utils import load_employees, save_employees
import os

class Employee:
    def __init__(self, name, emp_id, department, salary):
        self.name = name
        self.emp_id = emp_id
        self.department = department
        self.salary = float(salary)

    def to_dict(self):
        return {
            "name": self.name,
            "emp_id": self.emp_id,
            "department": self.department,
            "salary": self.salary
        }

    @staticmethod
    def from_dict(data):
        return Employee(data['name'], data['emp_id'], data['department'], data['salary'])

class EmployeeManager:
    def __init__(self, filename="employees.json"):
        current_dir = os.path.dirname(__file__)
        self.filename = os.path.join(current_dir, filename)
        self.employees = [Employee.from_dict(e) for e in load_employees(self.filename)]

    def add_employee(self):
        name = input("Enter employee name: ")
        emp_id = input("Enter employee ID: ")
        department = input("Enter department: ")
        try:
            salary = float(input("Enter salary: "))
            emp = Employee(name, emp_id, department, salary)
            self.employees.append(emp)
            print("Employee added successfully.\n")
        except ValueError:
            print("Invalid salary input.\n")

    def view_employees(self):
        if not self.employees:
            print("No employee records available.\n")
            return
        print("--- Employee Records ---")
        for e in self.employees:
            print(f"ID: {e.emp_id}\nName: {e.name}\nDepartment: {e.department}\nSalary: ₦{e.salary:.2f}\n")

    def search_employee(self):
        search_id = input("Enter employee ID to search: ")
        for e in self.employees:
            if e.emp_id == search_id:
                print(f"Found Employee:\nID: {e.emp_id}\nName: {e.name}\nDepartment: {e.department}\nSalary: ₦{e.salary:.2f}\n")
                return
        print("Employee not found.\n")

    def save_to_file(self):
        save_employees(self.filename, [e.to_dict() for e in self.employees])
        print("Employee records saved.\n")

    def load_from_file(self):
        self.employees = [Employee.from_dict(e) for e in load_employees(self.filename)]
        print("Employee records loaded.\n")

# --- Main Menu ---
manager = EmployeeManager()

while True:
    print("---------------------------------------------")
    print("         Employee Record Manager             ")
    print("---------------------------------------------")
    print("           Welcome to Employee Manager!      ")
    print("             Choose an option:               ")  
    print("---------------------------------------------")
    print("            1. Add Employee                  ")
    print("            2. View All Employees            ")
    print("            3. Search by ID                  ")
    print("            4. Save to File                  ")
    print("            5. Load from File                ")
    print("            6. Exit                          ")
    print("---------------------------------------------")

    choice = input("\nEnter your choice: ")

    if choice == "1":
        manager.add_employee()
    elif choice == "2":
        manager.view_employees()
    elif choice == "3":
        manager.search_employee()
    elif choice == "4":
        manager.save_to_file()
    elif choice == "5":
        manager.load_from_file()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number.\n")

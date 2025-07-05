import uuid
import os
from delivery_utils import save_packages, load_packages

class Package:
    def __init__(self, sender, recipient, status="Pending"):
        self.id = str(uuid.uuid4())
        self.sender = sender
        self.recipient = recipient
        self.status = status

    def to_dict(self):
        return {
            "id": self.id,
            "sender": self.sender,
            "recipient": self.recipient,
            "status": self.status
        }

    @staticmethod
    def from_dict(data):
        package = Package(data['sender'], data['recipient'], data['status'])
        package.id = data['id']
        return package

class PackageSystem:
    def __init__(self, filename="packages.json"):
        current_dir = os.path.dirname(__file__)
        self.filename = os.path.join(current_dir, filename)
        self.packages = [Package.from_dict(p) for p in load_packages(self.filename)]

    def register_package(self):
        sender = input("Enter sender name: ")
        recipient = input("Enter recipient name: ")
        package = Package(sender, recipient)
        self.packages.append(package)
        print(f"Package registered with ID: {package.id}\n")

    def mark_delivered(self):
        pid = input("Enter package ID to mark as delivered: ")
        for pkg in self.packages:
            if pkg.id == pid:
                pkg.status = "Delivered"
                print("Package marked as delivered.\n")
                return
        print("Package not found.\n")

    def view_packages(self):
        if not self.packages:
            print("No packages registered.\n")
            return
        print("--- Package List ---")
        for pkg in self.packages:
            print(f"ID: {pkg.id}\nSender: {pkg.sender}\nRecipient: {pkg.recipient}\nStatus: {pkg.status}\n")

    def save(self):
        save_packages(self.filename, [p.to_dict() for p in self.packages])
        print("Packages saved to file.\n")

    def load(self):
        self.packages = [Package.from_dict(p) for p in load_packages(self.filename)]
        print("Packages loaded from file.\n")

# --- Main Menu ---
system = PackageSystem()

while True:
    print("---------------------------------------------")
    print("           Package Delivery System           ")
    print("---------------------------------------------")
    print("   Welcome to the Package Delivery System    ")
    print("            Choose an option:                ")
    print("---------------------------------------------")
    print("           1. Register a Package             ")
    print("           2. Mark Package as Delivered      ")
    print("           3. View All Packages              ")
    print("           4. Save to File                   ")
    print("           5. Load from File                 ")
    print("           6. Exit                           ")
    print("---------------------------------------------")

    choice = input("\nEnter your choice: ")

    if choice == "1": system.register_package()
    elif choice == "2": system.mark_delivered()
    elif choice == "3": system.view_packages()
    elif choice == "4": system.save()
    elif choice == "5": system.load()
    elif choice == "6":
        print("Goodbye!")
        break
    else:
        print("Invalid choice. Please choose a number.\n")
import os
from datetime import datetime
from diary_tools import load_entries, save_entries

class DiaryEntry:
    def __init__(self, title, content):
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        self.title = title
        self.content = content

    def to_dict(self):
        return {
            "date": self.date,
            "title": self.title,
            "content": self.content
        }

    @staticmethod
    def from_dict(data):
        entry = DiaryEntry(data['title'], data['content'])
        entry.date = data['date']
        return entry

class Diary:
    def __init__(self, filename="diary.json"):
        current_dir = os.path.dirname(__file__)
        self.filename = os.path.join(current_dir, filename)
        self.entries = [DiaryEntry.from_dict(e) for e in load_entries(self.filename)]

    def add_entry(self):
        title = input("Enter title: ")
        content = input("Enter content: ")
        entry = DiaryEntry(title, content)
        self.entries.append(entry)
        print("Entry added.\n")

    def view_entries(self):
        if not self.entries:
            print("No diary entries found.\n")
            return
        print("--- Diary Entries ---")
        for entry in self.entries:
            print(f"Date: {entry.date}\nTitle: {entry.title}\nContent: {entry.content}\n")

    def search_entries(self):
        keyword = input("Enter date or title to search: ").lower()
        found = False
        for entry in self.entries:
            if keyword in entry.date.lower() or keyword in entry.title.lower():
                print(f"Date: {entry.date}\nTitle: {entry.title}\nContent: {entry.content}\n")
                found = True
        if not found:
            print("No matching entry found.\n")

    def save(self):
        save_entries(self.filename, [e.to_dict() for e in self.entries])
        print("Diary saved. Goodbye!")

# --- Main Menu ---
diary = Diary()

while True:
    print("---------------------------------------------")
    print("            Personal Diary App               ")
    print("---------------------------------------------")
    print("           Welcome to Your Diary!            ")
    print("             Choose an option:               ")
    print("---------------------------------------------")
    print("             1. Add Entry                    ")
    print("             2. View All Entries             ")
    print("             3. Search by Date or Title      ")
    print("             4. Save & Exit                  ")
    print("---------------------------------------------")

    choice = input("\nEnter your choice: ")

    if choice == "1": diary.add_entry()
    elif choice == "2": diary.view_entries()
    elif choice == "3": diary.search_entries()
    elif choice == "4":
        diary.save()
        break
    else:
         print("Invalid choice. Please choose a number.\n")


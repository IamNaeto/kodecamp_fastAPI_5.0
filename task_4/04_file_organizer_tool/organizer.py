import os
import shutil

# File type mappings
FILE_TYPES = {
    'Images': ['.jpg', '.jpeg', '.png', '.gif'],
    'Documents': ['.pdf', '.docx', '.doc', '.txt'],
    'Videos': ['.mp4', '.mov', '.avi'],
    'Music': ['.mp3', '.wav'],
    'Archives': ['.zip', '.rar'],
    'Others': []
}

def get_category(extension):
    for category, extensions in FILE_TYPES.items():
        if extension.lower() in extensions:
            return category
    return 'Others'

def organize_files(folder_path):
    try:
        if not os.path.exists(folder_path):
            print("Folder does not exist.")
            return

        files = os.listdir(folder_path)
        if not files:
            print("The folder is empty.")
            return

        for file_name in files:
            full_path = os.path.join(folder_path, file_name)
            if os.path.isfile(full_path):
                ext = os.path.splitext(file_name)[1]
                category = get_category(ext)
                category_folder = os.path.join(folder_path, category)

                os.makedirs(category_folder, exist_ok=True)
                target_path = os.path.join(category_folder, file_name)

                # Move the file
                shutil.move(full_path, target_path)
                print(f"Moved '{file_name}' to '{category}/'")

        print("\n Organizing complete.")

    except Exception as e:
        print(f"Error: {e}")

def main():
    folder_path = input("Enter the path to the folder you want to organize: ").strip()
    organize_files(folder_path)

if __name__ == "__main__":
    main()

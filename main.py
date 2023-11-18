import shutil
import os
from datetime import datetime, timedelta

SOURCE_DIRECTORY = r"C:\Users\abdoe\OneDrive\Desktop\repo"
DESTINATION_DIRECTORY = r"C:\Users\abdoe\OneDrive\Desktop\repo"

created_folders = []  # List to store created folder names


def move():
    # Move the source folder to the destination folder
    shutil.move(SOURCE_DIRECTORY, DESTINATION_DIRECTORY)
    print('Folder moved successfully.')


def move_files_except_created_folders(returned_current_month):
    source_directory = DESTINATION_DIRECTORY
    destination_directory = os.path.join(DESTINATION_DIRECTORY, returned_current_month)

    for item in os.listdir(source_directory):
        item_path = os.path.join(source_directory, item)

        # Check if the item is a file or directory and not in created_folders
        if os.path.exists(item_path) and item not in created_folders:
            destination_path = os.path.join(destination_directory, item)
            os.rename(item_path, destination_path)

def create_folders():
    # Create folders with names like "next month-all days in the month"
    today = datetime.now()
    next_month = today + timedelta(days=30)

    next_month_number = next_month.month
    last_day_of_next_month = (next_month.replace(day=1) + timedelta(days=32)).replace(day=1) - timedelta(days=1)

    for day in range(1, last_day_of_next_month.day + 1):
        folder_name = f"{next_month_number}-{day}"
        created_folders.append(folder_name)

        folder_path = os.path.join(DESTINATION_DIRECTORY, folder_name)

        # Check if the folder already exists
        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        else:
            print(f"Folder '{folder_name}' already exists.")


def create_previous_month(months_map):
    today = datetime.now()
    current_month_key = today.strftime("%b")
    current_month = "شهر " + months_map[current_month_key]
    created_folders.append(current_month)

    destination_directory = os.path.join(DESTINATION_DIRECTORY, current_month)

    if not os.path.exists(destination_directory):
        os.makedirs(destination_directory)

    return current_month  # Return the current_month value


def main():
    months_map = {
        "Jan": "يناير",
        "Feb": "فبراير",
        "Mar": "مارس",
        "Apr": "أبريل",
        "May": "مايو",
        "Jun": "يونيو",
        "Jul": "يوليو",
        "Aug": "أغسطس",
        "Sep": "سبتمبر",
        "Oct": "أكتوبر",
        "Nov": "نوفمبر",
        "Dec": "ديسمبر"
    }

    create_folders()
    create_previous_month(months_map)
    print(f"Folders created successfully in '{DESTINATION_DIRECTORY}'")
    # Now, the created_folders list contains the names of the folders created by the functions.

    print("Created Folders:", created_folders)

    returned_current_month = create_previous_month(months_map)
    print("Returned Current Month:", returned_current_month)
    move_files_except_created_folders(returned_current_month)


if __name__ == "__main__":
    main()


import os
import shutil


def organize_files(folder_path):
    """Organize files by their file extensions."""

    if not os.path.isdir(folder_path):
        print("Error: Folder does not exist.")
        return

    categories = {
        "Images": [".jpg", ".jpeg", ".png", ".gif"],
        "Documents": [".pdf", ".doc", ".docx", ".txt"],
        "Spreadsheets": [".csv", ".xls", ".xlsx"],
        "Python_Files": [".py"],
    }

    moved_count = 0

    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)

        if not os.path.isfile(file_path):
            continue

        extension = os.path.splitext(filename)[1].lower()
        category = "Others"

        for folder_name, extensions in categories.items():
            if extension in extensions:
                category = folder_name
                break

        destination_folder = os.path.join(
            folder_path, category
        )
        os.makedirs(destination_folder, exist_ok=True)

        destination_path = os.path.join(
            destination_folder, filename
        )

        try:
            shutil.move(file_path, destination_path)
            moved_count += 1
            print("Organized: {}".format(filename))
        except OSError as error:
            print("Could not move {}: {}".format(filename, error))

    print("\nFile organization completed!")
    print("Total files moved: {}".format(moved_count))


def main():
    print("===== PYTHON FILE ORGANIZER =====")
    folder_path = input(
        "Enter the folder path to organize: "
    ).strip().strip('"')

    organize_files(folder_path)


if __name__ == "__main__":
    main()

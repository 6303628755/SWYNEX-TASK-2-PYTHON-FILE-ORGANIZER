# Python File Organizer Automation Tool

## Project Overview
This project is a Python automation tool that organizes files into separate folders based on their file extensions. It helps reduce manual work and keeps folders organized.

## Features
- Automatically organizes files by extension.
- Creates folders for Images, Documents, Spreadsheets, Python_Files, and Others.
- Supports common file types such as JPG, PDF, TXT, CSV, XLSX, and PY.
- Displays the number of files moved.
- Handles invalid folder paths.

## Technologies Used
- Python
- os module
- shutil module

## How to Run

1. Install Python on your computer.
2. Download or clone this project.
3. Open the project folder in VS Code.
4. Open the terminal.
5. Run the following command:

```bash
python main.py
```

6. Enter the full path of the folder you want to organize when prompted.

## Example

```text
===== PYTHON FILE ORGANIZER =====
Enter the folder path to organize: C:\Users\User\Desktop\Task2_RealTest

File organization completed!
Total files moved: 7
```

## Project Structure

```text
Swynex_Task2/
├── main.py
└── README.md
```

## Learning Outcome
This project demonstrates Python file handling, automation, directory management, and exception handling.
## Sample Output

```text
===== PYTHON FILE ORGANIZER =====
Enter the folder path to organize: C:\Users\User\Desktop\Task2_RealTest

Organized: cleaned_student_data.csv
Organized: correlation_matrix.csv
Organized: eda_summary.csv
Organized: student_data_cleaning.py
Organized: student_performance_eda_task_2 - Copy.py
Organized: student_performance_eda_task_2.py
Organized: sushma_k_resume.pdf

File organization completed!
Total files moved: 7
```

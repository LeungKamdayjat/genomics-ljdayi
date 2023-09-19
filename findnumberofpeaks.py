
#this code is to find how many of peaks in bed files within a folder. 
import os

def count_lines_in_file(file_path):
    with open(file_path, 'r', encoding='utf-8', errors='ignore') as f:
        return sum(1 for line in f)

def main():
    folder_path = input("Enter the path of the folder: ")

    # Ensure the provided path is a directory
    if not os.path.isdir(folder_path):
        print(f"'{folder_path}' is not a valid directory.")
        return

    # Loop through each file in the directory and count the lines
    for filename in os.listdir(folder_path):
        file_path = os.path.join(folder_path, filename)
        if os.path.isfile(file_path):
            try:
                line_count = count_lines_in_file(file_path)
                print(f"'{filename}' has {line_count} lines.")
            except Exception as e:
                print(f"Error reading '{filename}': {e}")

if __name__ == "__main__":
    main()

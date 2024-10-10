import os
import sys
import zipfile
from pathlib import Path

def zip_directory(folder_path):
    """
    Zip the contents of a specified directory.

    :param folder_path: Path to the folder to be zipped.
    """
    zip_path = f"{folder_path}.zip"
    with zipfile.ZipFile(zip_path, 'w', zipfile.ZIP_DEFLATED) as zipf:
        for root, dirs, files in os.walk(folder_path):
            for file in files:
                file_path = os.path.join(root, file)
                arcname = os.path.relpath(file_path, start=folder_path)
                zipf.write(file_path, arcname=arcname)
    print(f"Directory {folder_path} zipped successfully into {zip_path}")

def unzip_directory(zip_path):
    """
    Unzip the contents of a specified zip file.

    :param zip_path: Path to the zip file to be unzipped.
    """
    extract_to = zip_path.replace('.zip', '')
    with zipfile.ZipFile(zip_path, 'r') as zipf:
        zipf.extractall(extract_to)
    print(f"Zip file {zip_path} extracted successfully into {extract_to}")

def main():
    if len(sys.argv) != 3:
        print("Usage: python zip_unzip_directory.py <zip|unzip> <path>")
        sys.exit(1)
    
    operation = sys.argv[1].lower()
    path = sys.argv[2]

    if operation == 'zip':
        if not os.path.isdir(path):
            print(f"Error: The path {path} is not a valid directory.")
            sys.exit(1)
        zip_directory(path)
    elif operation == 'unzip':
        if not os.path.isfile(path) or not path.endswith('.zip'):
            print(f"Error: The path {path} is not a valid zip file.")
            sys.exit(1)
        unzip_directory(path)
    else:
        print("Error: Invalid operation. Use 'zip' or 'unzip'.")
        sys.exit(1)

if __name__ == '__main__':
    main()

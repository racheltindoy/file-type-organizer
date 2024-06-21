import os
import shutil

# Initial directory to process (replace with your actual directory)
dir_path = "./"

# Loop through all files and subdirectories in the directory
for filename in os.listdir(dir_path):

    # Get the full path of the current item
    full_path = os.path.join(dir_path, filename)

    # Separate filename and extension
    file_path, file_extension = os.path.splitext(full_path)

    # Extract the extension without the leading dot (e.g., ".jpg" becomes "jpg")
    folder_name = file_extension[1:]

    # Construct the new folder path based on the extension
    new_folder_path = os.path.join(dir_path, folder_name)

    # Create the folder if it doesn't exist
    if not os.path.exists(new_folder_path):
        os.mkdir(new_folder_path)
        print(f"Created folder: {new_folder_path}")  # Optional: Print success message

    # Check if it's a file (not a directory)
    if not os.path.isdir(full_path):
        # Move the file to the newly created folder
        shutil.move(full_path, new_folder_path)
        print(f"Moved {filename} to {folder_name} folder")  # Optional: Print success message

print("\nAll files have been successfully organized.")
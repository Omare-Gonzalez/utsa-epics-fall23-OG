import os
import shutil

folder_path = "C:\\Users\\gomar\\OneDrive\\Desktop\\School"  # Replace with your folder path
destination_folder = "fodler"  # Replace with the destination folder name

# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# Filter out only image files (you can adjust the extension as needed)
image_files = [file for file in file_list if file.lower().endswith(".png")]

# Sort the image files to maintain the original order
image_files.sort()

# Create destination folders if they don't exist
for folder_index in range(1, 6):
    folder_name = f"{destination_folder}_{folder_index}"
    os.makedirs(os.path.join(folder_path, folder_name), exist_ok=True)

# Move images to the destination folders
images_per_folder = 10
for folder_index in range(1, 6):
    folder_name = f"{destination_folder}_{folder_index}"
    for i in range(images_per_folder):
        source_image = image_files.pop(0)
        source_path = os.path.join(folder_path, source_image)
        destination_path = os.path.join(folder_path, folder_name, source_image)
        shutil.move(source_path, destination_path)
        print(f"Moved {source_image} to {folder_name}")

print("Image distribution complete.")

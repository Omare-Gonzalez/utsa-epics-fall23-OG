import os

folder_path = "C:\\Users\\gomar\\OneDrive\\Desktop\\School"  # Replace with your folder path
new_name_prefix = "Omar"         # Prefix for the new names
extension = ".png"                # Image extension (change according to your images)

# Get a list of all files in the folder
file_list = os.listdir(folder_path)

# Filter out only image files based on the extension
image_files = [file for file in file_list if file.lower().endswith(extension)]

# Sort the image files to maintain the original order
image_files.sort()

# Iterate through the image files and rename them sequentially
for index, old_name in enumerate(image_files, start=1):
    new_name = f"{new_name_prefix}_{index:03d}{extension}"
    old_path = os.path.join(folder_path, old_name)
    new_path = os.path.join(folder_path, new_name)
    os.rename(old_path, new_path)
    print(f"Renamed {old_name} to {new_name}")

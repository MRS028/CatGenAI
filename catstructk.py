import os

MALE_FOLDER = r"D:\ML-AI\AI-ML Project\Cat Gender Classification Dataset\Male"

# List all files in the folder
files = [f for f in os.listdir(MALE_FOLDER) if os.path.isfile(os.path.join(MALE_FOLDER, f))]

# Sort files for consistent numbering
files.sort()

for idx, filename in enumerate(files, start=1):
    # Get file extension
    ext = os.path.splitext(filename)[1]
    # Create new filename with leading zeros
    new_name = f"Male_{idx:03d}{ext}"
    # Full paths
    src = os.path.join(MALE_FOLDER, filename)
    dst = os.path.join(MALE_FOLDER, new_name)
    # Rename file
    os.rename(src, dst)
    print(f"Renamed: {filename} -> {new_name}")

print("Renaming complete.") 


# --- Female folder renaming ---
FEMALE_FOLDER = r"D:\ML-AI\AI-ML Project\Cat Gender Classification Dataset\Female"

files = [f for f in os.listdir(FEMALE_FOLDER) if os.path.isfile(os.path.join(FEMALE_FOLDER, f))]
files.sort()

for idx, filename in enumerate(files, start=1):
    ext = os.path.splitext(filename)[1]
    new_name = f"Female_{idx:03d}{ext}"
    src = os.path.join(FEMALE_FOLDER, filename)
    dst = os.path.join(FEMALE_FOLDER, new_name)
    if os.path.exists(dst):
        print(f"Skipped: {new_name} already exists.")
        continue
    os.rename(src, dst)
    print(f"Renamed: {filename} -> {new_name}")

print("Female folder renaming complete.")
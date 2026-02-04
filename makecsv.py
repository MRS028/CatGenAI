import os
import csv

BASE_DIR = r"D:\ML-AI\AI-ML Project\Cat Gender Classification Dataset"
CSV_PATH = r"D:\ML-AI\AI-ML Project\metadata.csv"

rows = []

# Male = 1
male_dir = os.path.join(BASE_DIR, "Male")
male_imgs = [img for img in os.listdir(male_dir) if img.lower().endswith((".jpg", ".png", ".jpeg"))]
male_imgs.sort()
for img in male_imgs:
    rows.append([f"Male/{img}", 1])

# Female = 0
female_dir = os.path.join(BASE_DIR, "Female")
female_imgs = [img for img in os.listdir(female_dir) if img.lower().endswith((".jpg", ".png", ".jpeg"))]
female_imgs.sort()
for img in female_imgs:
    rows.append([f"Female/{img}", 0])

# Write CSV
with open(CSV_PATH, "w", newline="", encoding="utf-8") as f:
    writer = csv.writer(f)
    writer.writerow(["image_path", "label"])
    writer.writerows(rows)

print(f"✅ CSV created: {CSV_PATH}")
print(f"Total samples: {len(rows)}")
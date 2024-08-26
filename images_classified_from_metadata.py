import os
import pandas as pd
import shutil

csv_file_path = '/Users/aryanneizehbaz/Aryan8221/coding_projects/ProtoPNet/HAM10000/HAM10000_metadata.csv'
image_dir = '/Users/aryanneizehbaz/Aryan8221/coding_projects/ProtoPNet/HAM10000'
output_dir = '/Users/aryanneizehbaz/Aryan8221/coding_projects/ProtoPNet/HAM10000_classified'

df = pd.read_csv(csv_file_path)

os.makedirs(output_dir, exist_ok=True)

unique_dx = df['dx'].unique()

for dx in unique_dx:
    dx_folder_path = os.path.join(output_dir, dx)
    os.makedirs(dx_folder_path, exist_ok=True)

for index, row in df.iterrows():
    image_id = row['image_id']
    dx = row['dx']

    source_path = os.path.join(image_dir, f"{image_id}.jpg")
    destination_path = os.path.join(output_dir, dx, f"{image_id}.jpg")

    if os.path.exists(source_path):
        shutil.copy(source_path, destination_path)
    else:
        print(f"Image {source_path} not found.")

print("Images have been organized into folders based on dx values.")

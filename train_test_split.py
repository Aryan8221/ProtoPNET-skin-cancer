import os
import shutil
from sklearn.model_selection import train_test_split

input_dir = 'HAM10000_classified'
train_dir = 'datasets/train'
test_dir = 'datasets/test'

os.makedirs(train_dir, exist_ok=True)
os.makedirs(test_dir, exist_ok=True)

test_size = 0.2

for dx in os.listdir(input_dir):
    dx_folder_path = os.path.join(input_dir, dx)
    if os.path.isdir(dx_folder_path):
        images = [f for f in os.listdir(dx_folder_path) if f.endswith('.jpg') or f.endswith('.png')]

        train_images, test_images = train_test_split(images, test_size=test_size, random_state=42)

        train_dx_folder = os.path.join(train_dir, dx)
        test_dx_folder = os.path.join(test_dir, dx)
        os.makedirs(train_dx_folder, exist_ok=True)
        os.makedirs(test_dx_folder, exist_ok=True)

        for image in train_images:
            src = os.path.join(dx_folder_path, image)
            dst = os.path.join(train_dx_folder, image)
            shutil.copy(src, dst)

        for image in test_images:
            src = os.path.join(dx_folder_path, image)
            dst = os.path.join(test_dx_folder, image)
            shutil.copy(src, dst)

print("Data split into train and test sets successfully.")

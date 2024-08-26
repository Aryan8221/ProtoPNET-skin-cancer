# import Augmentor
# import os
#
#
# def makedir(path):
#     '''
#     if path does not exist in the file system, create it
#     '''
#     if not os.path.exists(path):
#         os.makedirs(path)
#
#
# datasets_root_dir = 'datasets/cub200_cropped/'
# dir = datasets_root_dir + 'train_cropped/'
# target_dir = datasets_root_dir + 'train_cropped_augmented/'
#
# makedir(target_dir)
# folders = [os.path.join(dir, folder) for folder in next(os.walk(dir))[1]]
# target_folders = [os.path.join(target_dir, folder) for folder in next(os.walk(dir))[1]]
#
# for i in range(len(folders)):
#     fd = folders[i]
#     tfd = target_folders[i]
#
#
#     # Function to safely process images with exception handling
#     def safe_process(pipeline, num_times=10):
#         try:
#             for _ in range(num_times):
#                 pipeline.process()
#         except ValueError as e:
#             print(f"Error processing images in folder {fd}: {e}")
#
#
#     # rotation
#     p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
#     p.rotate(probability=1, max_left_rotation=15, max_right_rotation=15)
#     p.flip_left_right(probability=0.5)
#     safe_process(p)
#     del p
#
#     # skew
#     p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
#     p.skew(probability=1, magnitude=0.2)  # max 45 degrees
#     p.flip_left_right(probability=0.5)
#     safe_process(p)
#     del p
#
#     # shear
#     p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
#     p.shear(probability=1, max_shear_left=10, max_shear_right=10)
#     p.flip_left_right(probability=0.5)
#     safe_process(p)
#     del p
#
#     # Uncomment and apply random_distortion if needed
#     # p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
#     # p.random_distortion(probability=1.0, grid_width=10, grid_height=10, magnitude=5)
#     # p.flip_left_right(probability=0.5)
#     # safe_process(p)
#     # del p

#-------------------------------------------
import os
import Augmentor

def safe_process(pipeline):
    try:
        pipeline.process()
    except Exception as e:
        print(f"An error occurred during augmentation: {e}")

# Paths
train_dir = 'datasets/train'  # Directory where the train split is stored
augmented_dir = os.path.join(train_dir, 'train_augmented')  # Directory to store all augmented images

# Ensure the Augmented directory exists
os.makedirs(augmented_dir, exist_ok=True)

# Iterate over each dx folder in the train directory
for dx in os.listdir(train_dir):
    dx_folder_path = os.path.join(train_dir, dx)
    if os.path.isdir(dx_folder_path):
        # Augmentation output directory for the specific dx class
        aug_output_dir = os.path.join(augmented_dir, dx)
        os.makedirs(aug_output_dir, exist_ok=True)

        # Apply augmentations
        fd = dx_folder_path  # Source directory
        tfd = aug_output_dir  # Target directory for augmented images

        # Rotation
        p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        p.rotate(probability=1, max_left_rotation=15, max_right_rotation=15)
        p.flip_left_right(probability=0.5)
        safe_process(p)
        del p

        # Skew
        p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        p.skew(probability=1, magnitude=0.2)  # max 45 degrees
        p.flip_left_right(probability=0.5)
        safe_process(p)
        del p

        # Shear
        p = Augmentor.Pipeline(source_directory=fd, output_directory=tfd)
        p.shear(probability=1, max_shear_left=10, max_shear_right=10)
        p.flip_left_right(probability=0.5)
        safe_process(p)
        del p

print("Augmentations completed and images saved in the Augmented folder.")

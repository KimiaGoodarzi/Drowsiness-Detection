import random

import numpy as np
import os
import shutil
import os
import cv2
import zipfile
import requests
# from tensorflow import layers, models
from sklearn.model_selection import train_test_split

#
# file_url = "https://orbi.uliege.be/bitstream/2268/191620/4/DROZY.zip"
# local_file_dir = "Videos"
# local_file_path = os.path.join(local_file_dir, "drozy.zip")
#
# # Check if the file has already been downloaded
# if not os.path.isfile(local_file_path):
#     response = requests.get(file_url)
#     if response.status_code == 200:
#         file_content = response.content
#         if not os.path.exists(local_file_dir):
#             os.makedirs(local_file_dir)
#         with open(local_file_path, "w+b") as file:
#             file.write(file_content)
#         print("File downloaded and saved to:", local_file_path)
#     else:
#         print("Failed to download the file. Status code:", response.status_code)
# else:
#     print("File already exists:", local_file_path)
#
# extraction_path = "Videos"
# extracted_content_path = os.path.join(extraction_path, "DROZY")
# if not os.path.exists(extracted_content_path):
#     with zipfile.ZipFile(local_file_path, 'r') as zip_ref:
#         zip_ref.extractall(extraction_path)
#     print("Extraction complete.")
# else:
#     print("Content already extracted.")
#
# video_directory = "Videos/DROZY/videos_i8"  # Update this path
# image_directory = "Videos/VideotoImage"  # Update this path
#
# if not os.path.exists(image_directory):
#     os.makedirs(image_directory)
#
# num_frames_to_extract = 6
#
# for video_file in os.listdir(video_directory):
#     if video_file.endswith(".mp4"):
#         video_path = os.path.join(video_directory, video_file)
#         video_capture = cv2.VideoCapture(video_path)
#         total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
#         frames_to_extract = random.sample(range(total_frames), num_frames_to_extract)
#
#         frame_count = 0
#         while True:
#             ret, frame = video_capture.read()
#             if not ret:
#                 break
#             if frame_count in frames_to_extract:
#                 image_file_name = f"{video_file}_frame{frame_count:04d}.jpg"
#                 image_path = os.path.join(image_directory, image_file_name)
#                 cv2.imwrite(image_path, frame)
#             frame_count += 1
#         video_capture.release()
#
# print("Random frame extraction complete.")
# ---------------------------------------------------------------------
image_directory = "Videos/VideotoImage"
organized_directory = "Videos/organized_images"

# A list of lists with sleepiness labels
video_labels = [
    [3, 6, 7], [3, 7, 6], [2, 3, 4], [4, 8, 9], [3, 7, 8], [2, 3, 7], [0, 4, 9], [2, 6, 8], [2, 6, 8],
    [3, 6, 7], [4, 7, 7], [2, 5, 6], [6, 3, 7], [5, 7, 8]
]

# Define the full paths for the binary classification directories
binary_class_directories = {
    "0_to_4": os.path.join(organized_directory, "0_to_4"),
    "5_to_9": os.path.join(organized_directory, "5_to_9")
}

# Create the binary classification directories
for class_dir in binary_class_directories.values():
    os.makedirs(class_dir, exist_ok=True)

# Move the images from the 10 labeled directories to the binary classification directories
for label in range(10):
    label_dir = os.path.join(organized_directory, str(label))
    if os.path.exists(label_dir):
        for filename in os.listdir(label_dir):
            if filename.endswith(".jpg"):
                src = os.path.join(label_dir, filename)
                class_dir = binary_class_directories["0_to_4"] if label <= 4 else binary_class_directories["5_to_9"]
                dst = os.path.join(class_dir, filename)
                shutil.move(src, dst)
                print(f"Moving {src} to {dst}")
    else:
        print(f"Directory {label_dir} does not exist")

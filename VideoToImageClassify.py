import random

import numpy as np
import os
import shutil
import os
import cv2
import zipfile
import requests
import random
# from tensorflow import layers, models
from sklearn.model_selection import train_test_split

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
# video_directory = "Videos/DROZY/videos_i8"
# image_directory = "Videos/VideotoImage"
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
# # ---------------------------------------------------------------------
# image_directory = "Videos/VideotoImage"
# organized_directory = "Videos/organized_images"
#
# # sleepiness labels
# video_labels = [
#     [3, 6, 7], [3, 7, 6], [2, 3, 4], [4, 8, 9], [3, 7, 8], [2, 3, 7], [0, 4, 9], [2, 6, 8], [2, 6, 8],
#     [3, 6, 7], [4, 7, 7], [2, 5, 6], [6, 3, 7], [5, 7, 8]
# ]
#
# binary_class_directories = {
#     "0_to_4": os.path.join(organized_directory, "0_to_4"),
#     "5_to_9": os.path.join(organized_directory, "5_to_9")
# }
#
# for class_dir in binary_class_directories.values():
#     os.makedirs(class_dir, exist_ok=True)
#
# # from 10 labeled directories to the binary classification directories
# for label in range(10):
#     label_dir = os.path.join(organized_directory, str(label))
#     if os.path.exists(label_dir):
#         for filename in os.listdir(label_dir):
#             if filename.endswith(".jpg"):
#                 src = os.path.join(label_dir, filename)
#                 class_dir = binary_class_directories["0_to_4"] if label <= 4 else binary_class_directories["5_to_9"]
#                 dst = os.path.join(class_dir, filename)
#                 shutil.move(src, dst)
#                 print(f"Moving {src} to {dst}")
#     else:
#         print(f"Directory {label_dir} does not exist")
#
# organized_directory = "Videos/organized_images"
#
# not_sleepy_prefixes = ['1-1', '2-1', '3-1', '4-1', '5-1', '6-1', '7-2', '8-1', '10-1', '11-1', '12-1', '13-2']
# sleepy_prefixes = ['1-2', '2-2', '4-2', '5-2', '6-3', '7-3', '8-2', '9-2', '10-3', '11-2', '13-1', '14-1']
#
# test_dataset_dir = os.path.join(organized_directory, "test_dataset")
# os.makedirs(test_dataset_dir, exist_ok=True)
#
#
# def move_random_image(prefixes, source_dir, destination_dir):
#     selected_files = []
#     for prefix in prefixes:
#
#         matching_files = [f for f in os.listdir(source_dir) if f.startswith(prefix)]
#
#         if matching_files:
#             selected_file = random.choice(matching_files)
#             src_path = os.path.join(source_dir, selected_file)
#             dst_path = os.path.join(destination_dir, selected_file)
#             shutil.move(src_path, dst_path)
#             selected_files.append(selected_file)
#             print(f"Moved {selected_file} to {destination_dir}")
#     return selected_files
#
#
# move_random_image(not_sleepy_prefixes, binary_class_directories['0_to_4'], test_dataset_dir)
#
# move_random_image(sleepy_prefixes, binary_class_directories['5_to_9'], test_dataset_dir)

from PIL import Image
import os

# Replace 'path_to_one_image.jpg' with the actual path to one of your images
image_path = 'Videos/organized_images/0_to_4/1-1.mp4_frame7362.jpg'

# Open the image and print its size
with Image.open(image_path) as img:
    print(img.size)  # Outputs: (width, height)

from random import random

import numpy as np
import os
import shutil
import os
import cv2
import zipfile
import requests
# from tensorflow import layers, models
from sklearn.model_selection import train_test_split

file_url = "https://orbi.uliege.be/bitstream/2268/191620/4/DROZY.zip"
response = requests.get(file_url)

if response.status_code == 200:
    file_content = response.content
else:
    print("Failed to download the file. Status code:", response.status_code)

local_file_dir = "Videos"

if not os.path.exists(local_file_dir):
    os.makedirs(local_file_dir)

local_file_path = os.path.join(local_file_dir, "drozy.zip")

with open(local_file_path, "w+b") as file:
    file.write(file_content)

print("File downloaded and saved to:", local_file_path)

extraction_path = "/Videos"

if not os.path.exists(extraction_path):
    os.makedirs(extraction_path)

with zipfile.ZipFile(local_file_path, 'r') as zip_ref:
    zip_ref.extractall(extraction_path)

video_directory = "Videos/DROZY/videos_i8"  # Update this path
image_directory = "Videos/VideotoImage"  # Update this path

if not os.path.exists(image_directory):
    os.makedirs(image_directory)

num_frames_to_extract = 6  # Changed from 3 to 6

for video_file in os.listdir(video_directory):
    if video_file.endswith(".mp4"):
        video_path = os.path.join(video_directory, video_file)
        video_capture = cv2.VideoCapture(video_path)
        total_frames = int(video_capture.get(cv2.CAP_PROP_FRAME_COUNT))
        frames_to_extract = random.sample(range(total_frames), num_frames_to_extract)

        frame_count = 0
        while True:
            ret, frame = video_capture.read()
            if not ret:
                break
            if frame_count in frames_to_extract:
                image_file_name = f"{video_file}_frame{frame_count:04d}.jpg"
                image_path = os.path.join(image_directory, image_file_name)
                cv2.imwrite(image_path, frame)
            frame_count += 1
        video_capture.release()

print("Random frame extraction complete.")
# ---------------------------------------------------------------------



# Assuming 'video_labels' is a list of lists with sleepiness labels
video_labels = [
    [3, 6, 7], [3, 7, 6], [2, 3, 4], [4, 8, 9],  # ... and so on for all 14 persons
]

image_directory = "/path/to/images"
organized_directory = "/path/to/organized_images"

# Create subdirectories for each sleepiness label
for i in range(10):  # Assuming sleepiness labels range from 0 to 9
    label_dir = os.path.join(organized_directory, str(i))
    os.makedirs(label_dir, exist_ok=True)

# Move the images to their respective label directories
for filename in os.listdir(image_directory):
    if filename.endswith(".jpg"):
        # Extract person number and video set number
        person, video_set = filename.split('-')[0], filename.split('-')[1].split('_')[0]
        person, video_set = int(person), int(video_set)

        # Use the extracted numbers to find the correct label
        label = video_labels[person - 1][video_set - 1]

        # Move the file to the correct directory
        src = os.path.join(image_directory, filename)
        dst = os.path.join(organized_directory, str(label), filename)
        shutil.move(src, dst)



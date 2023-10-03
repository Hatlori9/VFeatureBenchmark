import cv2
import csv
import os
import numpy as np
from tensorflow.keras.applications.vgg16 import VGG16, preprocess_input
from tensorflow.keras.models import Model

# Load VGG16 model + higher level layers
base_model = VGG16()
model = Model(inputs=base_model.input, outputs=base_model.get_layer('fc1').output)


def extract_features(video_path):
    cap = cv2.VideoCapture(video_path)
    frame_count = int(cap.get(cv2.CAP_PROP_FRAME_COUNT))
    fps = int(cap.get(cv2.CAP_PROP_FPS))

    features = []

    for i in range(frame_count):
        ret, frame = cap.read()
        if not ret:
            continue

        frame = cv2.resize(frame, (224, 224))
        frame = np.expand_dims(frame, axis=0)
        frame = preprocess_input(frame)

        feature_vector = model.predict(frame)[0]  # Flatten the output

        # Here, you might want to perform additional processing to interpret
        # the feature_vector, for example, clustering to categorize it.
        # For simplicity, we'll assume that the feature vector itself is the feature.

        feature_name = "feature_" + str(i)
        start_time = i / fps
        end_time = (i + 1) / fps
        start_frame = i
        end_frame = i + 1

        features.append((feature_name, start_time, end_time, start_frame, end_frame))

    cap.release()
    return features


def append_to_csv(data, csv_path):
    with open(csv_path, mode='a', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(data)


def process_videos(video_folder, csv_path):
    video_formats = (".mp4", ".mkv", ".avi", ".mov", ".flv")  # Add/modify video formats as needed

    for video_file in os.listdir(video_folder):
        if video_file.endswith(video_formats):
            video_path = os.path.join(video_folder, video_file)

            features = extract_features(video_path)

            video_id = os.path.splitext(video_file)[0]
            csv_data = [[video_id, *feature] for feature in features]

            append_to_csv(csv_data, csv_path)


# Example usage
video_folder_path = "/path/to/videos"
csv_file_path = "output_features.csv"

# Ensure the CSV has the header
with open(csv_file_path, mode='w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(["video_id", "feature_name", "start_time", "end_time", "start_frame", "end_frame"])

# Process videos
process_videos(video_folder_path, csv_file_path)

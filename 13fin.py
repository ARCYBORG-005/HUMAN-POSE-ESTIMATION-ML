import streamlit as st
import cv2
import mediapipe as mp
import matplotlib.pyplot as plt
from PIL import Image
import numpy as np

# Initialize Mediapipe Pose
mp_pose = mp.solutions.pose
pose = mp_pose.Pose(min_detection_confidence=0.5, min_tracking_confidence=0.5)
mp_drawing = mp.solutions.drawing_utils

# Streamlit UI
st.title("Pose Detection using Mediapipe")
st.markdown("Upload a video or image to detect pose landmarks")

uploaded_file = st.file_uploader("Choose a file", type=["mp4", "jpg", "png"])

if uploaded_file is not None:
    # For images
    if uploaded_file.type in ["image/jpeg", "image/png"]:
        image = Image.open(uploaded_file)
        st.image(image, caption="Uploaded Image", use_container_width=True)

        # Convert image to array and process
        frame = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
        frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
        results = pose.process(frame_rgb)

        if results.pose_landmarks:
            mp_drawing.draw_landmarks(
                frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
            )

        # Show the processed image
        processed_image = Image.fromarray(cv2.cvtColor(frame, cv2.COLOR_BGR2RGB))
        st.image(processed_image, caption="Processed Image", use_container_width=True)

    # For videos
    elif uploaded_file.type == "video/mp4":
        # Save the video to a temporary file
        with open("temp_video.mp4", "wb") as f:
            f.write(uploaded_file.getbuffer())

        cap = cv2.VideoCapture("temp_video.mp4")
        stframe = st.empty()

        while cap.isOpened():
            ret, frame = cap.read()
            if not ret:
                break

            frame_rgb = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            results = pose.process(frame_rgb)

            if results.pose_landmarks:
                mp_drawing.draw_landmarks(
                    frame, results.pose_landmarks, mp_pose.POSE_CONNECTIONS,
                    mp_drawing.DrawingSpec(color=(0, 255, 0), thickness=2, circle_radius=4),
                    mp_drawing.DrawingSpec(color=(0, 0, 255), thickness=2)
                )

            stframe.image(frame, channels="BGR", use_container_width=True)

        cap.release()
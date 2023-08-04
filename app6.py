import streamlit as st
import moviepy.editor as mp
import os
import json

import cv2
import json
import os
import tempfile
from pathlib import Path

def main():
    st.title("Video Player")

    st.title("Video Clip Fetcher")
    query = st.text_input("Enter the query:")

    # Provide the path to the folder containing the videos
    folder_path = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\Output Videos"

    # Load the captions from the JSON file
    with open('Final_frames_to_json_format.json', 'r') as file:
        image_data = json.load(file)

    # Get the video paths that match the query
    matching_videos = get_matching_videos(query, image_data, folder_path)

    # Play the matching videos
    for video_path in matching_videos:
        st.subheader("Video")
        play_video(video_path)


def get_matching_videos(query, image_data, folder_path):
    matching_videos = []

    # Iterate through each image data entry
    for image_info in image_data:
        caption = image_info.get('caption')

        # Check if the query matches the caption partially or completely
        if caption and query.lower() in caption.lower():
            # Get the frame path and construct the video path
            frame_path = os.path.join(folder_path, image_info.get('frame_path'))
            video_path = construct_video_path(frame_path, folder_path)

            # Add the video path to the list of matching videos
            matching_videos.append(video_path)

    return matching_videos


def construct_video_path(frame_path, folder_path):
    # Assuming the frame_path follows a specific pattern, extract the video file name
    video_name = os.path.basename(os.path.dirname(frame_path))

    # Construct the video path using the video file name
    video_path = os.path.join(folder_path, f"{video_name}.mp4")
    return video_path


def play_video(video_path):
    # Convert video to compatible format
    converted_path = "converted_video.mp4"
    clip = mp.VideoFileClip(video_path)
    clip.write_videofile(converted_path, codec="libx264", audio_codec="aac")

    # Display the converted video
    st.video(converted_path)


if __name__ == "__main__":
    main()

# import streamlit as st
# import cv2
# import json
# import os
# import tempfile
# from pathlib import Path

# # Function to extract frames matching the query from the JSON file
# def extract_matching_frames(query, json_file):
#     frames = []
#     with open(json_file, 'r') as file:
#         data = json.load(file)
#         for item in data:
#             if query.lower() in item['caption'].lower():
#                 frames.append(item)
#     return frames[:40]  # Extract only the first 40 matching frames

# # Function to create a video from the frames and save it in a rank-specific folder
# def create_video(frames, rank):
#     output_dir = os.path.join('videos', f'rank_{rank}')
#     Path(output_dir).mkdir(parents=True, exist_ok=True)

#     temp_dir = tempfile.mkdtemp()
#     for i, frame in enumerate(frames):
#         frame_path = frame['frame_path']
#         frame_data = cv2.imread(frame_path)
#         frame_name = f"frame_{i}.jpg"
#         frame_path = os.path.join(temp_dir, frame_name)
#         cv2.imwrite(frame_path, frame_data)  # Save the frame as an image

#     video_path = os.path.join(output_dir, "output.mp4")
#     frame_shape = cv2.imread(frame_path).shape
#     video_writer = cv2.VideoWriter(video_path, cv2.VideoWriter_fourcc(*"mp4v"), 25, (frame_shape[1], frame_shape[0]))

#     for i in range(len(frames)):
#         frame_path = os.path.join(temp_dir, f"frame_{i}.jpg")
#         frame = cv2.imread(frame_path)
#         video_writer.write(frame)  # Write the frame to the video

#     video_writer.release()
#     return video_path, frames

# # Streamlit interface
# def main():
#     st.title("Frame Matching and Video Generation")
#     query = st.text_input("Enter a text query")
#     json_file = "Final_frames_to_json_format.json"  # Path to your JSON file

#     if st.button("Search and Generate Videos"):
#         frames = extract_matching_frames(query, json_file)
#         if len(frames) == 0:
#             st.write("No matching frames found.")
#         else:
#             video_data = []
#             for i, frame in enumerate(frames):
#                 rank = i + 1
#                 video_path, video_frames = create_video([frame], rank)
#                 video_bytes = open(video_path, 'rb').read()
#                 video_data.append({"rank": rank, "video_bytes": video_bytes, "frames": video_frames})

#             selected_video = st.selectbox("Select Video", [data["rank"] for data in video_data])
#             selected_frames = [data["frames"] for data in video_data if data["rank"] == selected_video][0]

#             for frame in selected_frames:
#                 frame_data = cv2.imread(frame['frame_path'])
#                 st.image(frame_data, channels="BGR", use_column_width=True)

#             st.video(video_data[selected_video - 1]["video_bytes"])

# if __name__ == '__main__':
#     main()

import streamlit as st
import cv2
import json
import os
import tempfile
from pathlib import Path

import streamlit as st
import moviepy.editor as mp
import os





import streamlit as st
import moviepy.editor as mp
import os


def main():
    
    #title
    st.title("Welcome Cross Model Text-To-Video Retrieval")

    #Header
    st.header("Deep Learning")

    #information 
    st.info("Guide")
    #subheadre
    st.subheader("Mrs. Prajakta Ugale")

    #information
    st.info("Team Members ")
    st.text("Waqar Farooqui       PRN - 0120200475")
    st.text("Rohini Kanherkar     PRN - 0120200126")
    st.text("Puja Kumari          PRN - 0120200115")


    st.title("Video Clip Fetcher")
    query = st.text_input("Enter the query:")

    # Provide the path to the folder containing the videos
    folder_path = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\Output Videos"

    # Get a list of video files in the folder
    video_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(".mp4")]

    # Check if query is entered
    if query:
        # Convert and display each video in the folder
        for video_path in video_files:
            st.subheader("Video")

            # Convert video to compatible format
            converted_path = "converted_video.mp4"
            clip = mp.VideoFileClip(video_path)
            clip.write_videofile(converted_path, codec="libx264", audio_codec="aac")

            # Display the converted video
            st.video(converted_path)

if __name__ == "__main__":
    main()

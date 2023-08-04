# import streamlit as st

# import os
# import json
# import cv2

# # Load the JSON file containing image data
# with open('image_frames_full.json', 'r') as file:
#     image_data = json.load(file)

# # Function to retrieve frames based on text query and store them in a different path
# def retrieve_and_store_video_clips(query, destination_folder):
#     matching_frames = []
#     for image_info in image_data:
#         caption = image_info.get('caption')
#         if caption and query in caption:
#             frame_path = image_info.get('folder_path') + '\\' + f"frame_{str(image_info.get('frame_id')).zfill(4)}.jpg"
#             matching_frames.append(frame_path)
    
#     # Create the destination folder if it doesn't exist
#     os.makedirs(destination_folder, exist_ok=True)
    
#     # Iterate through each image and select additional 20 frames
#     for image_path in matching_frames:
#         image_name = os.path.basename(image_path)
#         image_folder = os.path.dirname(image_path)
#         image_frames = [image_path]  # Start with the original frame
        
#         # Add 20 more frames from the same image folder
#         image_frame_index = int(image_name.split('_')[-1].split('.')[0])  # Get the frame index from the image name
#         additional_frames = range(image_frame_index + 1, image_frame_index + 50)
#         for frame_index in additional_frames:
#             frame_name = f"frame_{str(frame_index).zfill(4)}.jpg"
#             frame_path = os.path.join(image_folder, frame_name)
#             if os.path.exists(frame_path):
#                 image_frames.append(frame_path)
        
#         # Create a video clip from the selected frames
#         video_clip_path = os.path.join(destination_folder, f"video_clip_{image_name.split('.')[0]}.mp4")
#         create_video_clip(image_frames, video_clip_path)
    
#     return destination_folder

# # Function to create a video clip from frames
# def create_video_clip(frames, output_path):
#     # Read the first frame to get its dimensions
#     first_frame = cv2.imread(frames[0])
#     frame_height, frame_width, _ = first_frame.shape
    
#     # Create a VideoWriter object to save the frames as a video
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec (use appropriate codec for the desired output format)
#     video_writer = cv2.VideoWriter(output_path, fourcc, 25.0, (frame_width, frame_height))
    
#     # Write each frame to the video
#     for frame_path in frames:
#         frame = cv2.imread(frame_path)
#         video_writer.write(frame)
    
#     # Release the VideoWriter and close the video file
#     video_writer.release()

# # Streamlit app
# def main():
#     st.title("Video Clip Generator")
#     query = st.text_input("Enter a query:")
#     destination_folder = 'C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\New folder'  # Specify the output folder path
    
#     if st.button("Generate Video Clips"):
#         if query:
#             st.info("Generating video clips. Please wait...")
#             retrieve_and_store_video_clips(query, destination_folder)
#             st.success("Video clips generated:")
#             video_clip_files = os.listdir(destination_folder)
#             for video_file in video_clip_files:
#                 video_path = os.path.join(destination_folder, video_file)
#                 st.video(video_path)
#         else:
#             st.warning("Please enter a query.")

# if __name__ == '__main__':
#     main()




# import streamlit as st
# from pathlib import Path
# import cv2

# def play_video(video_path):
#     cap = cv2.VideoCapture(str(video_path))
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         st.video(frame, channels="RGB")
#     cap.release()

# def main():
#     st.title("Video Player")
    
#     # Path to the folder containing the video files
#     video_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\New folder"
    
#     # Get a list of video files in the folder
#     videos = sorted(Path(video_folder).glob("*.mp4"))  # Update the file extension if needed
    
#     # Select a video to play
#     selected_video = st.selectbox("Select a video", videos)
    
#     # Play the selected video
#     play_video(selected_video)

# if __name__ == "__main__":
#     main()






# import streamlit as st
# import os
# import json
# import cv2
# from pathlib import Path

# # Load the JSON file containing image data
# with open('image_frames_full.json', 'r') as file:
#     image_data = json.load(file)

# # Function to retrieve frames based on text query and store them in a different path
# def retrieve_and_store_video_clips(query, destination_path):
#     matching_frames = []
#     for image_info in image_data:
#         caption = image_info.get('caption')
#         if caption and query in caption:
#             frame_path = os.path.join(image_info.get('folder_path'), f"frame_{str(image_info.get('frame_id')).zfill(4)}.jpg")
#             matching_frames.append(frame_path)
    
#     # Create the destination folder if it doesn't exist
#     os.makedirs(destination_path, exist_ok=True)
    
#     # Iterate through each image and select additional 20 frames
#     for image_path in matching_frames:
#         image_name = os.path.basename(image_path)
#         image_folder = os.path.dirname(image_path)
#         image_frames = [image_path]  # Start with the original frame
        
#         # Add 20 more frames from the same image folder
#         image_frame_index = int(image_name.split('_')[-1].split('.')[0])  # Get the frame index from the image name
#         additional_frames = range(image_frame_index + 1, image_frame_index + 50)
#         for frame_index in additional_frames:
#             frame_name = f"frame_{str(frame_index).zfill(4)}.jpg"
#             frame_path = os.path.join(image_folder, frame_name)
#             if os.path.exists(frame_path):
#                 image_frames.append(frame_path)
        
#         # Create a video clip from the selected frames
#         video_clip_path = os.path.join(destination_path, f"video_clip_{image_name.split('.')[0]}.mp4")
#         create_video_clip(image_frames, video_clip_path)
    
#     return destination_path

# # Function to create a video clip from frames
# def create_video_clip(frames, output_path):
#     # Read the first frame to get its dimensions
#     first_frame = cv2.imread(frames[0])
#     frame_height, frame_width, _ = first_frame.shape
    
#     # Create a VideoWriter object to save the frames as a video
#     video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 25.0, (frame_width, frame_height))
    
#     # Write each frame to the video
#     for frame_path in frames:
#         frame = cv2.imread(frame_path)
#         video_writer.write(frame)
    
#     # Release the VideoWriter and close the video file
#     video_writer.release()

# # Streamlit app
# def main():
#     st.title("Video Clip Fetcher")
#     query = st.text_input("Enter the query:")
#     destination_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\New folder"
#     if st.button("Fetch and Display Videos"):
#         video_folder = retrieve_and_store_video_clips(query, destination_folder)
#         #display_videos(video_folder)

#         # Play the first video in the folder
#         videos = sorted(Path(video_folder).glob("*.mp4"))
#         if len(videos) > 0:
#             video_path = str(videos[0])
#             st.video(video_path, width=500, height=375)
#         else:
#             st.write("No videos found.")

# if __name__ == "__main__":
#     main()











# import streamlit as st
# import os
# import json
# import cv2

# # Load the JSON file containing image data
# with open('image_frames_full.json', 'r') as file:
#     image_data = json.load(file)

# # Function to retrieve frames based on text query and store them in a different path
# def retrieve_and_store_video_clips(query, destination_path):
#     matching_frames = []
#     for image_info in image_data:
#         caption = image_info.get('caption')
#         if caption and query in caption:
#             frame_path = image_info.get('folder_path') + '\\' + f"frame_{str(image_info.get('frame_id')).zfill(4)}.jpg"
#             matching_frames.append(frame_path)
    
#     # Create the destination folder if it doesn't exist
#     os.makedirs(destination_path, exist_ok=True)
    
#     # Iterate through each image and select additional 20 frames
#     for image_path in matching_frames:
#         image_name = os.path.basename(image_path)
#         image_folder = os.path.dirname(image_path)
#         image_frames = [image_path]  # Start with the original frame
        
#         # Add 20 more frames from the same image folder
#         image_frame_index = int(image_name.split('_')[-1].split('.')[0])  # Get the frame index from the image name
#         additional_frames = range(image_frame_index + 1, image_frame_index + 50)
#         for frame_index in additional_frames:
#             frame_name = f"frame_{str(frame_index).zfill(4)}.jpg"
#             frame_path = os.path.join(image_folder, frame_name)
#             if os.path.exists(frame_path):
#                 image_frames.append(frame_path)
        
#         # Create a video clip from the selected frames
#         video_clip_path = os.path.join(destination_path, f"video_clip_{image_name.split('.')[0]}.mp4")
#         create_video_clip(image_frames, video_clip_path)
    
#     return destination_path

# # Function to create a video clip from frames
# def create_video_clip(frames, output_path):
#     # Read the first frame to get its dimensions
#     first_frame = cv2.imread(frames[0])
#     frame_height, frame_width, _ = first_frame.shape
    
#     # Create a VideoWriter object to save the frames as a video
#     video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 25.0, (frame_width, frame_height))
    
#     # Write each frame to the video
#     for frame_path in frames:
#         frame = cv2.imread(frame_path)
#         video_writer.write(frame)
    
#     # Release the VideoWriter and close the video file
#     video_writer.release()

# # Streamlit app
# def main():
#     st.title("Video Clip Fetcher")
#     query = st.text_input("Enter the query:")
#     destination_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\New folder"
#     if st.button("Fetch and Display Videos"):
#         video_folder = retrieve_and_store_video_clips(query, destination_folder)
#         #display_videos(video_folder)

#         # Play the first video in the folder
#         video_path = os.path.join(video_folder, os.listdir(video_folder)[0])
#         st.video(video_path, width=500, height=375)

# if __name__ == "__main__":
#     main()



# import streamlit as st
# import os
# import cv2

# # Function to play a video given its path
# def play_video(video_path):
#     cap = cv2.VideoCapture(video_path)
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         st.image(frame, channels="RGB")
#     cap.release()

# # Function to display frames as images
# def display_frames(frames):
#     for frame_path in frames:
#         frame = cv2.imread(frame_path)
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         st.image(frame, channels="RGB")

# # Function to retrieve frames and videos based on query
# def retrieve_and_display_videos(query, video_folder):
#     matching_videos = []
#     matching_frames = []

#     for video_file in os.listdir(video_folder):
#         if video_file.endswith(".mp4"):
#             video_path = os.path.join(video_folder, video_file)
#             matching_videos.append(video_path)

#             # Extract frames from the video
#             frame_folder = os.path.splitext(video_path)[0]
#             frames = extract_frames(video_path, frame_folder)
#             matching_frames.extend(frames)

#     # Display the videos
#     for video_path in matching_videos:
#         st.subheader("Video")
#         st.video(video_path)

#     # Display the frames
#     st.subheader("Frames")
#     display_frames(matching_frames)

# # Function to extract frames from a video
# def extract_frames(video_path, frame_folder):
#     os.makedirs(frame_folder, exist_ok=True)

#     cap = cv2.VideoCapture(video_path)
#     frame_count = 0
#     frames = []

#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break

#         frame_path = os.path.join(frame_folder, f"frame_{frame_count}.jpg")
#         cv2.imwrite(frame_path, frame)
#         frames.append(frame_path)

#         frame_count += 1

#     cap.release()
#     return frames

# # Streamlit app
# def main():
#     st.title("Video and Frame Retrieval")

#     # Query input
#     query = st.text_input("Enter your query")

#     # Video folder path
#     video_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\Output Videos"

#     # Retrieve and display videos and frames based on query
#     if st.button("Retrieve and Display"):
#         retrieve_and_display_videos(query, video_folder)

# if __name__ == "__main__":
#     main()


import streamlit as st
import os
import cv2

# Function to play a video given its path
def play_video(video_path):
    video_file = open(video_path, 'rb')
    video_bytes = video_file.read()
    st.video(video_bytes)

# Function to retrieve frames and videos based on query
def retrieve_and_display_videos(query, video_folder):
    matching_videos = []

    for video_file in os.listdir(video_folder):
        if video_file.endswith(".mp4"):
            video_path = os.path.join(video_folder, video_file)
            matching_videos.append(video_path)

    # Display the videos
    for video_path in matching_videos:
        st.subheader("Video")
        play_video(video_path)

# Streamlit app
def main():
    st.title("Video Retrieval")

    # Query input
    query = st.text_input("Enter your query")

    # Video folder path
    video_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\Output Videos"

    # Retrieve and display videos based on query
    if st.button("Retrieve and Display"):
        retrieve_and_display_videos(query, video_folder)

if __name__ == "__main__":
    main()

# # import streamlit as st

# # #title
# # st.title("Welcome Cross Model Text-To-Video Retrieval")

# # #Header
# # st.header("Deep Learning")

# # #information
# # st.info("Guide")
# # #subheadre
# # st.subheader("Mrs. Prajakta Ugale")

# # #information
# # st.info("Team Members ")
# # st.text("Waqar Farooqui       PRN - 0120200475")
# # st.text("Rohini Kanherkar     PRN - 0120200126")
# # st.text("Puja Kumari          PRN - 0120200115")

# # #warning
# # st.warning("Come on time or else you will be marked absent")

# # st.error("Wrong input")

# # st.success("Congrats you got video for your inputed query")


# import streamlit as st

# import os
# import json
# from shutil import copyfile
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
#         additional_frames = range(image_frame_index + 1, image_frame_index + 20)
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
#     destination_folder = st.text_input("Enter the destination folder path:")
    
#     if st.button("Generate Video Clips"):
#         if query and destination_folder:
#             st.info("Generating video clips. Please wait...")
#             retrieve_and_store_video_clips(query, destination_folder)
#             st.success("Video clips generated and stored in: " + destination_folder)
#         else:
#             st.warning("Please enter both the query and destination folder path.")

# if __name__ == '__main__':
#     main()




import streamlit as st

import os
import json
from shutil import copyfile
import cv2

# Load the JSON file containing image data
with open('image_frames_full.json', 'r') as file:
    image_data = json.load(file)

# Function to retrieve frames based on text query and store them in a different path
def retrieve_and_store_video_clips(query):
    matching_frames = []
    for image_info in image_data:
        caption = image_info.get('caption')
        if caption and query in caption:
            frame_path = image_info.get('folder_path') + '\\' + f"frame_{str(image_info.get('frame_id')).zfill(4)}.jpg"
            matching_frames.append(frame_path)
    
    # Create a list to store the video clip paths
    video_clip_paths = []
    
    # Iterate through each image and select additional 20 frames
    for image_path in matching_frames:
        image_name = os.path.basename(image_path)
        image_folder = os.path.dirname(image_path)
        image_frames = [image_path]  # Start with the original frame
        
        # Add 20 more frames from the same image folder
        image_frame_index = int(image_name.split('_')[-1].split('.')[0])  # Get the frame index from the image name
        additional_frames = range(image_frame_index + 1, image_frame_index + 20)
        for frame_index in additional_frames:
            frame_name = f"frame_{str(frame_index).zfill(4)}.jpg"
            frame_path = os.path.join(image_folder, frame_name)
            if os.path.exists(frame_path):
                image_frames.append(frame_path)
        
        # Create a video clip from the selected frames
        video_clip_path = os.path.join(image_folder, f"video_clip_{image_name.split('.')[0]}.mp4")
        create_video_clip(image_frames, video_clip_path)
        video_clip_paths.append(video_clip_path)
    
    return video_clip_paths

# Function to create a video clip from frames
def create_video_clip(frames, output_path):
    # Read the first frame to get its dimensions
    first_frame = cv2.imread(frames[0])
    frame_height, frame_width, _ = first_frame.shape
    
    # Create a VideoWriter object to save the frames as a video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec (use appropriate codec for the desired output format)
    video_writer = cv2.VideoWriter(output_path, fourcc, 25.0, (frame_width, frame_height))
    
    # Write each frame to the video
    for frame_path in frames:
        frame = cv2.imread(frame_path)
        video_writer.write(frame)
    
    # Release the VideoWriter and close the video file
    video_writer.release()

# Streamlit app
def main():
    st.title("Video Clip Generator")
    query = st.text_input("Enter a query:")
    
    if query:
        st.info("Generating video clips. Please wait...")
        video_clip_paths = retrieve_and_store_video_clips(query)
        st.success("Video clips generated:")
        for video_path in video_clip_paths:
            video_file = open(video_path, 'rb')
            video_bytes = video_file.read()
            st.video(video_bytes)

if __name__ == '__main__':
    main()

# import streamlit as st
# import os

# def fetch_videos(folder_path):
#     if not os.path.exists(folder_path):
#         st.error("Folder does not exist.")
#         return

#     videos = [f for f in os.listdir(folder_path) if f.endswith((".mp4", ".avi", ".mov"))]

#     if not videos:
#         st.warning("No videos found in the folder.")
#     else:
#         st.success(f"Found {len(videos)} video(s) in the folder:")
#         for video in videos:
#             st.write(video)



















# def main():
#     st.title("Video Folder Fetcher")
#     folder_path = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\New folder"
#     if st.button("Fetch Videos"):
#         fetch_videos(folder_path)

# if __name__ == "__main__":
#     main()

# import streamlit as st
# import os

# def main():
#     st.title("Video Folder Fetcher")
#     folder_path = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\New folder"
#     if st.button("Fetch Videos"):
#         fetch_videos(folder_path)

# def fetch_videos(folder_path):
#     if not os.path.exists(folder_path):
#         st.error("Folder does not exist.")
#         return

#     videos = [f for f in os.listdir(folder_path) if f.endswith((".mp4", ".avi", ".mov"))]

#     if not videos:
#         st.warning("No videos found in the folder.")
#     else:
#         st.success(f"Found {len(videos)} video(s) in the folder:")
#         for video in videos:
#             video_path = os.path.join(folder_path, video)
#             st.video(video_path)

# if __name__ == "__main__":
#     main()













# import streamlit as st
# from streamlit.components.v1 import html
# import base64
# import os

# def main():
#     st.title("Video Folder Fetcher")
#     folder_path = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\New folder"
#     if st.button("Fetch Videos"):
#         fetch_videos(folder_path)

# def fetch_videos(folder_path):
#     if not os.path.exists(folder_path):
#         st.error("Folder does not exist.")
#         return

#     videos = [f for f in os.listdir(folder_path) if f.endswith((".mp4", ".avi", ".mov"))]

#     if not videos:
#         st.warning("No videos found in the folder.")
#     else:
#         st.success(f"Found {len(videos)} video(s) in the folder:")
#         for video in videos:
#             video_path = os.path.join(folder_path, video)
#             video_base64 = base64_encode(video_path)
#             video_html = f'<video width="100%" controls><source src="data:video/mp4;base64,{video_base64}" type="video/mp4"></video>'
#             st.write(video)
#             html(video_html, height=300)

# def base64_encode(video_path):
#     with open(video_path, "rb") as file:
#         video_bytes = file.read()
#         encoded_bytes = base64.b64encode(video_bytes)
#         encoded_string = encoded_bytes.decode("utf-8")
#     return encoded_string

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
#     # Create a VideoWriter object to save the frames as a video
#     fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec (use appropriate codec for the desired output format)
#     video_writer = None
    
#     try:
#         # Read the first frame to get its dimensions
#         first_frame = cv2.imread(frames[0])
#         frame_height, frame_width, _ = first_frame.shape
        
#         video_writer = cv2.VideoWriter(output_path, fourcc, 25.0, (frame_width, frame_height))
        
#         # Write each frame to the video
#         for frame_path in frames:
#             frame = cv2.imread(frame_path)
#             video_writer.write(frame)
#     except Exception as e:
#         print(f"Error creating video clip: {e}")
#     finally:
#         # Release the VideoWriter and close the video file
#         if video_writer is not None:
#             video_writer.release()

# # Streamlit app
# def main():
#     st.title("Video Clip Fetcher")
#     query = st.text_input("Enter the query:")
#     destination_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\New folder"
#     if st.button("Fetch and Display Videos"):
#         video_folder = retrieve_and_store_video_clips(query, destination_folder)
#         display_videos(video_folder)

# def display_videos(video_folder):
#     videos = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]

#     if not videos:
#         st.warning("No videos found in the folder.")
#     else:
#         st.success(f"Found {len(videos)} video(s) in the folder path C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\New folder ")
#         for video in videos:
#             video_path = os.path.join(video_folder, video)
#             st.video(video_path)

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
#         display_videos(video_folder)

# def display_videos(video_folder):
#     videos = [f for f in os.listdir(video_folder) if f.endswith(".mp4")]

#     if not videos:
#         st.warning("No videos found in the folder.")
#     else:
#         st.success(f"Found {len(videos)} video(s) in the folder:")
#         for video in videos:
#             video_path = os.path.join(video_folder, video)
#             st.video(video_path)

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
# from pathlib import Path
# import cv2
# import os
# import json



# import streamlit as st

# #title
# st.title("Welcome To Cross Model Text-To-Video Retrieval")

# #Header
# st.header("Deep Learning")

# #information
# st.info("Guide")
# #subheadre
# st.subheader("Mrs. Prajakta Ugale")

# #information
# st.info("Team Members ")
# st.text("Waqar Farooqui       PRN - 0120200475")
# st.text("Rohini Kanherkar     PRN - 0120200126")
# st.text("Puja Kumari          PRN - 0120200115")

# # #warning``
# # st.warning("Come on time or else you will be marked absent")

# # st.error("Wrong input")

# # st.success("Congrats you got video for your inputed query")


# def play_video(video_path):
#     cap = cv2.VideoCapture(str(video_path))
#     while cap.isOpened():
#         ret, frame = cap.read()
#         if not ret:
#             break
#         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
#         st.image(frame, channels="RGB")
#     cap.release()

# with open('image_frames_full.json', 'r') as file:
#     image_data = json.load(file)

# def retrieve_and_store_video_clips(query, destination_path):
#     matching_frames = []
#     for image_info in image_data:
#         caption = image_info.get('caption')
#         if caption and query in caption:
#             frame_path = os.path.join(image_info.get('folder_path'), f"frame_{str(image_info.get('frame_id')).zfill(4)}.jpg")
#             matching_frames.append(frame_path)
    
#     # Create the destination folder if it doesn't exist
#     os.makedirs(destination_path, exist_ok=True)

#  # Iterate through each image and select additional 20 frames
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


# def main():
#     st.title("Video Player")
    
#     # Path to the folder containing the video files
#     video_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\Output Videos"
    
#     # Get a list of video files in the folder
#     videos = sorted(Path(video_folder).glob("*.mp4"))  # Update the file extension if needed
    
#     # Select a video to play
#     selected_video = st.selectbox("Select a video", videos)
    
#     # Play the selected video
#     play_video(selected_video)



#     st.title("Video Clip Fetcher")
#     query = st.text_input("Enter the query :")
#     destination_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\Output Videos"
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



# # import streamlit as st
# # from pathlib import Path
# # import cv2
# # import os
# # import json


# # def play_video(video_path):
# #     cap = cv2.VideoCapture(str(video_path))
# #     while cap.isOpened():
# #         ret, frame = cap.read()
# #         if not ret:
# #             break
# #         frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
# #         st.image(frame, channels="RGB")
# #     cap.release()


# # with open('image_frames_full.json', 'r') as file:
# #     image_data = json.load(file)


# # def retrieve_and_store_video_clips(query, destination_path):
# #     matching_frames = []
# #     for image_info in image_data:
# #         caption = image_info.get('caption')
# #         if caption and query in caption:
# #             frame_path = os.path.join(image_info.get('folder_path'), f"frame_{str(image_info.get('frame_id')).zfill(4)}.jpg")
# #             matching_frames.append(frame_path)
# #     # Create the destination folder if it doesn't exist
# #     os.makedirs(destination_path, exist_ok=True)

# #     # Iterate through each image and select additional 50 frames
# #     for image_path in matching_frames:
# #         image_name = os.path.basename(image_path)
# #         image_folder = os.path.dirname(image_path)
# #         image_frames = [image_path]  # Start with the original frame

# #         # Add 50 more frames from the same image folder
# #         image_frame_index = int(image_name.split('_')[-1].split('.')[0])  # Get the frame index from the image name
# #         additional_frames = range(image_frame_index + 1, image_frame_index + 51)
# #         for frame_index in additional_frames:
# #             frame_name = f"frame_{str(frame_index).zfill(4)}.jpg"
# #             frame_path = os.path.join(image_folder, frame_name)
# #             if os.path.exists(frame_path):
# #                 image_frames.append(frame_path)

# #         # Create a video clip from the selected frames
# #         video_clip_path = os.path.join(destination_path, f"video_clip_{image_name.split('.')[0]}.mp4")
# #         create_video_clip(image_frames, video_clip_path)

# #     return destination_path


# # # Function to create a video clip from frames
# # def create_video_clip(frames, output_path):
# #     # Read the first frame to get its dimensions
# #     first_frame = cv2.imread(frames[0])
# #     frame_height, frame_width, _ = first_frame.shape

# #     # Create a VideoWriter object to save the frames as a video
# #     video_writer = cv2.VideoWriter(output_path, cv2.VideoWriter_fourcc(*'mp4v'), 25.0, (frame_width, frame_height))

# #     # Write each frame to the video
# #     for frame_path in frames:
# #         frame = cv2.imread(frame_path)
# #         video_writer.write(frame)

# #     # Release the VideoWriter and close the video file
# #     video_writer.release()


# # def main():
# #     st.title("Video Player")

# #     # Path to the folder containing the video files
# #     video_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\Output Videos"

# #     # Get a list of video files in the folder
# #     videos = sorted(Path(video_folder).glob("*.mp4"))  # Update the file extension if needed

# #     # Select a video to play
# #     selected_video = st.selectbox("Select a video", videos)

# #     # Play the selected video
# #     play_video(selected_video)

# #     st.title("Video Clip Fetcher")
# #     query = st.text_input("Enter the query:")
# #     destination_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\Output Videos"
# #     if st.button("Fetch and Display Videos"):
# #         video_folder = retrieve_and_store_video_clips(query, destination_folder)

# #         # Get a list of video files in the folder
# #         videos = sorted(Path(video_folder).glob("*.mp4"))

# #         # Play the first video in the folder
# #         if len(videos) > 0:
# #             video_path = str(videos[0])
# #             st.video(video_path, width=500, height=375)
# #         else:
# #             st.write("No videos found.")


# # if __name__ == "__main__":
# #     main()





# import streamlit as st
# import moviepy.editor as mp
# import os

# def main():
#     st.title("Video Player")

#     st.title("Video Clip Fetcher")
#     query = st.text_input("Enter the query :")

#     # Provide the path to the folder containing the videos
#     folder_path = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\Output Videos"

#     # Get a list of video files in the folder
#     video_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(".mp4")]

#     # Play the matching videos based on the query
#     for video_path in video_files:
#         st.subheader("Video")
#         play_video_based_on_query(query, video_path)

# def play_video_based_on_query(query, video_path):
#     # Check if the query is present in the video file name or path
#     if query.lower() in video_path.lower():
#         # Convert video to compatible format
#         converted_path = "converted_video.mp4"
#         clip = mp.VideoFileClip(video_path)
#         clip.write_videofile(converted_path, codec="libx264", audio_codec="aac")

#         # Display the converted video
#         st.video(converted_path)

#         # Remove the converted video file
#         os.remove(converted_path)

# if __name__ == "__main__":
#     main()



# import streamlit as st
# import moviepy.editor as mp
# import os

# def main():
#     st.title("Video Player")

#     st.title("Video Clip Fetcher")
#     query = st.text_input("Enter the query:")

#     # Provide the path to the folder containing the videos
#     folder_path = "C:\\Users\\admin\\Desktop\\SCET_Major\\frmes to json\\Output Videos"

#     # Get a list of video files in the folder
#     video_files = [os.path.join(folder_path, filename) for filename in os.listdir(folder_path) if filename.endswith(".mp4")]

#     # Play the matching videos based on the query
#     for video_path in video_files:
#         st.subheader("Video")
#         play_video_based_on_query(query, video_path)

# def play_video_based_on_query(query, video_path):
#     # Check if the query is present in the video file name or path
#     if query.lower() in video_path.lower():
#         # Check if the video file is in a compatible format
#         if not video_path.endswith(".mp4"):
#             converted_path = "converted_video.mp4"
#             clip = mp.VideoFileClip(video_path)
#             clip.write_videofile(converted_path, codec="libx264", audio_codec="aac")

#             # Display the converted video
#             st.video(converted_path)
#         else:
#             st.video(video_path)
#     else:
#         st.warning("No video found matching the query.")
#         return

# if __name__ == "__main__":
#     main()


import streamlit as st
import moviepy.editor as mp
import os

def main():
    st.title("Video Player")

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

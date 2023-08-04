from flask import Flask, request, jsonify
import os
import json
from shutil import copyfile
import cv2

app = Flask(__name__, static_folder='.', static_url_path='')

# Load the JSON file containing image data
with open('image_frames_full.json', 'r') as file:
    image_data = json.load(file)

# Function to retrieve frames based on text query and store them in a different path
def retrieve_and_store_video_clips(query, destination_path):
    matching_frames = []
    for image_info in image_data:
        caption = image_info.get('caption')
        if caption and query in caption:
            frame_path = image_info.get('folder_path') + '\\' + f"frame_{str(image_info.get('frame_id')).zfill(4)}.jpg"
            matching_frames.append(frame_path)

    # Create the destination folder if it doesn't exist
    os.makedirs(destination_path, exist_ok=True)

    # Iterate through each image and select additional 20 frames
    for image_path in matching_frames:
        image_name = os.path.basename(image_path)
        image_folder = os.path.dirname(image_path)
        image_frames = [image_path]  # Start with the original frame

        # Add 20 more frames from the same image folder
        image_frame_index = int(image_name.split('_')[-1].split('.')[0])  # Get the frame index from the image name
        additional_frames = range(image_frame_index + 1, image_frame_index + 50)
        for frame_index in additional_frames:
            frame_name = f"frame_{str(frame_index).zfill(4)}.jpg"
            frame_path = os.path.join(image_folder, frame_name)
            if os.path.exists(frame_path):
                image_frames.append(frame_path)

        # Create a video clip from the selected frames
        video_clip_path = os.path.join(destination_path, f"video_clip_{image_name.split('.')[0]}.mp4")
        create_video_clip(image_frames, video_clip_path)

    return destination_path

# Function to create a video clip from frames
def create_video_clip(frames, output_path):
    # Create a VideoWriter object to save the frames as a video
    fourcc = cv2.VideoWriter_fourcc(*'mp4v')  # Specify the codec (use appropriate codec for the desired output format)
    video_writer = None

    try:
        # Read the first frame to get its dimensions
        first_frame = cv2.imread(frames[0])
        frame_height, frame_width, _ = first_frame.shape

        video_writer = cv2.VideoWriter(output_path, fourcc, 25.0, (frame_width, frame_height))

        # Write each frame to the video
        for frame_path in frames:
            frame = cv2.imread(frame_path)
            video_writer.write(frame)
    except Exception as e:
        print(f"Error creating video clip: {e}")
    finally:
        # Release the VideoWriter and close the video file
        if video_writer is not None:
            video_writer.release()

@app.route('/generate_video_clip', methods=['POST'])
def generate_video_clip():
    try:
        query = request.form['query']
        destination_folder = "C:\\Users\\admin\\Desktop\\SCET_Major\\frames_to_json\\New folder"  # Specify the destination folder path
        result_folder = retrieve_and_store_video_clips(query, destination_folder)
        response = {'success': True, 'destination_folder': result_folder}
    except Exception as e:
        response = {'success': False, 'error': str(e)}
    return jsonify(response)

if __name__ == '__main__':
    app.run(debug=True)

import os
import re
import subprocess
from tkinter import filedialog
from tkinter import Tk
import sys

def extract_coordinates_from_srt(srt_file):
    latitude, longitude = None, None
    try:
        with open(srt_file, 'r', encoding='utf-8') as file:
            for line in file:
                lat_match = re.search(r'\[latitude: (-?\d+\.\d+)\]', line)
                lon_match = re.search(r'\[longitude: (-?\d+\.\d+)\]', line)
                if lat_match and lon_match:
                    latitude = lat_match.group(1)
                    longitude = lon_match.group(1)
                    break  # Take the first match as the coordinates for the video and ignore the rest
    except Exception as e:
        print(f"Error reading SRT file {srt_file}: {e}")
    return latitude, longitude

def add_geo_metadata_to_video(video_file, latitude, longitude):
    if latitude is None or longitude is None:
        print(f"Skipping {video_file}: No coordinates found.")
        return
    
    try:
        # Determine the path to exiftool based on whether we are running from a bundle
        if getattr(sys, 'frozen', False):
            # If the script is bundled into an .exe by PyInstaller
            script_dir = sys._MEIPASS
        else:
            # If running as a regular script
            script_dir = os.path.dirname(__file__)
        
        exiftool_path = os.path.join(script_dir, "exiftool_files", "exiftool.exe")
        
        # Command to add GPS metadata
        command = [
            exiftool_path,
            "-overwrite_original",  # Overwrite the original file without creating a backup
            f"-GPSLatitude={latitude}",
            f"-GPSLongitude={longitude}",
            "-FileCreateDate<CreateDate",  # Set FileCreateDate to match CreateDate to preserve original date
            video_file
        ]
        
        subprocess.run(command, check=True)
        
        print(f"Updated {video_file} with geo-coordinates: ({latitude}, {longitude}) and preserved original creation date.")
    except subprocess.CalledProcessError as e:
        print(f"Error adding metadata to {video_file}: {e}")

def main():
    # Prompt user to select folder
    root = Tk()
    root.withdraw()  # Hide the root window
    folder = filedialog.askdirectory(title="Select Folder Containing MP4 and SRT Files")

    if not folder:
        print("No folder selected. Exiting...")
        return

    # Iterate over files in the selected folder and its subfolders
    for root_dir, _, files in os.walk(folder):
        for filename in files:
            if filename.endswith('.MP4'):
                video_path = os.path.join(root_dir, filename)
                srt_filename = filename.replace('.MP4', '.SRT')
                srt_path = os.path.join(root_dir, srt_filename)

                if os.path.exists(srt_path):
                    latitude, longitude = extract_coordinates_from_srt(srt_path)
                    add_geo_metadata_to_video(video_path, latitude, longitude)
                else:
                    print(f"No matching SRT file found for {filename}")

if __name__ == "__main__":
    main()

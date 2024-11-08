# Geo-Tagging Video Script

## Overview
This Python script adds geo-coordinates to video files based on information extracted from matching SRT files. It's specifically designed to work with videos (e.g., from drones) that have associated SRT files containing GPS metadata.

The script processes all MP4 files in a selected folder (including subfolders), finds the corresponding SRT files, and updates the video metadata with the coordinates. ExifTool is used to modify the metadata without re-encoding the video.

## Features
- **Batch Processing**: Automatically processes all MP4 files and their matching SRT files in a folder.
- **Metadata Editing**: Adds latitude and longitude to video files using ExifTool, while preserving the original creation date.
- **Recursive Search**: Processes files in subfolders as well.
- **No Need to Manually Install ExifTool**: ExifTool is bundled directly with the executable, ensuring ease of use.

## Requirements
### Python Modules
The script uses the following Python standard libraries:
- `os`
- `re`
- `subprocess`
- `tkinter`
- `sys`

All of these modules are part of the standard Python library and do not require additional installation.

### External Tool
- **ExifTool**: Required to add metadata to video files. The script bundles ExifTool, so no manual installation is needed.

## Installation
To run the script, you will need Python 3.11 or later. If you want to create an executable (`.exe`), use PyInstaller.

1. Clone this repository:
   ```sh
   git clone <repository-url>
   cd <repository-folder>
   ```

2. Install PyInstaller to create the executable:
   ```sh
   pip install pyinstaller
   ```

3. Create an executable using PyInstaller:
   ```sh
   pyinstaller --onefile --add-data "exiftool_files;exiftool_files" --icon=srt.ico srt.py
   ```
   This command will create an `.exe` in the `dist` folder.

## Usage
1. **Running the Python Script**
   - Make sure `exiftool_files` (with all necessary ExifTool files) is in the same directory as the Python script.
   - Run the script using Python:
     ```sh
     python srt.py
     ```

2. **Using the Executable**
   - If you have created an `.exe` using PyInstaller, you can run it directly by double-clicking it.

3. **Selecting Folder**
   - The script will prompt you to select the folder containing the MP4 and SRT files. It will then iterate over all files and add geo-coordinates where applicable.

## Notes
- Ensure that the SRT file names match the corresponding MP4 files (e.g., `DJI_0609.MP4` should have `DJI_0609.SRT`).
- The script takes the first set of coordinates from the SRT file to tag the video.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Contributing
Feel free to open issues or create pull requests if you have suggestions for improvements or find bugs.

## Contact
For any questions, feel free to reach out or open an issue on GitHub.


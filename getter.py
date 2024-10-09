import os
import pandas as pd
import requests
from datetime import datetime, timedelta

# Load the DataFrame containing the file information
file_info_df = pd.read_csv('file_info.csv')  # Update with your CSV file path

# Directory to store downloaded files (you can add a base directory if needed)
base_download_directory = 'downloaded_files'

# Create the base directory if it doesn't exist
os.makedirs(base_download_directory, exist_ok=True)

def should_download(last_downloaded, periodicity):
    """Determine if the file should be downloaded based on periodicity."""
    now = datetime.now()
    
    if periodicity == 'monthly':
        # Check if today is the specified day of the month
        return now.day == last_downloaded.day or now > last_downloaded
    elif periodicity == 'weekly':
        # Check if it has been a week since the last download
        return (now - last_downloaded) >= timedelta(weeks=1)
    return False

def download_and_save_csv(url, filename, directory):
    """Download CSV file and save it to the specified directory."""
    try:
        response = requests.get(url)
        response.raise_for_status()  # Raise an error for bad responses

        # Ensure the directory exists
        os.makedirs(directory, exist_ok=True)

        # Save the CSV file
        file_path = os.path.join(directory, filename)
        with open(file_path, 'wb') as f:
            f.write(response.content)
        
        print(f"Successfully downloaded: {filename}")
        return True
    except Exception as e:
        print(f"Failed to download {url}: {e}")
        return False

# Loop through the DataFrame rows
for index, row in file_info_df.iterrows():
    filename = row['filename']
    url = row['url']
    directory = os.path.join(base_download_directory, row['directory'])
    periodicity = row['periodicity']
    
    # Try to load the last downloaded timestamp from a local file or use a default
    last_downloaded_file = os.path.join(directory, f'{filename}.last_downloaded')
    if os.path.exists(last_downloaded_file):
        with open(last_downloaded_file, 'r') as f:
            last_downloaded_str = f.read().strip()
            last_downloaded = datetime.fromisoformat(last_downloaded_str)
    else:
        # If not downloaded before, set last_downloaded to a past date
        last_downloaded = datetime.now() - timedelta(days=30)  # Adjust as needed

    # Check if we should download the file
    if should_download(last_downloaded, periodicity):
        if download_and_save_csv(url, filename, directory):
            # Update the last downloaded timestamp
            with open(last_downloaded_file, 'w') as f:
                f.write(datetime.now().isoformat())
    else:
        print(f"No need to download {filename} yet.")

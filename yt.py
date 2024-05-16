from pytube import YouTube

# Function to download YouTube video
def download_video(video_url, save_path):
    try:
        # Create YouTube object with the video URL
        yt = YouTube(video_url)

        # Select the highest resolution stream
        stream = yt.streams.get_highest_resolution()

        # Download the video
        stream.download(output_path=save_path)
        print("Download successful!")
    except Exception as e:
        print("Error:", e)

# Example usage
if __name__ == "__main__":
    video_url = input("Enter the YouTube video URL: ")
    save_path = input("Enter the path where you want to save the video: ")
    download_video(video_url, save_path)
-
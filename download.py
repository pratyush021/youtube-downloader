import argparse
from pytube import YouTube
import os

def download_video(url, output_path, resolution):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    yt = YouTube(url)
    if resolution not in ["360p", "480p", "720p"]: 
        print("Not a valid resoltion")
        return; 
    str1 = yt.streams.filter(progressive=True).get_by_resolution(resolution=resolution)
    print(f"Downloading: {yt.title} ({resolution})")
    str1.download(output_path=
                  output_path)
    print("Download complete!")

def main():
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-o", "--output", default="./downloads", help="Output path for downloaded video")
    parser.add_argument("-r", "--resolution", default="720p", help="Video resolution (e.g., 720p, 1080p)")

    args = parser.parse_args()
    download_video(args.url, args.output, args.resolution)

if __name__ == "__main__":
    main()

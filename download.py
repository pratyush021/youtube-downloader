import argparse
from pytube import YouTube
import os
from tqdm import tqdm

def download_video(url, output_path, resolution):
    if not os.path.exists(output_path):
        os.makedirs(output_path)
    yt = YouTube(url)
    if resolution not in ["360p", "480p", "720p"]: 
        print("Not a valid resolution")
        print("Please choose from 240p, 360p, 480p and 720p")
        return; 
    str1 = yt.streams.filter(progressive=True).get_by_resolution(resolution=resolution)
    print(f"Downloading: {yt.title} ({resolution})...")
    str1.download(output_path=
                  output_path)
    print("Download complete!")

def download_with_progress_bar(url, output): 
    if not os.path.exists(output): 
        os.makedirs(output)
    yt = YouTube(url=url)

    stream = yt.streams.filter(progressive=True).get_highest_resolution()
    
    with tqdm(total = stream.filesize, unit='B', unit_scale=True, unit_divisor=1024) as pbar: 
        with open(os.path.join(output, f'{yt.title}'), 'wb') as file: 
            for chunk in stream.iter_bytes(): 
                file.write(chunk)
                pbar.update(len(chunk))
    print("Download complete")





def main():
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-o", "--output", default="./downloads", help="Output path for downloaded video")
    parser.add_argument("-r", "--resolution", default="720p", help="Video resolution (e.g., 720p, 1080p)")

    args = parser.parse_args()
    download_video(args.url, args.output, args.resolution)
    # download_with_progress_bar(args.url, args.output)

if __name__ == "__main__":
    main()

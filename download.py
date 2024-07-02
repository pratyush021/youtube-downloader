import argparse
from pytube import YouTube
import os
from tqdm import tqdm
import time 



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
    yt.register_on_complete_callback(on_complete)
    yt.register_on_progress_callback(on_progress)
    time1 = time.time()
    str1.download(output_path=
                  output_path)
    time2 = time.time() 
    time2 = time2 - time1

    print(f"Download complete in {time2} sec")

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

# write unit  test for on_progress function


def on_progress(stream, chunk, bytes_remaining): 
    total_size = stream.filesize
    bytes_downloaded = total_size - bytes_remaining
    per = bytes_downloaded/ total_size * 100 
    print(f"progress: {per:.2f}%")
def on_complete(stream, file_path):
    print(f"Download complete: {file_path}")


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

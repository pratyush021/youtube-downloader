import argparse
from pytube import YouTube

def download_video(url, output_path, resolution):
    yt = YouTube(url)
    print(yt.thumbnail_url)

    # video = yt.streams.filter(res=resolution, file_extension="mp4").first()
    # print(f"Downloading: {yt.title} ({resolution})")
    # video.download(output_path)
    # print("Download complete!")

def main():
    parser = argparse.ArgumentParser(description="YouTube Video Downloader")
    parser.add_argument("url", help="YouTube video URL")
    parser.add_argument("-o", "--output", default="./downloads", help="Output path for downloaded video")
    parser.add_argument("-r", "--resolution", default="720p", help="Video resolution (e.g., 720p, 1080p)")

    args = parser.parse_args()
    download_video(args.url, args.output, args.resolution)

if __name__ == "__main__":
    main()

# YOUTUBE DOWNLOADER 

## HOW TO USE: 
1. clone the repository in your local machine: 
```
git clone https://github.com/pratyush021/youtube-downloader.git
```
2. install the required libraries: 
```linux
pip install requests beautifulsoup4 pytube
```
3. Download any video using by running this in command line: 
```python
python3 download.py [URL] -o [OUTPUT LOCATION] -r [RESOLUTION]

```
1. python libraries used: Requests, Beautiful soup, pytube. 
	Requests: for HTTP requests to download the web page 
	Beautiful soup: for parsing HTML content 
	pytube: A library specifically designed to download youtube videos
	
2. Initial features: 
	1. accepet video url as input 
	2. fetch video info 
	3. selecting video quality 
	4. download the video 
	5. progress indicator
3. Not using DASH streams as I don't want to have to merge both audio and video codec. Once the core features are done, I'll do DASH. 



## DASH vs Progressive streams 
We have two options available for working  with media streams.
```python 
yt.streams
```
### Progressive streams: 
```
yt.streams.filter(progressive=True)
```
1. These are legacy streams that contain both video and audio codec. 
2. Only available for 720p and below resolution.

### DASH streams: 
```
yt.streams.filter(adaptive=True)
```
1. Stands for Dynamic Adaptive Streaming over HTTP
2. These streams have just video or audio codec. 
3. Both these audio and video tracks needs to be downloaded and post prossed them using FFmpeg to merge them.











### source: 
[pytube.io](https://pytube.io/en/latest/index.html)  <br>
chatGPT <br>
[tdqm](https://tqdm.github.io/)
from pytube import YouTube

def download_video(url):
    yt = YouTube(url)
    videos = yt.streams.all()
    video = list(enumerate(videos))
    
    for i in video:
        print(i)
          
    print("Enter the video you would like to download")
    download_format = int(input("Enter the format number: "))
    videos[download_format].download(max_retries=10)
    print("Downloaded video successfully")
    
if __name__ == "__main__":
    print("Enter the URL of the video you would like to download: ")
    url = input()
    download_video(url)
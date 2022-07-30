from pytube import YouTube
link = "https://www.youtube.com/watch?v=vMFegdwz7Tc"
yt = YouTube(link)
videos = yt.streams.all()
vid = list(enumerate(videos))
for i in vid:
    print(i)


strm = int(input("Enter:  "))
videos[strm].download()
print("Video Downloaded to current folder")
 
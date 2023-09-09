#import the package

from pytube import YouTube

yt = YouTube("https://www.youtube.com/watch?v=VuwboLzEM-0")

my_stream = yt.streams

for each_stream in my_stream:
  print(each_stream)

yt.streams.get_by_itag(18).download(filename="evil.mp4")

print(yt.title)
print(yt.thumbnail_url)
print(yt.author)


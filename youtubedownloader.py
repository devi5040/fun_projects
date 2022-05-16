from pytube import YouTube

link=input('Youtube Link: ')

def on_complete(stream, filepath):
	print("Download Complete")
	print("File stored in"+filepath)
def on_progress(stream, chunk, bytes_remaining):
	progress_string=f'{round(100-bytes_remaining/stream.filesize*100 ,2)}%'
	print(progress_string)

video_object=YouTube(link,on_complete_callback=on_complete,on_progress_callback=on_progress)

print(f'title:  {video_object.title}')
print(f'length: {round((video_object.length)/60)} minutes')
print(f'views:  {round((video_object.views)/1000000,2)} millions')
print(f'author: {video_object.author}')

print('download: (b)est | (w)orst| (a)udio | (e)xit')
download_choice=input('choice: ')

if download_choice=='b':
	video_object.streams.get_highest_resolution().download(r'D:\downloads')
elif download_choice=='w':
	video_object.streams.get_lowest_resolution().download(r'D:\downloads')
elif download_choice=="a":
	video_object.streams.get_audio_only().download(r'D:\downloads')
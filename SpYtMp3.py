from pytube import YouTube

#Takes Soptify Playlists Turns into youtube playlists into mp3s
def download_youtube_video_as_mp3(youtube_url, output_path):
    try:
        # Download YouTube video
        yt = YouTube(youtube_url)
        video = yt.streams.filter(only_audio=True).first()
        download_path = video.download(output_path=output_path)

        # Convert to MP3 using moviepy
        mp4_file = download_path
        mp3_file = f"{output_path}/{yt.title}.mp3"

        video_clip = VideoFileClip(mp4_file)
        audio_clip = video_clip.audio
        audio_clip.write_audiofile(mp3_file)

        # Close the clips
        audio_clip.close()
        video_clip.close()

        # Optionally, you might want to delete the original mp4 file
        # import os
        # os.remove(mp4_file)

        return mp3_file
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
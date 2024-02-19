import os
import pandas as pd
from googleapiclient.discovery import buildp
from pytube import YouTube

api_key = os.environ.get('youtube_api')
youtube = build('youtube', 'v3', developerKey=api_key)


def download(data):
    ids = []
    for song_name in data:
        print("Scraping the ID of song: " + song_name)
        request = youtube.search().list(q=song_name, part='id', type='video', maxResults=1)
        response = request.execute()

        if response['items']:
            video_id = response['items'][0]['id']['videoId']
            print(f"Found video ID: {video_id}")
            ids.append(video_id)
        else:
            print("No YouTube video found.")
            ids.append(None)
    print("scrapping of ids is done")
    print(ids)
    print("downloading songs")
    return downloadusingid(ids)


def downloadusingid(video_ids):
    base_url = "https://www.youtube.com/watch?v="
    for video_id in video_ids:
        video_url = base_url + video_id
        print(f"Downloading audio for: {video_url}")
        yt = YouTube(video_url)
        video = yt.streams.filter(only_audio=True).first()
        out_file = video.download()
        base, ext = os.path.splitext(out_file)
        new_file = base + ".mp3"
        os.rename(out_file, new_file)
        print("\nSuccessfully Downloaded\n")



if __name__ == '__main__':
    df = pd.read_csv('songs.csv')
    data = df['Song Names'].tolist()
    print(data)
    download(data)

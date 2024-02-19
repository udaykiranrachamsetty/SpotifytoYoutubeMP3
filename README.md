# Spotify YouTube Downloader

This is a Python application that allows users to download audio tracks from YouTube based on their Spotify saved tracks.

## Prerequisites

Before running the application, make sure you have Python installed on your system. Additionally, ensure that you have the following dependencies installed:

- Flask
- Spotipy
- html5lib
- Requests
- BeautifulSoup4
- pytube
- google-api-python-client
- pandas
- pyarrow


## Spotify and YouTube API Credentials

To use this application, you'll need to obtain API credentials for both Spotify and YouTube. Follow these steps to obtain the required credentials:

### Spotify API

1. Go to the [Spotify Developer Dashboard](https://developer.spotify.com/dashboard/) and log in with your Spotify account or create a new one.
2. Create a new application and note down the client ID and client secret.
3. Set the redirect URI to `http://localhost:5000/redirect` or any other URI specified in the application.

### YouTube API

1. Go to the [Google Cloud Console](https://console.cloud.google.com/) and create a new project.
2. Enable the YouTube Data API v3 for your project.
3. Create credentials for your project and select "API key". Note down the API key generated.

Once you have obtained the API credentials, set them as environment variables named `SPOTIFY_CLIENT_ID`, `SPOTIFY_CLIENT_SECRET`, and `YOUTUBE_API_KEY` respectively.

## Installation

To install the required dependencies, run the following command:

```bash
python install_packages.py
```

## Usage

1. Run the Flask application by executing the `app.py` file:

    ```bash
    python app.py
    ```

2. Open a web browser and navigate to [http://localhost:5000](http://localhost:5000) to initiate the Spotify authentication process.

3. Log in with your Spotify credentials and authorize the application to access your saved tracks.

4. Once authenticated, the application will fetch your saved tracks from Spotify and create a CSV file named `songs.csv`.

5. After the CSV file is generated, the application will download the corresponding audio tracks from YouTube and save them as MP3 files in the `downloads` directory.



import time
import pandas as pd
import spotipy
from flask import Flask, url_for, redirect, session, request
from spotipy.oauth2 import SpotifyOAuth
import os

app = Flask(__name__)

# Retrieve client ID and secret from environment variables
SPOTIFY_CLIENT_ID = os.environ.get('client_id')
SPOTIFY_CLIENT_SECRET = os.environ.get('client_secret_key')
TOKEN_INFO = "TOKEN"
print(SPOTIFY_CLIENT_SECRET)
print(SPOTIFY_CLIENT_ID)

# Set up Flask app configuration
app.config['SECRET_KEY'] = os.urandom(24)
app.config['SESSION_COOKIE_NAME'] = 'spotify_login_session'


def create_spotify_oauth():
    """Creates and returns a SpotifyOAuth object configured with our app's credentials."""
    return SpotifyOAuth(
        client_id=SPOTIFY_CLIENT_ID,
        client_secret=SPOTIFY_CLIENT_SECRET,
        scope='user-library-read',
        redirect_uri=url_for('redirectPage', _external=True))


@app.route('/')
def login():
    auth = create_spotify_oauth()
    auth_url = auth.get_authorize_url()
    return redirect(auth_url)


@app.route('/redirect')
def redirectPage():
    auth = create_spotify_oauth()
    session.clear()
    code = request.args.get('code')
    token_info = auth.get_access_token(code)
    if token_info:
        session[TOKEN_INFO] = token_info
        return redirect(url_for('gettracks'))
    else:
        return "Failed to obtain access token."


@app.route('/gettracks')
def gettracks():
    try:
        token_info = get_token()  # Ensure get_token() is properly defined elsewhere
    except Exception as e:
        print("User not logged in or another error occurred:", e)
        return redirect('/')

    if token_info:
        sp = spotipy.Spotify(auth=token_info.get('access_token'))
        results = []
        offset = 0

        while True:
            curGroup = sp.current_user_saved_tracks(limit=50, offset=offset)['items']
            if not curGroup:
                break
            for item in curGroup:
                track = item['track']
                val = track['name'] + " - " + track['artists'][0]['name']
                results.append(val)

            offset += 50

        if results:
            df = pd.DataFrame(results, columns=["Song Names"])
            df.to_csv('songs.csv', index=False)
            return "Done"
        else:
            return "No tracks found."
    else:
        return "Token info was not obtained."


def get_token():
    token_info = session.get(TOKEN_INFO, None)
    if not token_info:
        raise "exception"
    now = int(time.time())
    is_expired = token_info['expires_at'] - now < 60
    if is_expired:
        auth = create_spotify_oauth()
        token_info = auth.refresh_access_token(token_info['refresh_token'])
    return token_info


if __name__ == '__main__':
    app.run(debug=True)

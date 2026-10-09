import requests
from flask import Flask, jsonify
from flask_cors import CORS
import os
import spotipy
from spotipy.oauth2 import SpotifyOAuth
from dotenv import load_dotenv
load_dotenv()



app = Flask(__name__)
CORS(app)

CLIENT_ID = os.environ["ClientId"]
CLIENT_SECRET = os.environ["ClientSecret"]

REDIRECT_URI =  "http://localhost:8888/callback"



sp = spotipy.Spotify(auth_manager=SpotifyOAuth(
    client_id=CLIENT_ID,
    client_secret=CLIENT_SECRET,
    redirect_uri=REDIRECT_URI,
    scope="user-read-currently-playing user-read-recently-played",
    cache_path=".spotify_cache",  # stores your token here after first login
))



print(sp.current_user_playing_track()) 

@app.route("/spotifyGet")
def now_playing():
    current = sp.current_user_playing_track()

    if current and current.get("item"):
        item = current["item"]
        return jsonify({
            "isPlaying": True,
            "name": item["name"],
            "artist": ", ".join(a["name"] for a in item["artists"]),
            "albumArt": item["album"]["images"][0]["url"],
            "url": item["external_urls"]["spotify"],
        })

    # nothing playing -> fall back to recently played
    recent = sp.current_user_recently_played(limit=1)
    track = recent["items"][0]["track"]
    return jsonify({
        "isPlaying": False,
        "name": track["name"],
        "artist": ", ".join(a["name"] for a in track["artists"]),
        "albumArt": track["album"]["images"][0]["url"],
        "url": track["external_urls"]["spotify"],
    })


if __name__ == "__main__":
    app.run(port=5000, debug=True)
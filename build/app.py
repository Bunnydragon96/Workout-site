##Creating an exercise routine website using HTMl and Jinja blocks.
##Johnel Cunningham Rivera @1/29/2026
##Johnel Cunningham River Modified@5/1/2026

import os
import requests
from flask import Flask, render_template
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

YOUTUBE_API_KEY = os.getenv("YOUTUBE_API_KEY")
PLAYLIST_ID = os.getenv("PLAYLIST_ID")

def get_playlist_videos():
    url = "https://www.googleapis.com/youtube/v3/playlistItems"
    params = {
        "part": "snippet",
        "playlistId": PLAYLIST_ID,
        "maxResults": 20,
        "key": YOUTUBE_API_KEY
    }
    res = requests.get(url, params=params)
    items = res.json().get("items", [])

    videos = []
    for item in items:
        snippet = item["snippet"]
        vid_id = snippet["resourceId"]["videoId"]
        videos.append({
            "title": snippet["title"],
            "url": f"https://www.youtube.com/watch?v={vid_id}"
        })
    return videos

##List pages of easy, medium, full, and pushup triangle.
@app.route("/")
def start_page():
    videos = get_playlist_videos()
    return render_template("warmup.html", videos=videos)

@app.route("/easy")
def easy_workout():
    return render_template("123exercise-easy.html")

@app.route("/medium")
def medium_workout():
    return render_template("123exercise-medium.html")

@app.route("/full")
def full_workout():
    return render_template("123exercise-full.html")

@app.route("/triangle")
def triangle_workout():
    return render_template("pushuptriangle.html")

if __name__ == "__main__":
    app.run()

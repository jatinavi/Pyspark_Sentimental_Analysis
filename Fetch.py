import json
import pandas as pd
from googleapiclient.discovery import build
import os
os.makedirs("data", exist_ok=True)

# ✅ Load API key from file
with open("key.json") as f:
    key = json.load(f)["API_KEY"]

# ✅ Build YouTube API client
youtube = build("youtube", "v3", developerKey=key)

# ✅ Extract video ID from YouTube URL
def get_video_id(url):
    return url.split("v=")[-1]

# ✅ Fetch top-level comments using YouTube Data API
def get_comments(video_url, max_results=100):
    video_id = get_video_id(video_url)
    comments = []

    response = youtube.commentThreads().list(
        part="snippet",
        videoId=video_id,
        maxResults=100,
        textFormat="plainText"
    ).execute()

    while response:
        for item in response["items"]:
            comment = item["snippet"]["topLevelComment"]["snippet"]["textDisplay"]
            comments.append(comment)

        # Fetch next page if available
        if "nextPageToken" in response and len(comments) < max_results:
            response = youtube.commentThreads().list(
                part="snippet",
                videoId=video_id,
                pageToken=response["nextPageToken"],
                maxResults=100,
                textFormat="plainText"
            ).execute()
        else:
            break

    return comments

# ✅ Save comments to CSV
def save_to_csv(comments):
    df = pd.DataFrame(comments, columns=["comment"])
    df.to_csv("data/comments.csv", index=False)
    print("✅ Saved comments.csv with", len(df), "comments")

# ✅ Main script
if __name__ == "__main__":
    url = input("Paste YouTube video URL: ")
    comments = get_comments(url)
    save_to_csv(comments)

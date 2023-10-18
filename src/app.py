import os
import sys
from sqlalchemy import create_engine
import pandas as pd
from dotenv import load_dotenv
import seaborn as sns
import spotipy
from spotipy.oauth2 import SpotifyClientCredentials

# load the .env file variables
load_dotenv()
client_id = os.environ.get("CLIENT_ID")
client_secret = os.environ.get("CLIENT_SECRET")

spotify = spotipy.Spotify(client_credentials_manager=SpotifyClientCredentials(client_id = client_id, client_secret=client_secret))

TOOL = 'spotify:artist:2yEwvVSSSUkcLeSTNyHKh8'
results = spotify.artist_top_tracks(TOOL)

names = []
popularities = []
durations = []

for track in results['tracks'][:10]:
    name = names.append(track['name'])
    popularity = popularities.append(track['popularity'])
    duration = durations.append(round(track['duration_ms'] / 60000, 2))



df = pd.DataFrame(list(zip(names, popularities, durations)), columns =['Name', 'Popularity', 'Duration'])
df = df.sort_values('Popularity', ascending=False)
print(df)
print(df.head(3))



scatter_plot = sns.scatterplot(data = df, x = "Popularity", y = "Duration")
fig = scatter_plot.get_figure()
fig.savefig("scatter_plot.png")

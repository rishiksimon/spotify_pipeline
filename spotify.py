from spotipy.oauth2 import SpotifyClientCredentials
import spotipy
import pandas as pd
import matplotlib.pyplot as plt
import re

# set up your credentials
sp = spotipy.Spotify(auth_manager=SpotifyClientCredentials(
    client_id="7484c2eac5334c65be79b75aa0317593",
    client_secret="e97abd16857e44039b84029b5af3142d"
))

# full track URL(example: channa mereya by arjith singh)
track_url = "https://open.spotify.com/track/003vvx7Niy0yvhvHt4a68B"

track_id = re.search(r"track/([a-zA-Z0-9]+)", track_url).group(1)

track = sp.track(track_id)
print(track)

# extract metadata
track_data = {
    'Track Name': track['name'],
    'Artist': ", ".join([artist['name'] for artist in track['artists']]),
    'Album': track['album']['name'],
    'Popularity': track['popularity'],
    'Duration (minutes)': track['duration_ms'] / 60000
}

# Display metadata
print(f"\nTrack Name: {track_data['Track Name']}")
print(f"Artist: {track_data['Artist']}")
print(f"Album: {track_data['Album']}")
print(f"Popularity: {track_data['Popularity']}")
print(f"Duration: {track_data['Duration (minutes)']:.2f} minutes")


# convert metadata to dataframe
df = pd.DataFrame([track_data])
print("\nTrack Data as DataFrame:")
print(df)

# save as CSV
df.to_csv('spotify_track_data.csv', index=False)

# visualize the track
features = ['Popularity', 'Duration (minutes)']
values = [track_data['Popularity'], track_data['Duration (minutes)']]

plt.figure(figsize=(8,5))
plt.bar(features, values, color='skyblue', edgecolor='black')
plt.title(f"Track Metadata for '{track_data['Track Name']}'")
plt.ylabel('value')
plt.show()

```python
# Import necessary modules
import random

class Playlist:
    def __init__(self):
        # Initialize an empty playlist
        self.playlist = []

    def create_playlist(self, curated_music):
        # This function should create a playlist from the curated music
        self.playlist = curated_music

        # Log the created playlist
        print(f'Created playlist: {self.playlist}')

        return self.playlist

    def update_playlist(self, playlist, wellness_data):
        # This function should update the playlist based on wellness data
        # For the sake of this example, we will randomly shuffle the playlist
        random.shuffle(playlist)

        # Log the updated playlist
        print(f'Updated playlist: {playlist}')

        return playlist

    def display_playlist(self, playlist):
        # This function should display the playlist to the user
        print(f'Your playlist: {playlist}')
```

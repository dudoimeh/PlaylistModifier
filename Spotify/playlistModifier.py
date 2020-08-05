"""
step 1: get main playlist ID (p1)
step 2: get playlist to add (p2)
step 3: loop through p2 and add each song IF not in p1
step 4: delete p2? 
"""

import json, requests
from tkinter import *


class PlaylistModifier():
    #each time you modify a playlist, you need a new access token
    def __init__(self):
        secrets = {}
        with open("C:/Users/dudoi/OneDrive/Desktop/python/Spotify/secrets.txt", "r") as f:
            for line in f:
                (key, val) = line.strip().split(":", 1)
                secrets[key] = val
        self.userID = secrets["userID"]
        self.accessToken = secrets["accessToken"]
        self.mainPlaylist = secrets["playlist1ID"]
        self.secondPlaylist = secrets["playlist2ID"]
        self.exampleSong = secrets["photosynthesisID"]
        self.commmand = secrets["command"]

    def getP2Songs(self):
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(self.secondPlaylist)
        response = requests.get(
            query,
            headers={
                "Authorization": "Bearer {}".format(self.accessToken)
            }
        )
        responseJson = response.json()
        songs = []
        for item in responseJson["items"]:
            songs.append(item["track"]["id"])
        for i in range(len(songs)):
            songs[i] = "spotify:track:" +songs[i]
        return songs

    def addSongs(self, songsToAdd):
        # for now, this function assumes there are no duplicates between either playlist
        requestData = json.dumps(songsToAdd)
        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(self.mainPlaylist)
        response = requests.post(
            query,
            data=requestData,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.accessToken)
            }
        )
        return response

    def deleteSongs(self, songsToDelete):
        # the uris must be passed in the request body as a LIST of DICTIONARIES
        uris = []
        for song in songsToDelete:
            dictionary = {"uri": song}
            uris.append(dictionary)
        requestBody = json.dumps({
            "tracks": uris
        })

        query = "https://api.spotify.com/v1/playlists/{}/tracks".format(self.mainPlaylist)
        response = requests.delete(
            query,
            data=requestBody,
            headers={
                "Content-Type": "application/json",
                "Authorization": "Bearer {}".format(self.accessToken)
            }
        )
        return response

    def combinePlaylists(self):
        songs = self.getP2Songs()
        ifCombinedPlaylists = self.addSongs(songs)
        return ifCombinedPlaylists
    
    def subtractPlaylists(self):
        songs = self.getP2Songs()
        ifSubtractedPlaylists = self.deleteSongs(songs)
        return ifSubtractedPlaylists

def main():
    pass

if __name__ == "__main__":
    main()
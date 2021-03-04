# kexp_spotify_sync
Syncing liked tracks from KEXP app into a Spotify playlist

It kind of works?  Super messy because I haven't written Python in a very long time.  

## Setup
1. Export favorite tracks in KEXP app (Share menu), place in script directory 
2. Edit sync.py with desired playlist ID
3. Set client id / client secret / redirect URL environment variables
4. run script using given "KexpSavedTracks.html" file
5. Check KEXP playlist + errors.txt to manually add missed tracks


## TODO
1. ~~Create KEXP playlist if it doesn't already exist (Alternatively, create a new one with current date)~~
2. ~~Find KEXP playlist, stop hardcoding in the playlist ID~~ kind of implemented
3. Either check for existing tracks and only add new ones, or delete existing tracks to prevent duplicates
4. ~~Output out failed track additions with error code to diagnose~~ errors.txt will contain missing tracks
5. Improve code quality
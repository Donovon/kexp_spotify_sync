# kexp_spotify_sync
Syncing liked tracks from KEXP app into a Spotify playlist

It kind of works?  Super messy because I haven't written Python in a very long time.  
Usage: Export favorite tracks in KEXP app, run script using given "KexpSavedTracks.html" file

## TODO
1. Create KEXP playlist if it doesn't already exist (Alternatively, create a new one with current date)
2. Find KEXP playlist, stop hardcoding in the playlist ID 
3. Either check for existing tracks and only add new ones, or delete existing tracks to prevent duplicates
4. Output out failed track additions with error code to diagnose
5. Improve code quality
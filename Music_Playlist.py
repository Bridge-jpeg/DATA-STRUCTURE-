#Author: Lyndo M. Lusac 
#Description: This program creates a playlist that searches for your desired song, plays the song,
#               and displays your playlist.
#Date of submission: May 10, 2025

class SongNode(object):     
    def __init__(self, title, next = None):
        self.title = title 
        self.next = next

class PlayList:
    def __init__(self):
        self.head = None
    def add_song(self, title):      # adds the songs desired by the suer in the Playlist
        new_SongNode = SongNode(title)
        if self.head == None:
            self.head = new_SongNode
            return
        add_SongNode = self.head 
        while add_SongNode.next != None:
            add_SongNode = add_SongNode.next
        add_SongNode.next = new_SongNode 
    
    def play_song(self, title):     # searches for the song and plays the song if it exists
        song = self.head
        while song != None and title != song.title:
            song = song.next
        if song != None:
            print(f"Now playing: {song.title}")     # plays the song if exist 
        else:
            print(f"Song not found ")       # returns this print statement if the song does not exist

    def display_playlist(self):     # displays all the songs in the playlist
        song = self.head
        print("Your Playlist: ")
        while song != None:     # checks all the songs
            if song != None:
                print(f'> {song.title}')        # prints the songs 
            else:
                print("Playlist is empty")      # returns this print statement if the playlsit is empty
            song = song.next

# Main method           
lynds = PlayList()      # instance of the class Playlist()
# Songs in the Playlist
# Adds songs using the method add_song()
lynds.add_song("Multo")     
lynds.add_song("Enchanted")
lynds.add_song("Iris")
lynds.add_song("Marilag")
lynds.add_song("Let Her Go")

# Plays the songs in the Playlist using play_song()
lynds.play_song("Iris")     # Searches for the existing song in the Playlist
lynds.play_song("You'll be safe here")      # Searches for the non-existing song in the Playlist

# Displays the Playlist using display_playlist()
lynds.display_playlist()        
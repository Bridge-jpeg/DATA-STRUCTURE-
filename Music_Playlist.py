#Author: Lyndo M. Lusac 
#Description: (brief description of the program) 
#Date of submission: 

class SongNode(object):
    def __init__(self, title, next = None):
        self.title = title 
        self.next = next

class PlayList:
    def __init__(self):
        self.head = None
    def add_song(self, title):
        new_SongNode = SongNode(title)
        if self.head == None:
            self.head = new_SongNode
            return
        add_SongNode = self.head 
        while add_SongNode.next != None:
            add_SongNode = add_SongNode.next
        add_SongNode.next = new_SongNode 
    
    def play_song(self, title):
        song = title
        while song != None and song != song.data:
            song = song.link
        if song != None:
            print(f"Now playing: {song.data} ")
        else:
            print(f"Song not found: {song.data} ")

    def display_playlist(self):
        song = self.head
        while song != None:
            if song != None:
                print(song.data, end = ">")
            else:
                print("Playlist is empty")

lynds = PlayList()
lynds.add_song("Multo")
lynds.add_song("Enchanted")
lynds.add_song("Iris")
lynds.add_song("Marilag")
lynds.add_song("Let Her Go")

lynds.play_song("iris")
lynds.play_song("You'll be safe here")

lynds.display_playlist()
class PlaylistObj:

    pl_len = 0
    coverUrl = ''
    tracks = []


    def __init__(self, name):
        self.name = name

    def setLen(self, plLength):
        self.pl_len = plLength

    def setURL(self, urlAddr):
        self.coverUrl = urlAddr

    def addTracks(self, tracklist):
        self.tracks = []
        for obj in tracklist:
            self.tracks.append(obj)

        self.setLen(len(self.tracks))

    def displayInfo(self):
        print(self.name)
        print(self.pl_len)
        print(self.coverUrl)
        for items in self.tracks:
            print((items))
        
    def dispName(self):
        print(self.name)   
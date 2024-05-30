import SongObj

class PlaylistObj:

    pl_len = 0
    coverUrl = ''
    tracks = []
    trackObjs = []


    def __init__(self, name):
        self.name = name

    def setLen(self, plLength):
        self.pl_len = plLength

    def setURL(self, urlAddr):
        self.coverUrl = urlAddr

    def addTracks(self, tracklist):
        self.tracks = tracklist
        self.setLen(len(self.tracks))

    def addTrackObj(self, trObj):
        self.trackObjs = trObj

    def displayInfo(self):
        print(self.name)
        print(self.pl_len)
        print(self.coverUrl)
        for items in self.tracks:
            print((items))
        
    def dispName(self):
        print(self.name)   

    def dispObjs(self):
        for item in self.trackObjs:
            item.displayDetail()

    def getSongs(self):
        return self.trackObjs
    
    def getName(self):
        return self.name
    
    def getCoverUrl(self):
        return self.coverUrl
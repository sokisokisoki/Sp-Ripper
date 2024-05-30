class SongObj:
    track_length = 0
    artists = []

    def __init__(self, name):
        self.name = name

    def setTrackLen(self, length):
        self.track_length = length

    def addArtists(self, artistList):
        self.artists = artistList

    def convertTrackTime(self, trTime):
        seconds = trTime / 1000
        minutes, remaining_seconds = divmod(seconds, 60)
        print(f"Track Time: {int(minutes)}:{int(remaining_seconds):02}")

    def displayDetail(self):
        print('Song Name: ' + self.name)
        self.convertTrackTime(self.track_length)
        #print("Artists:", self.artists)
        # print("Artists: ", end='')
        # print("".join(self.artists), sep=', ')
        if type(self.artists) == list:
            aL = ', '.join(self.artists)
            print("Artists:", aL)
        else:
            print("Artist:", self.artists)
        
        
        print("Query: ", self.createSearchQuery())

        print()

    def createSearchQuery(self):
        query = self.name + " "
        if type(self.artists) == list:
            query += ' '.join(self.artists)
        else:
            query += self.artists
        return query
    
    def getTrankLen(self):
        return self.track_length
    
    def getAdjTrLen(self):
        return self.track_length/1000
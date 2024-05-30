from pytube import Search
from SongObj import SongObj
from PlaylistObj import PlaylistObj

class YtObj:

    def __init__(self, name, tracks):
        self.name = name
        self.tracks = tracks

    #returns top three results
    def searcher(SearchTarget):
        hits = Search(SearchTarget)
        f2 = hits.results[:3]
        return f2

    #caramel emotions Forth Wanderers
    # output = searcher('nodding off by narrow head')

    # print(output)

    def bestMatch(self, hits, AdjustedSongDuration):
        closest = None
        for num in hits:
            result = AdjustedSongDuration - hits.length

            if closest_to_zero is None or abs(result) < abs(closest):
                closest_to_zero = result
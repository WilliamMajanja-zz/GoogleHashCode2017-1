class Video:

    def __init__(self, size):
        self.size = size
        self.caches = []

    def addCache(self, idc):
        self.caches.append(idc)

class Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.used = 0
        self.endpoints = {}
        self.videos = {}
        self.solution = []

    def addEndpoint(self, ide, latency):
        self.endpoints[ide] = latency

    def addVideo(self, idv, size):
        self.videos[idv] = size
        self.used += size

    def getEndpoints(self):
        return self.endpoints

    def getVideos(self):
        return self.videos

    def getSolution(self):
        return self.solution


class Endpoint:

    def __init__(self, latency):
        self.latency = latency
        self.videos = {}
        self.caches = {}

    def addVideo(self, idv, size):
        self.videos[idv] = size

    def addCache(self, idc, latency):
        self.caches[idc] = latency

    def getVideos(self):
        return self.videos

    def getCaches(self):
        return self.caches

def main():
    endpoints = []
    caches = []
    files = ["me_at_the_zoo.in", "videos_worth_spreading.in", "trending_today.in", "kittens.in"]
    print("Start of parsing")

    with open(files[0], 'r') as f:
        nVideos, nEndpoints, nRequests, nCaches, cacheSize = map(int, f.readline().split(' '))
        #print(nVideos, nEndpoints, nRequests, nCaches, cacheSize)

        for i in range(nCaches):
            c = Cache(cacheSize)
            caches.append(c)

        videos = list(map(int, f.readline().split(' ')))
        #print(videos)

        for i in range(nEndpoints):
            lat, connectedCaches = map(int, f.readline().split(' '))
            #print(lat, connectedCaches)
            e = Endpoint(lat)
            for j in range(connectedCaches):
                idc, latc = map(int, f.readline().split(' '))
                #print(idc, latc)
                e.addCache(idc, latc)
                caches[idc].addEndpoint(i, latc)
            endpoints.append(e)

        for i in range(nRequests):
            idv, ide, rNum = map(int, f.readline().split(' '))
            #print(idv, ide, rNum)
            endpoints[ide].addVideo(idv, rNum)

    print("End of parsing")


    print("Start of bestemmie")


if __name__ == "__main__":
    main()


class Video:

    def __init__(self, size):
        self.size = size
        self.caches = []

    def addCache(self, idc):
        self.caches.append(idc)

class Cache:

    def __init__(self, capacity):
        self.capacity = capacity
        self.endpoints = {}
        self.videos = {}
        self.solution = []
        self.orded = []
        self.used = 0

    def addEndpoint(self, ide, latency):
        self.endpoints[ide] = latency

    def addVideo(self, idv, weight):
        self.videos[idv] = weight

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
        self.assigned = {}

    def addVideo(self, idv, req):
        self.videos[idv] = req

    def addCache(self, idc, latency):
        self.caches[idc] = latency

    def addAssignation(self, idv, idc):
        self.assigned[idv] = idc

    def getVideos(self):
        return self.videos

    def getCaches(self):
        return self.caches

def main():
    endpoints = []
    caches = []
    videos = []
    files = ["me_at_the_zoo", "videos_worth_spreading", "trending_today", "kittens"]
    print("Start of parsing")
    ff = 0
    with open(files[ff] + ".in", 'r') as f:
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

    for cache in caches:
        for endpoint in cache.getEndpoints().items():
            for video in endpoints[endpoint[0]].getVideos().items():
                #print(video)
                if video[0] in cache.getVideos().keys():
                    cache.getVideos()[video[0]] += video[1]*(endpoints[endpoint[0]].latency-endpoint[1])/videos[video[0]]
                else:
                    cache.addVideo(video[0], video[1]*(endpoints[endpoint[0]].latency-endpoint[1])/videos[video[0]])

    for cache in caches:
        #print(i, sorted(cache.getVideos().items(), key=lambda x:x[1], reverse=True))
        cache.orded = sorted(cache.getVideos().items(), key=lambda x:x[1], reverse=True)
        i = 0
        while cache.used < cacheSize and i < len(cache.orded):
            if cache.used + videos[cache.orded[i][0]] < cacheSize:
                cache.solution.append(cache.orded[i][0])
                cache.used += videos[cache.orded[i][0]]
            i = i + 1

    invalid = 0
    for i, cache in enumerate(caches):
        summa = 0
        for i in cache.solution:
            summa += videos[i]
            #print((videos[i]))
        assert summa < cacheSize
        if summa == 0:
            invalid = invalid + 1
        #print(summa)

    #print(nCaches-invalid)
    with open(files[ff] + ".out", "w") as out:
        out.write(str(nCaches-invalid) + '\n')
        for i, cache in enumerate(caches):
            out.write(str(i) + " " + " ".join([str(i) for i in cache.solution]) + '\n')


if __name__ == "__main__":
    main()

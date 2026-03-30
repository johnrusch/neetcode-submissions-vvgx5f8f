class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweets[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        
        users = {userId} | self.follow_map.get(userId, set())

        for uid in users:
            tweets = self.tweets.get(uid, [])
            if tweets:
                idx = len(tweets) - 1

                ts, tid = tweets[idx]
                heapq.heappush(heap, (-ts, tid, uid, idx))

        res = []
        while heap and len(res) < 10:
            neg_ts, tid, uid, idx = heapq.heappop(heap)
            res.append(tid)

            if idx > 0:
                idx -= 1
                ts, tid = self.tweets[uid][idx]
                heapq.heappush(heap, (-ts, tid, uid, idx))

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)

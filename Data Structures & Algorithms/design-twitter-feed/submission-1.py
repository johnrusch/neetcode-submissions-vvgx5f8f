class Twitter:

    def __init__(self):
        self.time = 0
        self.tweets = defaultdict(list)
        self.follow_map = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        heapq.heappush(self.tweets[userId], (self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        feed = []
        
        feed.extend(self.tweets.get(userId, []))

        for followeeId in self.follow_map.get(userId, set()):
            feed.extend(self.tweets.get(followeeId, []))

        top10 = heapq.nlargest(10, feed)

        return [tweetId for timestamp, tweetId in top10]


    def follow(self, followerId: int, followeeId: int) -> None:
        if followerId != followeeId:
            self.follow_map[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].discard(followeeId)

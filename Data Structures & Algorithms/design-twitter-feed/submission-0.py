class Twitter:

    def __init__(self):
        self.follow_map = defaultdict(set)
        self.tweet_map = defaultdict(list)
        self.time = 0
        

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.tweet_map[userId].append((self.time, tweetId))
        self.time += 1

    def getNewsFeed(self, userId: int) -> List[int]:
        followees = self.follow_map[userId]
        followees.add(userId)
        tweets = []
        for followee in followees:
            tweets += self.tweet_map[followee]
        
        heapq.heapify_max(tweets)
        feed = []
        while tweets and len(feed) < 10:
            feed.append(heapq.heappop_max(tweets)[1])
        
        return feed

        

    def follow(self, followerId: int, followeeId: int) -> None:
        self.follow_map[followerId].add(followeeId)
        
    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.follow_map[followerId]:
            self.follow_map[followerId].remove(followeeId)
        

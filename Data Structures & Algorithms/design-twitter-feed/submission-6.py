class Twitter:

    def __init__(self):
        self.users = defaultdict(set)
        self.tweets = defaultdict(list)
        self.count = 0


    def postTweet(self, userId: int, tweetId: int) -> None:
            self.count -= 1
            self.tweets[userId].append((self.count,tweetId))


    def getNewsFeed(self, userId: int) -> List[int]:
        heap = []
        users_to_check = self.users[userId] | {userId}
        
        for uid in users_to_check:
            for tweet in self.tweets[uid][-10:]:
                heapq.heappush(heap, tweet)

        res = []
        while heap and len(res) < 10:
            res.append(heapq.heappop(heap)[1])

        return res


    def follow(self, followerId: int, followeeId: int) -> None:
        self.users[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.users[followerId]:
            self.users[followerId].remove(followeeId)


        

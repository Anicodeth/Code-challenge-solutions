class Twitter:

    def __init__(self):
      self.following = defaultdict(set)
      self.feed = []

    def postTweet(self, userId: int, tweetId: int) -> None:
      self.feed.append([userId, tweetId])
        

    def getNewsFeed(self, userId: int) -> List[int]:
      res = []
      count = 0
      end = len(self.feed) - 1
      while count < 10 and end >= 0:
        if self.feed[end][0] in self.following[userId] or self.feed[end][0] == userId:
          res.append(self.feed[end][1])
          count += 1

        end -= 1

      return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.following[followerId].add(followeeId)
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
      if followerId in self.following and followeeId in self.following[followerId]:
        self.following[followerId].remove(followeeId)
        

        


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)

from typing import List
class Twitter:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.tweets = {}
        self.time = 1
        self.follow_table = {}

        
    def postTweet(self, userId: int, tweetId: int) -> None:
        """
        Compose a new tweet.
        """
        self.tweets[userId] = self.tweets.get(userId,[])+[(self.time,tweetId)]
        self.time+=1
        

    def getNewsFeed(self, userId: int) -> List[int]:
        """
        Retrieve the 10 most recent tweet ids in the user's news feed. Each item in the news feed must be posted by users who the user followed or by the user herself. Tweets must be ordered from most recent to least recent.
        """
        if userId in self.tweets:
            all_tweets = self.tweets[userId].copy()
        else:
            all_tweets = []
        if userId in self.follow_table:
            for user in list(self.follow_table[userId]):
                all_tweets.extend(self.tweets[user])
        all_tweets.sort(reverse=True)
        return [all_tweets[a][1] for a in range(min(len(all_tweets),10))]


    def follow(self, followerId: int, followeeId: int) -> None:
        """
        Follower follows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId!=followeeId:
            if followerId in self.follow_table:
                self.follow_table[followerId].add(followeeId)
            else:
                self.follow_table[followerId] = set([followeeId])
        

    def unfollow(self, followerId: int, followeeId: int) -> None:
        """
        Follower unfollows a followee. If the operation is invalid, it should be a no-op.
        """
        if followerId in self.follow_table and followeeId in self.follow_table[followerId]:
            self.follow_table[followerId].remove(followeeId)

        
# Your Twitter object will be instantiated and called as such:
obj = Twitter()
obj.postTweet(1,5)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.follow(1,2)
obj.postTweet(2,6)
param_2 = obj.getNewsFeed(1)
print(param_2)
obj.unfollow(1,2)
param_2 = obj.getNewsFeed(1)
print(param_2)
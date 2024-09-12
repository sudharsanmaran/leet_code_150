from collections import defaultdict, deque
import heapq
from typing import List


class Twitter:

    def __init__(self):
        self.count = 0
        self.tweets = defaultdict(deque)
        self.followers = defaultdict(set)

    def postTweet(self, userId: int, tweetId: int) -> None:
        self.count -= 1
        self.tweets[userId].append((self.count, tweetId))

    def getNewsFeed(self, userId: int) -> List[int]:
        feeds, res = [], []
        # adding last tweet of all followee
        self.followers[userId].add(userId)
        for followeeId in self.followers[userId]:
            if followeeId not in self.tweets:
                continue

            last_index = len(self.tweets[followeeId]) - 1
            count, tweet_id = self.tweets[followeeId][last_index]
            heapq.heappush(
                feeds, (count, tweet_id, followeeId, last_index - 1))

        while feeds and len(res) < 10:
            count, tweet_id, followeeId, last_index = heapq.heappop(feeds)
            res.append(tweet_id)
            if last_index >= 0:
                count, tweet_id = self.tweets[followeeId][last_index]
                heapq.heappush(
                    feeds, (count, tweet_id, followeeId, last_index - 1))
        return res

    def follow(self, followerId: int, followeeId: int) -> None:
        self.followers[followerId].add(followeeId)

    def unfollow(self, followerId: int, followeeId: int) -> None:
        if followeeId in self.followers[followerId]:
            self.followers[followerId].remove(followeeId)


"""
["Twitter","postTweet","postTweet","getNewsFeed"]
[[],[1,5],[1,3],[1]]
"""

obj = Twitter()
obj.postTweet(1, 5)
obj.postTweet(1, 3)
print(obj.getNewsFeed(1))

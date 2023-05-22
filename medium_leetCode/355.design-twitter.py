#
# @lc app=leetcode id=355 lang=python
#
# [355] Design Twitter
#
# self.post_stack.append((userId, tweetId))

# @lc code=start
class Twitter(object):

    def __init__(self):
        self.post_stack = []
        self.connections = {}

    def postTweet(self, userId, tweetId):
        """
        :type userId: int
        :type tweetId: int
        :rtype: None
        """
        self.post_stack = [(userId, tweetId)] + self.post_stack

    def getNewsFeed(self, userId):
        """
        :type userId: int
        :rtype: List[int]
        """

        return [tId for (uId, tId) in self.post_stack if userId ==
                uId or uId in self.connections.get(userId, set())][:10]

    def follow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId not in self.connections:
            self.connections[followerId] = set()

        self.connections[followerId].add(followeeId)

    def unfollow(self, followerId, followeeId):
        """
        :type followerId: int
        :type followeeId: int
        :rtype: None
        """
        if followerId in self.connections:
            self.connections[followerId].remove(followeeId)


# Your Twitter object will be instantiated and called as such:
# obj = Twitter()
# obj.postTweet(userId,tweetId)
# param_2 = obj.getNewsFeed(userId)
# obj.follow(followerId,followeeId)
# obj.unfollow(followerId,followeeId)
# @lc code=end

#
# @lc app=leetcode id=929 lang=python
#
# [929] Unique Email Addresses
#

# @lc code=start
class Solution(object):
    def numUniqueEmails(self, emails):
        """
        :type emails: List[str]
        :rtype: int
        """
        emails_set = set()
        for email in emails:
            local_s_domain = email.split("@")
            emails_set.add(local_s_domain[0].split("+")[0].replace(".", "") + "@" + local_s_domain[1])
        return len(emails_set)

# @lc code=end


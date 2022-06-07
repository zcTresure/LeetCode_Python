# -*- coding: utf-8 -*-
# File:      929. 独特的电子邮件地址.py
# DATA:      2022/6/4
# Software:  PyCharm
__author__ = 'zcFang'

from typing import List


class Solution:
    def numUniqueEmails(self, emails: List[str]) -> int:
        email_set = set()
        for email in emails:
            index = email.index('@')
            local = email[:index].split('+', 1)[0]
            local = local.replace('.', '')
            email_set.add(local + email[index:])
        return len(email_set)


emails = ["test.email+alex@leetcode.com", "test.e.mail+bob.cathy@leetcode.com", "testemail+david@lee.tcode.com"]
print(Solution().numUniqueEmails(emails))

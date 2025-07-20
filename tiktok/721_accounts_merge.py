"""
Given a list of accounts where each element accounts[i] is a list of strings, 
where the first element accounts[i][0] is a name, and the rest of the elements 
are emails representing emails of the account.
"""
from typing import List
from collections import deque

class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        # To set up a dictionary. key (email) : value (account index)
        email_to_indexes = {}
        for i in range(len(accounts)):
            currAccount = accounts[i]
            for j in range(1, len(accounts[i])):
                email = currAccount[j]
                accountList = email_to_indexes.get(email, [])
                accountList.append(i)
                email_to_indexes[email] = accountList
        res = [] # The final result
        visitedEmails = set() # To track used emails

        for email in email_to_indexes.keys():
            if email in visitedEmails:
                continue
            mergedEmails = []
            mergedEmails.append(email)
            # Use BFS to add all emails
            queue = deque()
            queue.append(email)
            visitedEmails.add(email)
            while queue: # The condition?
                currEmail = queue.popleft() # The email as key
                indices = email_to_indexes[currEmail] # A list of index: [0, 2, 3]
                for index in indices:
                    for i in range(1, len(accounts[index])):
                        # If we already have visited this email, continue
                        if accounts[index][i] in visitedEmails:
                            continue
                        queue.append(accounts[index][i])
                        visitedEmails.add(accounts[index][i])
                        mergedEmails.append(accounts[index][i])
            mergedEmails.sort()
            # The clear on the what's subscriptable
            name = accounts[email_to_indexes[email][0]][0]
            mergedEmails.insert(0, name)
            res.append(mergedEmails)            
        return res
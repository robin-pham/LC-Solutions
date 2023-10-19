# 721 - Accounts Merge

"""
given array accounts which has a name as first element followed by a number of emails
if emails are repeated, merge these accounts
if emails are the same, the first name will be the same
if names are the same, they might just be different people - only way to tell is the emails

union find of emails? if a person has multiple emails, union these
then after processing all accounts, find the emails parents, group them, return

"""


class DSU:
    def __init__(self):
        self.parents = {}
        self.rank = {}
        self.name = {}

    def find(self, node):
        if node not in self.parents:
            self.parents[node] = node
        if self.parents[node] != node:
            self.parents[node] = self.find(self.parents[node])
        return self.parents[node]

    def write_name(self, node, name):
        if node not in self.name:
            self.name[node] = name

    def get_rank(self, node):
        if node not in self.rank:
            self.rank[node] = 0
        return self.rank[node]

    def union(self, node_a, node_b):
        parent_a = self.find(node_a)
        parent_b = self.find(node_b)
        if parent_a == parent_b:
            return
        rank_a = self.get_rank(parent_a)
        rank_b = self.get_rank(parent_b)
        if rank_a > rank_b:
            self.parents[parent_b] = parent_a
        else:
            self.parents[parent_a] = parent_b
            if rank_a == rank_b:
                self.rank[parent_b] += 1


from collections import defaultdict


def account_merge(accounts):
    email_groups = DSU()
    for account in accounts:
        email_groups.find(account[1])
        email_groups.write_name(account[1], account[0])
        for email in account[2:]:
            email_groups.union(email, account[1])
            email_groups.write_name(email, account[0])
    merged_accounts = defaultdict(set)
    sorted_merged_accounts = []
    for email in email_groups.parents.keys():
        parent_email = email_groups.find(email)
        merged_accounts[parent_email].add(email)
    for parent in merged_accounts:
        sorted_merged_accounts.append(
            [email_groups.name[parent]] + sorted(merged_accounts[parent])
        )
    return sorted_merged_accounts


accounts = [
    ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
    ["John", "johnsmith@mail.com", "john00@mail.com"],
    ["Mary", "mary@mail.com"],
    ["John", "johnnybravo@mail.com"],
]
print(account_merge(accounts))

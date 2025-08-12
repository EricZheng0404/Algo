#!/bin/python3

import math
import os
import random
import re
import sys
import ast


def has_cycle(adj_matrix):
    # Write your code here
    # The number of nodes
    n = len(adj_matrix)
    visited = [False] * n
    for i in range(n):
        if visited[i]:
            return False
        visited[i] = True
        traverse(adj_matrix, visited, i)
    return True

def traverse(adj_matrix, visited, start):
    for i in range(len(adj_matrix)):
        if visited[i]:
            return False
        if adj_matrix[start][i] == 1:
            visited[i] = True
            traverse(adj_matrix, visited, i)

adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 1, 0, 0],
    [0, 1, 0, 0, 0],
    [0, 0, 0, 0, 1],
    [0, 0, 0, 1, 0]
]

print(has_cycle(adj_matrix))
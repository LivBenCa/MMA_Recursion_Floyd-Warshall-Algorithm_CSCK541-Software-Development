# Test Cases for Floyd Warshall Function

""" This file contains four different test cases for the Floyd Warshall
algorithm function.   The function works for all types of graphs
including ones with negative edges, except if the graph contains a
negative cycle.  Below is the expected inputs and outputs for each
different scenario.
"""

# Use value for infinity to denote edges that do not exist
INF = float('inf')

# Test A: Control Graph
""" Title: Floyd Warshall Algorithm | DP-16
Author: GeeksforGeeks
Date: 24th Nov. 2021
Code version: unknown
Availability: https://www.geeksforgeeks.org/floyd-warshall-algorithm-dp-16/
"""
sample_a = [[0, 5, INF, 10],
            [INF, 0, 3, INF],
            [INF, INF, 0,   1],
            [INF, INF, INF, 0]]

output_a = [[0, 5, 8, 9],
            [INF, 0, 3, 4],
            [INF, INF, 0, 1],
            [INF, INF, INF, 0]]

# Test B: Negative Edges Graph (No Negative Cycles)
sample_b = [[0, INF, 9, INF],
            [INF, 0, INF, INF],
            [INF, -5, 0, 8],
            [-3, 2, INF, 0]]

output_b = [[0, 4, 9, 17],
            [INF, 0, INF, INF],
            [5, -5, 0, 8],
            [-3, 1, 6, 0]]

# Test C: Small Graph (Three Vertices)
sample_c = [[0, INF, 10],
            [INF, 0, INF],
            [INF, 2, 0]]

output_c = [[0, 12, 10],
            [INF, 0, INF],
            [INF, 2, 0]]

# Test D: Large Graph (Eight Vertices)
sample_d = [[0, 8, INF, INF, 5, 3, INF, INF],
            [INF, 0, INF, 11, 5, INF, 9, INF],
            [7, 4, 0, INF, INF, 4, INF, INF],
            [INF, INF, INF, 0, 1, INF, INF, 2],
            [INF, INF, INF, INF, 0, INF, INF, INF],
            [INF, INF, INF, INF, INF, 0, INF, INF],
            [INF, INF, INF, 3, INF, INF, 0, 12],
            [INF, INF, INF, INF, INF, INF, INF, 0]]

output_d = [[0, 8, INF, 19, 5, 3, 17, 21],
            [INF, 0, INF, 11, 5, INF, 9, 13],
            [7, 4, 0, 15, 9, 4, 13, 17],
            [INF, INF, INF, 0, 1, INF, INF, 2],
            [INF, INF, INF, INF, 0, INF, INF, INF],
            [INF, INF, INF, INF, INF, 0, INF, INF],
            [INF, INF, INF, 3, 4, INF, 0, 5],
            [INF, INF, INF, INF, INF, INF, INF, 0]]

# Test E: Very Large Graph (Sixteen Vertices)
sample_e = [[0, 8, INF, INF, 5, 3, INF, INF, 5, 2, 8, 11, 23, 17, 1, 2],
            [INF, 0, INF, 11, 5, INF, 9, INF, INF, 4, INF, 1, 4, 11, INF, 8],
            [7, 4, 0, INF, INF, 4, INF, INF, 5, 3, INF, INF, 5, 2, 8, 11],
            [4, 4, 8, 0, 1, INF, INF, 2, INF, INF, INF, INF, INF, INF, INF, 3],
            [4, 4, 8, INF, 0, INF, INF, INF, INF, 4, INF, 11, 5, INF, 9, INF],
            [4, 4, 8, INF, INF, 0, INF, INF, 7, 4, 9, INF, INF, 4, INF, INF],
            [4, 4, 8, 3, INF, 2, 0, 12, INF, INF, INF, INF, INF, INF, INF, 12],
            [4, 4, 8, INF, INF, INF, INF, 0, 5, 2, 9, 22, 3, 7, 9, 1],
            [2, 8, 8, INF, 5, 3, INF, INF, 0, 2, 8, 11, 23, 17, 1, 2],
            [INF, 5, INF, 11, 5, INF, 9, INF, INF, 0, INF, 1, 4, 11, INF, 8],
            [7, 4, 2, INF, INF, 4, INF, INF, 5, 3, 0, INF, 5, 2, 8, 11],
            [INF, 7, 4, INF, 1, 2, 9, 2, INF, INF, INF, 0, INF, INF, INF, 3],
            [INF, 7, 4, 11, 2, INF, INF, 3, 5, 4, INF, 11, 0, INF, 9, INF],
            [INF, 7, 4, INF, INF, 9, INF, INF, 7, 4, 9, INF, INF, 0, INF, INF],
            [INF, 7, 4, 3, INF, INF, 8, 12, INF, 6, INF, INF, INF, INF, 0, 12],
            [INF, 7, 4, INF, INF, INF, INF, 1, 5, 2, INF, 22, 3, 7, 9, 0]]

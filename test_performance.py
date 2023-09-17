# Performance Tests for Floyd Warshall Function

# Update PYTHON Path (Source below)
""" Title: Relative imports in Python 3
Author: E-rich
Date: 10th Nov. 2021
Code version: 1.0
Availability:
https://stackoverflow.com/questions/16981921/relative-imports-in-python-3
"""
import sys
import os
SCRIPT_DIR = os.path.dirname(os.path.abspath(__file__))
sys.path.append(os.path.dirname(SCRIPT_DIR))

# Import Floyd Warshall function
from floydwarshall.function import floydWarshall

# Import Floyd Warshall test cases
from test_cases import (sample_a, sample_b, sample_c, sample_d, sample_e)

# Import testing package
import cProfile

# Performance Tests
cProfile.run(f"{floydWarshall(sample_a)}")

cProfile.run(f"{floydWarshall(sample_b)}")

cProfile.run(f"{floydWarshall(sample_c)}")

cProfile.run(f"{floydWarshall(sample_d)}")

# Uncomment to test very large graph
# cProfile.run("floydWarshall(sample_e)")

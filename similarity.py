# -*- coding: utf-8 -*-

import numpy as np

def cos_similarity(v1, v2):

    v1 = v1.flatten()
    v2 = v2.flatten()
    dot_prod = np.dot(np.array(v1), np.array(v2))
    v1_sum = np.sqrt(np.sum(np.square(v1)))
    v2_sum = np.sqrt(np.sum(np.square(v2)))
    return dot_prod/(v1_sum*v2_sum)

# Euclidean distance function
def euclidean_distance(v1, v2):
    total_distance = np.sqrt(np.sum((np.array(v1) - np.array(v2)) ** 2))
    return total_distance

# Manhattan distance function
def manhattan_distance(v1, v2):
    total_distance = np.sum(np.abs(np.array(v1) - np.array(v2)))
    return total_distance

#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Tue Jun 20 08:41:23 2023

@author: ewstott
"""

def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)   
        if t[1] not in words:   
            words = words + (t[1],)
    min_nums = min(nums)
    max_nums = max(nums)
    unique_words = len(words)
    return (min_nums, max_nums, unique_words)


(small, large, words) = get_data(((1, 'mine'), 
                                  (3, 'yours'),
                                  (5, 'ours'),
                                  (7, 'mine')))
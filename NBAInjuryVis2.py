#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:04:41 2018

@author: shriramgharpure
"""
import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
labels = ['DR Before', 'DR After', 'BR Before', 'BR After', 'PG Before', 'PG After', 'JW Before', 'JW After']
PERPlayers = [23.10, 9.32, 24.08, 13.94, 20.16, 20.98, 19.83, 19.20]
index = np.arange(len(labels))
plt.bar(index, PERPlayers, color=['red', 'red', 'brown', 'brown', 'yellow', 'yellow', 'blue', 'blue'])
plt.title('Player Efficiency Ratio: Before and After Year-Long Injury')
plt.xticks(index, labels, fontsize=8)
plt.xlabel('Before Injury and After Injury Seasons')
plt.ylabel('Player Efficiency Ratio(PER)')

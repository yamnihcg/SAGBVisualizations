#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Oct 19 17:34:54 2018

@author: shriramgharpure
"""

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
labels = ['DR Before', 'DR After', 'BR Before', 'BR After', 'PG Before', 'PG After', 'JW Before', 'JW After']
WSPlayers = [13.10, 2.34, 13.50, 7.42, 10.80, 9.20, 8.40, 2.70]
index = np.arange(len(labels))
plt.bar(index, WSPlayers, color=['red', 'red', 'brown', 'brown', 'yellow', 'yellow', 'blue', 'blue'])
plt.title('Win Shares: Before and After Year-Long Injury')
plt.xticks(index, labels, fontsize=8)
plt.xlabel('Before Injury and After Injury Seasons')
plt.ylabel('Win Shares(WS)')
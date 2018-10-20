#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Oct 11 07:48:30 2018

@author: shriramgharpure
"""

import matplotlib.pyplot as plt
import numpy as np 
import pandas as pd
# Change in WinShares and PER for the 2 guards, 2 forwards and 2 Centers in the Study
#Red: Paul George and John Walll
#Green: Derrick Rose and Brandon Roy
changeinWinSharesG = [-6.91, -6.08]
changeinPERG = [-13.78, -10.14]
changeinWinSharesF = [-1.6, -2.9]
changeinPERF = [0.82, -0.63]
plt.scatter(changeinWinSharesG, changeinPERG, color=['red'],label='Guards')
plt.scatter(changeinWinSharesF, changeinPERF, color=['green'], label='Forwards')
plt.legend(loc='upper left')
plt.xlim(-10, 0)
plt.ylim(-20, 2)
plt.xlabel('Change in Winshares(ΔWS)')
plt.ylabel('Change in Player Efficiency Ratio(ΔPER)')
plt.title('Relationship between ΔWS and ΔPER')


# -*- coding: utf-8 -*-
"""
Created on Sat Oct 07 17:44:41 2017

@author: 93138
"""

import numpy as np
from scipy import stats
from scipy.stats import chisquare
observed = np.array([15,95])
 #观测值：110学生中化妆的女生95人，化妆的男生15人
expected = np.array([55,55])
#理论值：110学生中化妆的女生55人，化妆的男生55人
cs=chisquare(observed,expected)
print cs
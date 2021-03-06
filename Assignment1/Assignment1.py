# -*- coding: utf-8 -*-
"""Untitled0.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1uOgB149pFhb3B7R3Unb-wsTtPWZ6kzpq
"""

import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import bernoulli

#6 trails
#Number of trails is 6, 1 denotes red ball and 0 denotes black ball
simlen=int(6)

#Probability of the event
prob = 7/16

#Generating sample date using Bernoulli r.v.
data_bern = bernoulli.rvs(size=simlen,p=prob)
#Calculating the number of favourable outcomes
err_ind = np.nonzero(data_bern == 1)
#calculating the probability from simulation
err_n = np.size(err_ind)/simlen

#Theory vs simulation
print("Probability-simulation,actual:",err_n,prob)
print("Samples generated:",data_bern)
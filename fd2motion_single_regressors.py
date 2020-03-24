# -*- coding: utf-8 -*-
"""
Created on Tue Feb  5 11:32:25 2019

@author: martin
"""

# This script takes output identified as outliers (see extractDataFromConfoundFile_fMRIPrep.py) 
# and converts volume numbers into arrays of zeros and ones that can be used as additional regressors 
# This script writes one regressor for each bad volume.

import os
import numpy as np

base_dir = '/data/subjects'

participants = ['001']
runs = ['1','2']


This is for the localizer

a = 'outliers_index_run-{0}.txt'
b = 'sub-control{0}'

for vp in participants:
   for run in runs:
   
       print('This is participant ' + vp + ' and run ' + run)       
       
       path = os.path.join(base_dir, b.format(vp), 'ses-1/motion')
       os.chdir(path)
       
       with open(a.format(run)) as f:
           content = f.readlines()
       
       content = [x.strip() for x in content]
       
       content = map(int, content)
       
       f = open('fd_regressors_run-%s.txt' %run, 'w')   
       firstline = content[0]
       arr = np.zeros((133, 1), dtype = int)
       np.put(arr, [firstline - 1], [1])
       np.savetxt('fd_regressors_run-%s.txt' %run, arr, fmt='%i')
       
       def appendAsColumn(arr):
           fileContent = np.loadtxt('fd_regressors_run-%s.txt' %run, dtype = int, ndmin = 2)
           fileContent = np.hstack((fileContent, arr.astype(int)))
           np.savetxt('fd_regressors_run-%s.txt' %run, fileContent, fmt='%i')
       
       for line in content[1:]:
           arr = np.zeros((133, 1), dtype = int)
           np.put(arr, [line - 1], [1])    
           appendAsColumn(arr)  
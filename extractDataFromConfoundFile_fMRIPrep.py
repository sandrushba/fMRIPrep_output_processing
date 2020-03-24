# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 18:22:08 2019

@author: martin
"""
import os
import pandas as pd

base_dir = '/data/'

participants = ['001']

runs = ['1', '2']

tasks = ['X', 'Y']

a = 'sub-control{0}'
b = 'sub-control{0}_ses-1_task-{1}_run-{2}_desc-confounds_regressors.tsv'
c = 'motion_task-{0}_run-{1}.txt'
d = 'fd_task-{0}_run-{1}.txt'
e = 'outliers_index_task-{0}_run-{1}.txt'
h = 'control{0}'

for vp in participants:
    for task in tasks:
        for run in runs:
            print('This is participant ' + vp + ' and task ' + task + ' and run ' + run)
            confound_dir = os.path.join(base_dir, h.format(vp), 'fmriprep', a.format(vp), 'ses-1/func')
            os.chdir(confound_dir)
    
    
    ## This part extracts the 6 motion regressors from the confounds.tsv file written by fmriprep
    
            # Read confound file for second echo for each participant
            confound_file = pd.read_csv(b.format(vp, task, run), sep = '\t', header = 0)
    #    
            # Extraxt six motion regressors from data frame
            z = confound_file[['trans_x', 'trans_y', 'trans_z', 'rot_x', 'rot_y', 'rot_z']]
            
            y = z
    
            # Write data frame to text file, don't write index and header    
            with open(os.path.join('/data/subjects', a.format(vp), 'ses-1/motion', c.format(task, run)), 'w') as f:
                f.write(y.to_string(index = False, header = False))
    #   
    
    
    ## This part extracts the index numbers from the framewise_displacement column that exceed the value of 0.9
    
            w = confound_file
                
            x = w[w.framewise_displacement >= 0.9]
            fd = x[['framewise_displacement']]
              
            with open(os.path.join('/data/p_02221/MDN_APH/Derivatives/subjects', a.format(vp), 'ses-1/motion', d.format(task, run)), 'w') as f:
                  f.write(fd.to_string(header=False))
                
            with open(os.path.join('/data/subjects', a.format(vp), 'ses-1/motion', d.format(task, run))) as f:
                with open(os.path.join('/data/subjects', a.format(vp), 'ses-1/motion', e.format(task, run)), 'w') as i:
                    for line in f:
                          if line.strip():
                              i.write("\t".join(line.split()[:1]) + "\n")
            

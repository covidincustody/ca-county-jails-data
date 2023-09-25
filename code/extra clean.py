# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 00:30:33 2023

@author: apkom
"""
import os
import shutil
import re

# Reorganizing LA County web data archive

# Script to clean web documentation for Los Angeles County Sheriff's Office
read_path = 'C:/Users/apkom/Downloads/Los Angeles County Web Documentation'
write_path = 'C:/Users/apkom/Downloads/Los Angeles County Web Documentation (Clean)'

# Read data from raw data folders and reorganize for public display
for day in os.listdir(read_path):
    try: 
        if '-' in day:
            total_docs = len(os.listdir(read_path+'/'+day))
            for i, file in enumerate(os.listdir(read_path+'/'+day)):
                store_path = write_path+'/'+day
                if not os.path.exists(store_path):
                    os.makedirs(store_path)
                new_path = store_path+'/'+day+' (Part '+str(i+1)+' of '+str(total_docs)+').jpg'
                shutil.copyfile(read_path+'/'+day+'/'+file, new_path)
    except:
        print('Could not process: ', day)
        
        
# Read data from raw year folders and reorganize for public display
date_pattern = r"\d{2}_\d{2}_\d{4}"
for year in os.listdir(read_path):
    if year in ['2021', '2022']:
        for month in os.listdir(read_path+'/'+year+'/'+year):
            for day in os.listdir(read_path+'/'+year+'/'+year+'/'+month):
                res = re.search(date_pattern, day)
                if res:
                    store_path = write_path+'/'+year
                    if not os.path.exists(store_path):
                        os.makedirs(store_path)
                    new_path = store_path+'/'+res.group()+' (Part 1 of 1).pdf'
                    if not os.path.exists(new_path):
                        shutil.copyfile(read_path+'/'+year+'/'+year+'/'+month+'/'+day, new_path)
                    else:
                        new_path = store_path+'/'+res.group()+' (Part 1 of 2).pdf'
                        shutil.copyfile(read_path+'/'+year+'/'+year+'/'+month+'/'+day, new_path)
                        print(day)
                        
###############################################################################

# Reorganizing SF County web data archive

# Script to clean web documentation for San Francisco County Sheriff's Office
read_path = 'C:/Users/apkom/Downloads/San Francisco County Web Documentation'
write_path = 'C:/Users/apkom/Downloads/San Francisco County Web Documentation (Clean)'

# Read data from raw data folders and reorganize for public display
for day in os.listdir(read_path):
    try: 
        if '-' in day:
            total_docs = len(os.listdir(read_path+'/'+day))
            for i, file in enumerate(os.listdir(read_path+'/'+day)):
                store_path = write_path+'/'+day
                if not os.path.exists(store_path):
                    os.makedirs(store_path)
                new_path = store_path+'/'+day+' (Part '+str(i+1)+' of '+str(total_docs)+').jpg'
                shutil.copyfile(read_path+'/'+day+'/'+file, new_path)
    except:
        print('Could not process: ', day)
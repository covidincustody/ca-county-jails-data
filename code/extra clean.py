# -*- coding: utf-8 -*-
"""
Created on Wed Sep 13 00:30:33 2023

@author: apkom
"""
import os
import shutil


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
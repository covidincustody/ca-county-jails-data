# -*- coding: utf-8 -*-

import pandas as pd
import os
import gspread
import oauth2client
import oauth2client.service_account
import shutil




def gen_var_list(var_list, pop_cat):
    # Initialize list of variables
    mod_vars = []
    for var in var_list:
        if var in ['Active Cases', 'Pending Tests', 'Population', 'Fully Vaccinated', 'Boosted']:
            mod_vars.append(var+' ('+pop_cat+', '+'current'+')')
        elif 'Percent' in var:
            mod_vars.append(var+' ('+pop_cat+')')
        else:
            mod_vars.append(var+' ('+pop_cat+', '+'cumulative'+')')
    # General columns
    meta_data = ['Facility Name', 'As of Date', 'County']
    for var in meta_data:
        mod_vars.append(var)
        
    return mod_vars




def mod_data(df):
    df.columns = df.iloc[1, :]
    df.drop([0,1], inplace = True)
    df['As of Date'] = pd.to_datetime(df['As of Date'])
    df.set_index(df['As of Date'], drop = True, inplace = True)
    df.drop(columns = 'As of Date', inplace = True)




def gen_county_jails_dataset(read_path, select_vars, write_path):
    # Generate variables of interest
    pop_vars = gen_var_list(select_vars, 'Incarcerated population')
    sheriff_staff_vars = gen_var_list(select_vars, "Sheriff's office")
    jail_staff_vars = gen_var_list(select_vars, 'Jail staff')
    med_staff_vars = gen_var_list(select_vars, 'Medical staff')
    
    # Initialize file lists
    pop_files = []
    staff_files = []
    
    # Initialize dataframes
    all_pop_data = pd.DataFrame()
    all_sheriff_staff_data = pd.DataFrame()
    all_jail_staff_data = pd.DataFrame()
    all_med_staff_data = pd.DataFrame()
    
    # Process data per file per county
    for county in os.listdir(read_path):
        for file in os.listdir(read_path+'/'+county):
            # Incarcerated population data
            if ('Data' in file) and ('xlsx' in file):
                pop_files.append(file)
                pop_data = pd.read_excel(read_path+'/'+county+'/'+file)
                mod_data(pop_data)
                all_pop_data = pd.concat([all_pop_data, pop_data[[col for col in pop_data.columns if col in pop_vars]]])
            # Staff population data
            if ('Staff' in file) and ('xlsx' in file):
                staff_files.append(file)
                # Sheriff's office
                if "Sheriffs office" in pd.read_excel(read_path+'/'+county+'/'+file, None).keys():
                    sheriff_staff_data = pd.read_excel(read_path+'/'+county+'/'+file, "Sheriffs office")
                    mod_data(sheriff_staff_data)
                    all_sheriff_staff_data = pd.concat([all_sheriff_staff_data, sheriff_staff_data[[col for col in sheriff_staff_data.columns if col in sheriff_staff_vars]]])
                # Jail staff
                if 'Jail staff' in pd.read_excel(read_path+'/'+county+'/'+file, None).keys():
                    jail_staff_data = pd.read_excel(read_path+'/'+county+'/'+file, "Jail staff")
                    mod_data(jail_staff_data)
                    all_jail_staff_data = pd.concat([all_jail_staff_data, jail_staff_data[[col for col in jail_staff_data.columns if col in jail_staff_vars]]])
                # Medical staff
                if 'Medical staff' in pd.read_excel(read_path+'/'+county+'/'+file, None).keys():
                    med_staff_data = pd.read_excel(read_path+'/'+county+'/'+file, "Medical staff")
                    mod_data(med_staff_data)
                    all_med_staff_data = pd.concat([all_med_staff_data, med_staff_data[[col for col in med_staff_data.columns if col in med_staff_vars]]])

    # Initialize dataframe with aggregated data - population, staff, medical staff, etc.                 
    county_jail_data = all_pop_data
    for df in [all_jail_staff_data, all_sheriff_staff_data, all_med_staff_data]:
       county_jail_data = pd.merge(county_jail_data, df, how = 'outer', on = ['As of Date', 'County', 'Facility Name'])
    county_jail_data = county_jail_data.groupby(by = [county_jail_data.index, 'Facility Name', 'County']).max()
    county_jail_data = county_jail_data.reset_index()
    county_jail_data = county_jail_data.set_index('As of Date', drop = True)
    county_jail_data = county_jail_data.sort_values(by = ['County', 'As of Date'])
    
    # Write results to excel output
    with pd.ExcelWriter(write_path) as writer:  
        county_jail_data.to_excel(writer, sheet_name='All Data', index = True)
    
    return county_jail_data
        


        
def gen_recent_vals(county_jail_data, write_path):
    # Initialize dataframe
    all_recent_data = pd.DataFrame(columns = ['As of Date', 'Facility Name', 'County'])
    # Find most recent value for each variable in the aggregated dataset
    for var in [var for var in county_jail_data.columns if (var in ['As of Date', 'County', 'Facility Name']) == False]:
        recent_var_data = pd.DataFrame()
        for county in [county for county in county_jail_data['County'].unique() if pd.isna(county) == False]:
            var_data = county_jail_data[county_jail_data['County'] == county][var]
            var_data = var_data[pd.isna(var_data) == False]
            if len(var_data) != 0:
                recent_var_data = pd.concat([recent_var_data, 
                    pd.DataFrame([[var_data.index[-1], 
                    county_jail_data[county_jail_data['County'] == county]['Facility Name'][-1],
                    county,
                    var_data[-1]]],
                    columns = ['As of Date', 'Facility Name', 'County', var])])
        all_recent_data = pd.merge(all_recent_data, recent_var_data, how = 'outer', on = ['As of Date', 'County', 'Facility Name'])
                    
    all_recent_data = all_recent_data.sort_values(by = ['County', 'As of Date'])  

    with pd.ExcelWriter(write_path) as writer:  
        all_recent_data.to_excel(writer, sheet_name='Recent Data', index = False)
    
    return all_recent_data




def write_raw_data(read_path, write_path):
    # Read data from raw data folders and reorganize for public display
    for county in os.listdir(read_path):
        for file in os.listdir(read_path+'/'+county):
            if '.xlsx' in file:
                store_path = write_path+'/'+county
                if not os.path.exists(store_path):
                    os.makedirs(store_path)
                shutil.copyfile(read_path+'/'+county+'/'+file, store_path+'/'+file)
    return           
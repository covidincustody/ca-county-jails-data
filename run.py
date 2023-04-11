# -*- coding: utf-8 -*-

import pandas as pd
import os
import gspread
import oauth2client
import oauth2client.service_account
from utils import *


# Generate variable lists
select_vars = ['Active Cases',
             'Confirmed Cases',
             'Tests',
             'Deaths',
             'Pending Tests',
             'Population', 
             'Fully Vaccinated',
             'Boosted', 
             'Percent of Population Fully Vaccinated',
             'Percent of Population Boosted']

# Aggregating county jail data across all counties using the specified variables 
all_county_jails_data = gen_county_jails_dataset(read_path = 'C:/Users/apkom/Downloads/Data Collection - County Jails',
                                               select_vars = select_vars,
                                               write_path = 'C:/Users/apkom/Documents/COVID19_Data_Analysis_CA_Incarcerated_Jails/All_Data/All_Data.xlsx') 

recent_var_data = gen_recent_vals(county_jail_data = all_county_jails_data, 
                                  write_path = "C:/Users/apkom/Documents/COVID19_Data_Analysis_CA_Incarcerated_Jails/All_Data/Recent_Data.xlsx")


# Uploading aggregated county jails data to spreadsheet online (in Google Cloud)
scope = ['https://spreadsheets.google.com/feeds','https://www.googleapis.com/auth/drive']
creds = oauth2client.service_account.ServiceAccountCredentials.from_json_keyfile_name('C:/Users/apkom/credentials.json', scope)
client = gspread.authorize(creds)

# Get the instance of the Google Sheet in the cloud
sheet = client.open('Covid In-Custody Project: CA County Jails COVID Data').sheet1

# Get the first tab of the spreadsheet
all_county_jails_data = all_county_jails_data.fillna('')
all_county_jails_data.insert(0, column = 'As of Date', value = all_county_jails_data.index)
all_county_jails_data = all_county_jails_data[['As of Date', 'Facility Name', 'County',
       'Active Cases (Incarcerated population, current)',
       'Confirmed Cases (Incarcerated population, cumulative)',
       'Deaths (Incarcerated population, cumulative)',
       'Tests (Incarcerated population, cumulative)',
       'Pending Tests (Incarcerated population, current)',
       'Population (Incarcerated population, current)',
       'Fully Vaccinated (Incarcerated population, current)',
       'Boosted (Incarcerated population, current)',
       'Percent of Population Fully Vaccinated (Incarcerated population)',
       'Percent of Population Boosted (Incarcerated population)',
       'Active Cases (Jail staff, current)',
       'Confirmed Cases (Jail staff, cumulative)',
       'Deaths (Jail staff, cumulative)', 
       'Tests (Jail staff, cumulative)',
       'Population (Jail staff, current)',
       'Fully Vaccinated (Jail staff, current)',
       'Boosted (Jail staff, current)',
       'Percent of Population Fully Vaccinated (Jail staff)',
       'Percent of Population Boosted (Jail staff)',
       "Active Cases (Sheriff's office, current)",
       "Confirmed Cases (Sheriff's office, cumulative)",
       "Deaths (Sheriff's office, cumulative)",
       "Tests (Sheriff's office, cumulative)",
       "Population (Sheriff's office, current)",
       "Fully Vaccinated (Sheriff's office, current)",
       "Boosted (Sheriff's office, current)",
       "Percent of Population Fully Vaccinated (Sheriff's office)",
       "Percent of Population Boosted (Sheriff's office)",
       'Population (Medical staff, current)',
       'Fully Vaccinated (Medical staff, current)',
       'Boosted (Medical staff, current)',
       'Percent of Population Fully Vaccinated (Medical staff)',
       'Percent of Population Boosted (Medical staff)']]

all_county_jails_data['As of Date'] = all_county_jails_data['As of Date'].astype(str)

# Upload dataframe to the Google Sheet
sheet.update('A3', [all_county_jails_data.columns.values.tolist()] + all_county_jails_data.values.tolist())






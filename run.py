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

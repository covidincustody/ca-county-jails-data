# Background

The Covid In-Custody Project is building a dataset on COVID-19 in California's correctional facilities using public sources (official websites, open data portals etc.) and freedom of information laws. This repository focuses on California's 58 county jail systems, a majority of which do not publicly disclose any data. An detailed outline of the counties, records requests, correspondences, etc. can be found here: https://drive.google.com/drive/folders/1VQr_BHHzCEwUH93qSXlsF3V2k1r6wAxi. 

We read and process data from each county jail (in the Google Drive link) to generate a dataset of cases, vaccinations and deaths among incarcerated people and staff: https://docs.google.com/spreadsheets/d/1q9zoEN_nI_oBAxO8k_9kd5612gCaMHSfViU-1WKVSKY/edit#gid=0. 

# Instructions

# Data dictionary

The data has been aggregated across all county jails and has the following definitions:\
```Incarcerated population```:	The population in the Sheriff's Office county jail custody.\
```Sheriff's office```:	All employees, including correctional officers, administrative staff, sworn and civilian staff, in the Sheriff's Office. These employees encompass the entire Sheriff's Office and are not specific to jail or custodial roles.\
```Jail staff```:	Sheriff's Office employees working in correctional settings only. In some counties, this may include non-jail Sheriff's Office employees working in the jails on a non-permanent basis.\
```Medical staff```:	Medical workers in the correctional setting, including part-time and full-time workers who are contracted by third-party medical services such as Wellpath or provided through the county healthcare services division.

Sources: Data is primarily collected from California Public Records Act (abbreviated as CPRA or PRA) requests to Sheriff's Offices and Sheriff's Office websites that contain updates on COVID-19 in custody. As a result, the data definitions below are subject to the each Sheriff's Office interpretation of our CPRA requests. Some counties hold weekly or monthly conference calls with community members, the county public health department and the correctional health provider, wherein updates on COVID-19 in custody are discussed. Data may also be collected from these calls.

Note: Unless specified otherwise, ""staff"" in this definitions list refers to all categories of staff, namely sheriff's office, jail staff and medical staff."		

Data Category |	Variable Names | Definition
--------------|----------------|--------------
```Active Cases``` | Active Cases (Incarcerated population, current), Active Cases (Sheriff's office, current), Active Cases (Jail staff, current) | The number of current positive confirmed COVID-19 cases.\ NOTE:\ Incarcerated population: Includes individuals who tested positive during the booking or intake process\
Incarcerated population/staff: For some counties, active cases may be the number of positive COVID-19 test results returned on a given date or during some time period prior to the specified date. As a result, it may be an inaccurate representation of active cases on the specified date. Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.
Confirmed Cases	| Confirmed Cases (Incarcerated population, cumulative), Confirmed Cases (Sheriff's office, cumulative), Confirmed Cases (Jail staff, cumulative) |	 The total number of positive COVID-19 cases that have been confirmed since the start of the pandemic.\ NOTE:\ Incarcerated population/staff: For some counties, the starting date of the count may be much later than Jan - March 2020, which is roughly taken to be the initial period of the pandemic. The count may also be the number of positive COVID-19 test results and not the number of COVID-19 cases, which could result in overcounting of cases. For example, if an individual was tested twice or more in the same infection period their positive cases would be counted more than once in the total.\ Sheriff's office/jail staff: For some counties, this may exclude positive cases that were not reported to the county's human resources department. It may also only include positive cases that were identified through testing on-site by the local public health department or jail medical provider. Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.
Deaths | Deaths (Incarcerated population, cumulative), Deaths (Sheriff's office, cumulative), Deaths (Jail staff, cumulative) | The total number of deaths from COVID-19 related complications.\ NOTE: Incarcerated population: For some counties, this may be the number of suspected but not confirmed deaths from COVID-19. Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.
Tests	"Tests (Incarcerated population, cumulative)
Tests (Sheriff's office, cumulative)
Tests (Jail staff, cumulative)"	"The total number of COVID-19 tests that have been administered since the start of the pandemic
NOTE: 
Incarcerated population/staff: For some counties, the starting date of the count may be much later than Jan - March 2020, which is roughly taken to be the initial period of the pandemic. The count may also exclude antigen or home-tests and count PCR tests only. It may also be the number of tests administered and not the number of unique individuals tested, thereby this may not be a good denominator to calculate the test positivity rate.
Sheriff's office/jail staff: For some counties, this count may only include tests there were either reported to HR, administered on-site by the county public health department or the jail medical provider, or self-administered. It may not be the true number of tests that staff members have taken.
Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details."
Pending Tests	Pending Tests (Incarcerated population, current)	"The number of COVID-19 tests that are awaiting results
NOTE: Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details."
Population	"Population (Incarcerated population, current)
Population (Sheriff's office, current)
Population (Jail staff, current)"	"For the incarcerated population and jail staff, it is the number of individuals living or working in custody as of the specified date. For the sheriff's office, it is the total number of active employees as of the specified date.
NOTE:
Incarcerated population/staff: For some counties, this may be the average daily population for the week or month prior to the specified date.
Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details."
Fully Vaccinated	"Fully Vaccinated (Incarcerated population, current)
Fully Vaccinated (Sheriff's office, current)
Fully Vaccinated (Jail staff, current)"	"The total number of individuals that are at least fully vaccinated
NOTE: 
Incarcerated population: The count excludes any fully vaccinated incarcerated individual who is no longer in custody. In some counties, this may only include individuals who were vaccinated by the jail medical provider, i.e. excludes individuals who were vaccinated prior to their incarceration
Sheriff's office/jail staff: For some counties, this may exclude fully vaccinated staff members who did not report or confirm their vaccination status with human resources. 
Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details."
Boosted	"Boosted (Incarcerated population, current)
Boosted (Sheriff's office, current)
Boosted (Jail staff, current)"	"The total number of individuals that have received at least one booser
NOTE: 
Incarcerated population: The count excludes any boosted incarcerated individual who is no longer in custody. In some counties, this may only include individuals who received boosters from the jail medical provider, i.e. excludes individuals who were boosted prior to their incarceration
Sheriff's office/jail staff: For some counties, this may exclude boosted staff members who did not report or confirm their vaccination status with human resources. 
Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details."
Percent of Population Fully Vaccinated	"Percent of Population Fully Vaccinated (Incarcerated population)
Percent of Population Fully Vaccinated (Sheriff's office)
Percent of Population Fully Vaccinated (Jail staff)"	"Calculated field
The percentage of the population that is fully vaccinated at the least. It is calculated using the fully vaccinated and population variables for the same date.
NOTE: Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details."""
Percent of Population Boosted 	"Percent of Population Boosted (Incarcerated population)
Percent of Population Boosted (Sheriff's office)
Percent of Population Boosted (Jail staff)"	"Calculated field
The percentage of the population that has received at least one booster dose. It is calculated using the boosted and population variables for the same date.
NOTE: Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details."""
		

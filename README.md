# Table of Contents

- [Background](#background)
- [Instructions](#instructions)
- [Repo Structure](#repo-structure)
- [Data Dictionary](#data-dictionary)
  * [General](#general)
  * [Sources](#sources)
  * [Note](#note)
  * [Definitions](#definitions)

# Background

Our dataset on COVID-19 in California's correctional facilities combines information that was publicly disclosed by county agencies (official websites, open data portals etc.) or retrieved retrieved using freedom of information laws. In this repository, we focus on California's 58 county jails managed by independent sheriff's departments as opposed to the 35 state prisons under the jurisdiction of the CA Department of Corrections and Rehabilitation (CDCR). Since a majority of the county jails did not publicly disclose any COVID-19 data (cases, testing rate, vaccination rate, etc.), we relied on the California Public Records Act (CPRA) to gain insights into the pandemic behind bars. Details about our correspondences with the public records units can be found here: https://drive.google.com/drive/folders/1VQr_BHHzCEwUH93qSXlsF3V2k1r6wAxi. 

Dataset is live and available here: https://docs.google.com/spreadsheets/d/1q9zoEN_nI_oBAxO8k_9kd5612gCaMHSfViU-1WKVSKY/edit#gid=0. Refer to the data dictionary for details on the definitions used to aggregate data from all 58 county jail systems.

# Instructions

Download repository and modify run.py file to reflect the appropriate read and write paths. The read path will be your local copy of this folder: https://drive.google.com/drive/folders/1VQr_BHHzCEwUH93qSXlsF3V2k1r6wAxi. For simplest execution, use Anacondas (https://www.anaconda.com/products/distribution) with the necessary modules or packages pre-installed. Navigate to the folder with the run.py file using the Anaconda Terminal and execute program as ```python run.py```.

Please contact info@covidincustody.org with any questions or concerns

# Repo Structure

```bash
├── ca-county-jails-data
│   ├── code
│   │   ├── run.py
│   │   ├── utils.py
│   │   ├── cloud-upload.py (do not execute unless admin)
│   ├── data
│   │	├── aggregate
│   │	│	├── All_Data.xlsx (data aggregated across all 58 county jail systems)
│   │	├── recent data
│   │	│	├── Recent_Data.xlsx (the most recent timestamp available per county jail system)
│   │	├── ca counties (raw data files per county without aggregation or cleaning)
│   │	│	├── Alameda County
│   │	│	│	├── Alameda County Jails Data.xslx (jail population cases and vaccination data)
│   │	│	│	├── Alameda County Jails - Staff Testing and Cases.xslx (staff cases data)
│   │	│	│	├── Alameda County Jails - Staff Vaccinations.xslx (staff vaccination data)
│   │	│	│	├── Alameda County Jails - Vaccination Demographics.xslx (vaccinated jail population demographics)
│   │	│	│	├── Alameda County Jails - Testing Breakdown.xslx (jail population tested)
│   │	│	├── Amador County
│   │	│	│	├── ...
│   │	│	├── ...
│   │	│	├── Yolo County
│   │	│	│	├── ...
│   │	│	├── Yuba County
│   │	│	│	├── ...
├── README.md
```


# Data Dictionary

## General
```Incarcerated population```:	The population in the Sheriff's Office county jail custody.</br>
```Sheriff's office```:	All employees, including correctional officers, administrative staff, sworn and civilian staff, in the Sheriff's Office. These employees encompass the entire Sheriff's Office and are not specific to jail or custodial roles.</br>
```Jail staff```:	Sheriff's Office employees working in correctional settings only. In some counties, this may include non-jail Sheriff's Office employees working in the jails on a non-permanent basis.</br>
```Medical staff```:	Medical workers in the correctional setting, including part-time and full-time workers who are contracted by third-party medical services such as Wellpath or provided through the county healthcare services division.

## Sources
Data is primarily collected from California Public Records Act (abbreviated as CPRA or PRA) requests to Sheriff's Offices and Sheriff's Office websites that contain updates on COVID-19 in custody. As a result, the data definitions below are subject to the each Sheriff's Office interpretation of our CPRA requests. Some counties hold weekly or monthly conference calls with community members, the county public health department and the correctional health provider, wherein updates on COVID-19 in custody are discussed. Data may also be collected from these calls.

## Note
Unless specified otherwise, "staff" in this definitions list refers to all categories of staff, namely Sheriff's Office, jail staff and medical staff.

## Definitions

|Data Category | Variable Names | Definition|
| ------------ | -------------- | --------- |
| ```Active Cases``` | ```Active Cases (Incarcerated population, current)```, </br> ```Active Cases (Sheriff's office, current)```, </br> ```Active Cases (Jail staff, current)``` | The number of current positive confirmed COVID-19 cases.</br> **Notes**: </br> Incarcerated population: Includes individuals who tested positive during the booking or intake process.</br> Incarcerated population/staff: For some counties, active cases may be the number of positive COVID-19 test results returned on a given date or during some time period prior to the specified date. As a result, it may be an inaccurate representation of active cases on the specified date. Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details. | 
| ```Confirmed Cases``` | ```Confirmed Cases (Incarcerated population, cumulative)```, </br> ```Confirmed Cases (Sheriff's office, cumulative)```, </br> ```Confirmed Cases (Jail staff, cumulative)``` | The total number of positive COVID-19 cases that have been confirmed since the start of the pandemic.</br> **Notes**: </br> Incarcerated population/staff: For some counties, the starting date of the count may be much later than Jan - March 2020, which is roughly taken to be the initial period of the pandemic. The count may also be the number of positive COVID-19 test results and not the number of COVID-19 cases, which could result in overcounting of cases. For example, if an individual was tested twice or more in the same infection period their positive cases would be counted more than once in the total.</br> Sheriff's office/jail staff: For some counties, this may exclude positive cases that were not reported to the county's human resources department. It may also only include positive cases that were identified through testing on-site by the local public health department or jail medical provider. Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details. |
| ```Deaths``` | ```Deaths (Incarcerated population, cumulative)```, </br> ```Deaths (Sheriff's office, cumulative)```, </br> ```Deaths (Jail staff, cumulative)``` | The total number of deaths from COVID-19 related complications.</br> **Notes**:</br> Incarcerated population: For some counties, this may be the number of suspected but not confirmed deaths from COVID-19. Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.|
| ```Tests``` | ```Tests (Incarcerated population, cumulative)```, </br> ```Tests (Sheriff's office, cumulative)```, </br> ```Tests (Jail staff, cumulative)``` | The total number of COVID-19 tests that have been administered since the start of the pandemic. </br> **Notes**: </br> Incarcerated population/staff: For some counties, the starting date of the count may be much later than Jan - March 2020, which is roughly taken to be the initial period of the pandemic. The count may also exclude antigen or home-tests and count PCR tests only. It may also be the number of tests administered and not the number of unique individuals tested, thereby this may not be a good denominator to calculate the test positivity rate.</br> Sheriff's office/jail staff: For some counties, this count may only include tests there were either reported to HR, administered on-site by the county public health department or the jail medical provider, or self-administered. It may not be the true number of tests that staff members have taken. Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.|
| ```Pending Tests``` | ```Pending Tests (Incarcerated population, current)``` | The number of COVID-19 tests that are awaiting results. </br> **Notes**: Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.|
| ```Population``` | ```Population (Incarcerated population, current)```, </br> ```Population (Sheriff's office, current)```, </br> ```Population (Jail staff, current)```, </br> ```Population (Medical staff, current)``` | For the incarcerated population and jail staff, it is the number of individuals living or working in custody as of the specified date. For the sheriff's office, it is the total number of active employees as of the specified date. </br> **Notes**: </br> Incarcerated population/staff: For some counties, this may be the average daily population for the week or month prior to the specified date. Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.|
| ```Fully Vaccinated``` | ```Fully Vaccinated (Incarcerated population, current)```, </br> ```Fully Vaccinated (Sheriff's office, current)```, </br> ```Fully Vaccinated (Jail staff, current)```, </br> ```Fully Vaccinated (Medical staff, current)``` | The total number of individuals that are at least fully vaccinated. </br> **Notes**: </br> Incarcerated population: The count excludes any fully vaccinated incarcerated individual who is no longer in custody. In some counties, this may only include individuals who were vaccinated by the jail medical provider, i.e. excludes individuals who were vaccinated prior to their incarceration. </br> Sheriff's office/jail staff: For some counties, this may exclude fully vaccinated staff members who did not report or confirm their vaccination status with human resources. Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.|
| ```Boosted``` | ```Boosted (Incarcerated population, current)```, </br> ```Boosted (Sheriff's office, current)```, </br> ```Boosted (Jail staff, current)```, </br> ```Boosted (Medical staff, current)``` | The total number of individuals that have received at least one booser. </br> **Notes**: </br> Incarcerated population: The count excludes any boosted incarcerated individual who is no longer in custody. In some counties, this may only include individuals who received boosters from the jail medical provider, i.e. excludes individuals who were boosted prior to their incarceration. </br> Sheriff's office/jail staff: For some counties, this may exclude boosted staff members who did not report or confirm their vaccination status with human resources. Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.|
| ```Percent of Population Fully Vaccinated``` | ```Percent of Population Fully Vaccinated (Incarcerated population)```, </br> ```Percent of Population Fully Vaccinated (Sheriff's office)```, </br> ```Percent of Population Fully Vaccinated (Jail staff)```, </br> ```Percent of Population Fully Vaccinated (Medical staff)``` | The percentage of the population that is fully vaccinated at the least (may or may not be boosted). It is calculated using the fully vaccinated and population variables for the same date. </br> **Notes**: Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.|
| ```Percent of Population Boosted``` | ```Percent of Population Boosted (Incarcerated population)```, </br> ```Percent of Population Boosted (Sheriff's office)```, </br> ```Percent of Population Boosted (Jail staff)```, </br> ```Percent of Population Boosted (Medical staff)``` | The percentage of the population that has received at least one booster dose. It is calculated using the boosted and population variables for the same date. </br> **Notes**: Refer to the raw data files/PRA request submissions/PRA request responses and county specific data definitions for more details.|
		

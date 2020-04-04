# Coronavirus Tracker
These scripts let you retrieve data regarding coronavirus on a given country, and register an update of that data every 2 hours.  

## Requirements
Firt of all, to be able to even run any of these scripts, download [python](https://python.org/downloads/).
Secondly there are certain python modules required for the scripts to function correctly.
To install them, run next command:
```commandline
pip install requirements.txt
``` 

## Usage
### Retrieving Data
To get data from a country, run next command:
```commandline
py corona_tracker.py <country>
```
**Example** 
```commandline
py corona_tracker.py USA
```
It should output something like this:
```text
{
    "Country": "USA",
    "TotalCases": "104,142",
    "NewCases": "+16",
    "TotalDeaths": "1,696",
    "NewDeaths": "",
    "TotalRecovered": "2,522",
    "ActiveCases": "99,924",
    "Critical": "2,463",
    "TotCases": "315"
}

Date: 21:41 03/27/20
```
### Logging Data
To write that data to a text file, run next command:
```commandline
py coronavirus-stats-logger.py <country>
```

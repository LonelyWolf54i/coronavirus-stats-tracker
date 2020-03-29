# Coronavirus Tracker
These scripts let you retrieve data regarding coronavirus on a given country, and register an update of that data every certain time.  

## Usage 
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
To write that data to a text file, run next command:
```commandline
py coronavirus-stats-logger.py <country>
```

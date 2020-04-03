
import re
from bs4 import BeautifulSoup
from MyPythonLibs.prettyit import prettylist
import urllib
from datetime import datetime
import requests
import warnings
import traceback
import sys
from subprocess import call


def warn(*args, **kwargs):
    pass


warnings.warn = warn


class AppURLopener(urllib.request.FancyURLopener):
    version = "Mozilla/5.0"


website_url = r"https://www.worldometers.info/coronavirus/"
header = ['Country', 'TotalCases', 'NewCases', 'TotalDeaths',
          'NewDeaths', 'TotalRecovered', 'ActiveCases', 'Critical',
          'TotCases']


def track(country_name):
    try:
        opener = AppURLopener()
        response = opener.open(website_url)
        website_content = response.read()
        date = datetime.now().strftime("%H:%M %x")
        if len(sys.argv) == 2: country_name = sys.argv[1]
        soup = BeautifulSoup(website_content, 'lxml')
        rows = [str(r) for r in soup.find_all(id="main_table_countries_today")]
        soup2 = BeautifulSoup(''.join(rows), 'lxml')
        countries_data = re.search(country_name+'(\n(\+?[0-9]+,?[0-9]* *)?){8}',
                         soup2.get_text()).group().split("\n")
        countries_data[3] = countries_data[3].strip()
        data = {}
        for i in range(len(header)):
            data[header[i]] = countries_data[i]
        country_data = prettylist(data)
        print(country_data)
        print(f'\nDate: {date}')
        return country_data, date
    except KeyboardInterrupt:
        pass
    except OSError:
        call("netsh wlan connect ssid=CiscoST name=CiscoST".split(' '), shell=True)
        with open("coronavirus-tracker-OSError-errors.txt", "a") as error_log:
            error_log.write(f"\n\nDATE: {datetime.now().strftime('%H:%M %x')}\n")
            error_log.writelines(traceback.format_exc())
        track("Ecuador")
    except:
        with open("coronavirus-tracker-errors.txt", "a") as error_log:
            error_log.write(f"\n\nDATE: {datetime.now().strftime('%H:%M %x')}\n")
            error_log.writelines(traceback.format_exc())



if __name__ == '__main__':
    track("Ecuador")

from coronavirus_tracker import track
from datetime import datetime
import traceback
import sys
from time import sleep


def extract(country_name):
    if len(sys.argv) == 2: country_name = sys.argv[1]
    country_data, date = track(country_name)
    with open(f"coronavirus-{country_name}.txt", "a") as file:
        file.write("\n\n\n" + date + "\n")
        file.writelines(country_data)


def main():
    try:
        while True:
            extract("Ecuador")
            sleep(7200)
    except KeyboardInterrupt:
        pass
    except Exception:
        with open("coronavirus-stats-errors.txt", "a") as error_log:
            error_log.write(f"\n\nDATE: {datetime.now().strftime('%H:%M %x')}\n")
            error_log.writelines(traceback.format_exc())


main()
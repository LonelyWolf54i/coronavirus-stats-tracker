
from coronavirus_tracker import track
from datetime import datetime, timedelta
import traceback
import sys


def extract(country_name):
    if len(sys.argv) == 2: country_name = sys.argv[1]
    country_data, date = track(country_name)
    with open(f"coronavirus-{country_name}.txt", "a") as file:
        file.write("\n\n\n" + date + "\n")
        file.writelines(country_data)
    next_extraction_time = datetime.now() + timedelta(hours=2)
    return next_extraction_time.strftime('%H:%M')


def main():
    try:
        next_extraction_time = extract("Ecuador")
        while True:
            extraction_time = datetime.now().strftime('%H:%M') == next_extraction_time
            if extraction_time:
                next_extraction_time = extract("Ecuador")
    except KeyboardInterrupt:
        pass
    except Exception as e:
        with open("coronavirus-stats-errors.txt", "a") as error_log:
            error_log.write(f"\n\nDATE: {datetime.now().strftime('%H:%M %x')}\n")
            error_log.writelines(traceback.format_exc())


main()
import csv
import datetime
import calendar

def find_month_length():
    # get current date
    current_date = datetime.datetime.now()
    current_year = current_date.year
    current_month = current_date.month

    # get num of days in current_month
    first_day, num_days = calendar.monthrange(current_year, current_month)

    # dictionary to store day numbers and day abbreviations
    month_dict = {}

    # iterate through month days, add day number and abbreviation to month_dict
    for num in range(1, num_days + 1):
        day_num = num
        day_abbr = calendar.day_abbr[first_day]
        month_dict.update({day_num: day_abbr })
        first_day = (first_day + 1) % 7

    return month_dict

# load csv
def load_csv(csv_file):
    with open(csv_file, mode='r') as csv_file:
        # check if csv is empty
        if csv_file.read() == '':
            print('File is empty')
        else:
            # reset file pointer
            csv_file.seek(0)
            # read file
            csv_reader = csv.reader(csv_file)
            for lines in csv_reader:
                print(lines)

# create csv
def create_csv_daily():
    with open('daily_schedule.csv', mode='w', newline='') as daily_schedule:
        writer = csv.writer(daily_schedule)
        writer.writerow(['Time', 'Activity'])

def create_csv_monthly():
    with open('monthly_schedule.csv', mode='w', newline='') as monthly_schedule:
        writer = csv.writer(monthly_schedule)
        writer.writerow(['Day', 'Work / Day Off', 'Schedule'])

        # populate monthly csv
        for num, day in find_month_length().items():
            entry = f'{num}, {day}'
            writer.writerow([entry, '', ''])


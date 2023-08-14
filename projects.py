#!/usr/bin/env python
# coding: utf-8
# Prints out total timesheet hours by project for a range of dates.

from datetime import date, timedelta
import pandas as pd
from dateutil.parser import parse
from questionary import text

# make default start and end date from prior month
end_d = date.today().replace(day=1) - timedelta(days=1)
start_d = end_d.replace(day=1)
start_date = text('Enter Start Date, any format:', default=start_d.strftime('%b %e, %Y')).ask()
end_date = text('Enter End Date, any format:', default=end_d.strftime('%b %e, %Y')).ask()
start_d = parse(start_date)
end_d = parse(end_date)

ts_file_url = 'https://docs.google.com/spreadsheets/d/1ChHQ47LFvT_8jOmUfEOXm0l0x6ZlevQV2TVsEV6jo3c/export?format=tsv'
df = pd.read_csv(ts_file_url, sep='\t', parse_dates=['Date'])



dfr = df.query('Date >= @start_d and Date <= @end_d').groupby('Project').sum()[['Hours']]
print()
print(dfr)

#!/usr/bin/env python
# coding: utf-8
"""Script to calculate the Amp-hours that were supplied in each
bike battery charging session.
"""

days_to_include = float(input('Enter # of Days to Incude: '))
default_delta = 300.0  # default reading spacing in seconds
max_delta = 1000.0     # if spacing greater than this between charging readings, must be a new cycle
ending_amps = 0.1      # if amps are below this level charging is complete

import pandas as pd
import numpy as np
from bmondata import Server
from datetime import datetime, timedelta

server = Server('https://bmon.analysisnorth.com/')

start_ts = str(datetime.now()-timedelta(days=days_to_include))
df = server.sensor_readings('260034000c47343432313031_amps', start_ts=start_ts)
df.columns = ['amps']
df['ts'] = pd.to_datetime(df.index)

# create a DataFrame that only includes charging periods
df2 = df.query('amps > @ending_amps').copy()
df2['delta'] = df2.ts.diff().dt.seconds     # time between readings

# Fill the NA that was created by the diff() method.
df2.delta.fillna(default_delta, inplace=True)

# The start of the cycle is identified by a large time difference
# between a prior reading greater than ending amps.
# Clever trick with cumsum() to label all readings in a cycle with
# same id.
df2['cycle'] = np.where(df2.delta > max_delta, 1, 0).cumsum()

# Now make sure the first reading in each cyle uses the default time interval
# as that reading has a very time difference.
df2['delta'] = np.where(df2.delta > max_delta, default_delta, df2.delta)

df2['amp_hr'] =  df2.amps * df2.delta / 3600.0
df_results = df2.groupby('cycle').agg({'amp_hr': 'sum', 'ts': 'first'})

print(df_results.reset_index()[['ts', 'amp_hr']])

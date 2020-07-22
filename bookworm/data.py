import yaml
import pandas as pd
from sodapy import Socrata
import datetime as dt
import os

CHECKOUTS_QUERY = """
    SELECT
      usageclass as usage_class,
      checkoutmonth,
      checkoutyear,
      SUM(checkouts) AS monthly_checkouts
    WHERE
      checkoutyear >= 2017
      AND (
        materialtype = 'EBOOK'
        OR materialtype = 'AUDIOBOOK'
        OR materialtype = 'BOOK'
      )
    GROUP BY
      usageclass, checkoutmonth, checkoutyear
"""


def get_checkouts_by_usage_class(query=CHECKOUTS_QUERY, filename='usage_class_data.csv', force_download=False):
    """
    Loads mosnthly checkout data by usage class or pulls fresh data from
    data.seattle.gov using the CHECKOUTS_QUERY and a Socrata client and saves it
    locally. Once raw data is pulled or loaded, data types are fixed and a new
    date column is created.
    """
    if force_download or not os.path.exists(filename):
        with open("config.yml", 'r') as ymlfile:
            cfg = yaml.safe_load(ymlfile)
        client = Socrata(cfg['domain'], cfg['app_token'], timeout=180)

        print('Client created, querying data...')
        result = client.get(cfg['dataset_id'], query=query)
        df = pd.DataFrame.from_records(result)

        print('Caching data...')
        df.to_csv(filename, index=False)
    else:
        print('Loading cached data...')
        df = pd.read_csv(filename)

    print('Processing data...')
    for col in ['checkoutmonth', 'checkoutyear', 'monthly_checkouts']:
        df[col] = df[col].astype('int')

    df['month_date'] = df.apply(
        lambda x: dt.datetime(year=x['checkoutyear'], month=x['checkoutmonth'], day=1), axis=1
    )
    print('Done')
    return df[['month_date', 'usage_class', 'monthly_checkouts']].sort_values(by=['month_date', 'usage_class'])

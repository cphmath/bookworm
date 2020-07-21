import yaml
import pandas as pd
from sodapy import Socrata
import datetime as dt

CHECKOUTS_BY_USAGE_CLASS_QUERY = """
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


def get_checkouts_by_usage_class(query=CHECKOUTS_BY_USAGE_CLASS_QUERY):
    with open("config.yml", 'r') as ymlfile:
        cfg = yaml.safe_load(ymlfile)
    client = Socrata(cfg['domain'], cfg['app_token'], timeout=180)
    print('Client created, querying data...')
    result = client.get(cfg['dataset_id'], query=query)
    print('Raw data queried, processing data...')
    df = pd.DataFrame.from_records(result)

    for col in ['checkoutmonth', 'checkoutyear', 'monthly_checkouts']:
        df[col] = df[col].astype('int')

    df['month_date'] = df.apply(
        lambda x: dt.datetime(year=x['checkoutyear'], month=x['checkoutmonth'], day=1), axis=1
    )
    print('Done')
    return df[['month_date', 'usage_class', 'monthly_checkouts']].sort_values(by=['month_date', 'usage_class'])

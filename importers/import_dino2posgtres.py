import pandas as pd
import os

import sqlalchemy
from collections import defaultdict
from sqlalchemy import create_engine

engine = create_engine('postgresql://asfandyar@localhost:5432/asfandyar')

date_maps = defaultdict(list)
date_maps.update({'service_restriction.din': ['DATE_FROM', 'DATE_UNTIL'],
                  'calendar_of_the_company.din': ['DAY'],
                  'set_version.din': ['PERIOD_DATE_FROM', 'PERIOD_DATE_TO']})

for filename in os.listdir("/Users/asfandyar/IdeaProjects/dinoToGtfsVRR/gtfs_dino_vrr/dino_vrr_20170307/"):
    if filename.endswith(".din"):
        print('Loading {}'.format(filename))
        df = pd.read_csv('/Users/asfandyar/IdeaProjects/dinoToGtfsVRR/gtfs_dino_vrr/dino_vrr_20170307/' + filename, delimiter=';', skipinitialspace=True,
                         encoding='iso-8859-1', parse_dates=date_maps[filename])
        df.columns = [x.lower() for x in df.columns]
        for column in df.columns:
            if df[column].dtype == object:
                df[column] = df[column].str.strip()

        df.to_sql(filename.split(".")[0], engine, if_exists='replace',
                  dtype=dict((x.lower(), sqlalchemy.types.Date) for x in date_maps[filename]))
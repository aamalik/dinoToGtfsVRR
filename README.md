DINO To GTFS Conversion
=======================

This code is tested for DINO data from VRR. This is just a test project. Nothing more
Tested with python 2.7.10 on mac Sierra


### Make Database Schemas

```
sudo -u asfandyar createuser -s $(whoami); createdb $(whoami)
createuser -h 127.0.0.1 -U asfandyar -P -R -S rid
createdb -h 127.0.0.1 -U asfandyar -O asfandyar -E UTF8 ridprod
createdb -h 127.0.0.1 -U asfandyar -O asfandyar -E UTF8 kv1tmp
createdb -h 127.0.0.1 -U asfandyar -O asfandyar -E UTF8 ifftmp
cat sql_schema/rid.sql | psql -h 127.0.0.1 -U asfandyar -d ridprod
cat sql_schema/kv1tmp.sql | psql -h 127.0.0.1 -U asfandyar -d kv1tmp
psql -d asfandyar -c "create extension if not exists postgis;"
```

```
pip install -r requirements.txt
pip install psycopg2-binary
pip install wheel
pip install pandas
pip install virtualenv
pip install sqlalchemy
pip install psycopg2
```

Importing and exporting data to Postgres Database from bliksemintegration
```
python import_dino2posgtres.py ~/dinoData/dino_vrr_20170307
python vrr-import.py
psql -h localhost -U asfandyar -d ridprod -f exporters/gtfs.sql
```

### Sources

Code adapted from bliksemintegration from !(blikemlabs)[http://docs.plannerstack.org/en/latest/bliksem/Introduction/]

Dino data downloaded from !(openVRR)[https://www.openvrr.de/id/dataset/dino-daten]
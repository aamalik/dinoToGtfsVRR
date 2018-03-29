DINO To GTFS Conversion
=======================

This code is tested for DINO data from VRR. This is just a test project. Nothing more.
Tested with `python 2.7.10` on `Mac Sierra`


#### Create Postgres Database Schemas

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

#### Install python dependencies
```
pip install -r requirements.txt
pip install psycopg2-binary
pip install wheel
pip install pandas
pip install sqlalchemy
pip install psycopg2
```
if the above installations fail, maybe you should try installing using virtual environment.
```
pip install virtualenv
virtualenv venv
source venv/bin/activate
```


#### Final commands to convert from Dino data to GTFS  (Dino -> DinoPostgresFormat -> BliksemPostgresFormat -> GTFS)

Move Dino Data into corresponding Postgresql database
```
python import_dino2posgtres.py /dino_vrr/dino_vrr_20170307
```

Convert all data in our postgreql to bliksemintegration format in Postgres
```
python vrr-import.py
```

Convert from bliksemintegration format to GTFS data format and into our gtfs files which get saved in /gtfs folder
```
psql -h localhost -U asfandyar -d ridprod -f exporters/gtfs.sql
```




#### Sources

Code adapted from bliksemintegration from [blikemlabs](http://docs.plannerstack.org/en/latest/bliksem/Introduction/)

Dino data downloaded from [openVRR](https://www.openvrr.de/id/dataset/dino-daten)
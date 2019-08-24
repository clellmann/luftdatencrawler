# luftdatencrawler

The luftdatencrawler is designed to cyclicly crawl particulate matter ([PM](http://www.npi.gov.au/resource/particulate-matter-pm10-and-pm25))
data from [luftdaten.info](https://luftdaten.info/)

API: http://api.luftdaten.info/static/v1/data.json

It is supposed to run on a AWS cloud VM (EC2) instance and save data to the dynamoDB.

## How to run

First instantiate a dynamoDB and a Amazon EC2 VM on AWS.  
Edit `app.env.sample` with your credentials and rename to `app.env`.  
Connect to the VM via ssh and edit `crontab -e`. Enter `*/30 * * * * bash -c '(cd /home/ubuntu/luftdatencrawler && source ./app.env && python3 ./luftdatencrawler.py)  >/tmp/out.err 2>&1` and the crawler runs every 30 min and saves data to the dynamoDB instance.
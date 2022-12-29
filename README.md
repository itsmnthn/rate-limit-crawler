# DDos Script

## Setup

```bash
# install python3 if not install
# install venv
python3 -m pip install venv

# create virtual environment
python3 -m venv venv

# activate venv
source venv/bin/activate

# install required packages
pip install -r requirement.txt
```

## Running crawler

```bash
# url=url to request and rq=number of request to make default is 2000
scrapy crawl attack -a url=https://example.com -a rq=2000
```

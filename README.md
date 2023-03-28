## Email Webscraper

Simple webscraper that takes a depth and a list of urls, and returns all email addresses found.

### Prerequisites

- python installed

### Usage

1. install dependencies

```bash
pip install -r requirements.txt
```

2. Edit `config.json` to match your requirements.

`depth` specifies how many nested links from the main url the scraper should follow. Note that the higher the depth, the longer execution time.

`urls` is a list of main urls the scraper should start from.

3. Run the program

```bash
python app.py
```

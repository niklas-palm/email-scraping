## Email Webscraper

Simple webscraper that takes a depth and a list of urls, and stores all email addresses found in a csv file.

### Prerequisites

- python installed

### Usage

1. install dependencies

```bash
pip install -r requirements.txt
```

2. Edit `config.json` to match your requirements.

`depth` specifies how many nested links from the main url the scraper should follow. _Note that the higher the depth, the longer execution time_.

`urls` is a list of main urls the scraper should start from.

3. Run the program

```bash
python app.py
```

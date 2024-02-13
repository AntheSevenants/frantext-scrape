# frantext-scrape
A scraper for the frantext corpus for Julie Nijs

This is a scraper/downloader for the [frantext corpus](https://www.frantext.fr/repository/frantext/corpora/view). It was cobbled up in 30 minutes, so don't expect exquisite code quality.

Some texts in the frantext corpus are *sous droits* (under copyright). These cannot be downloaded.

## How to use

1. Install requirements  
    `pip install -r requirements.txt`
2. Run `python frantext-scrape.py` or `python3 frantext-scrape.py`
3. The program will scrape all frantext corpus files available.
# frantext-scrape
A scraper for the frantext corpus for Julie Nijs

**UPDATE 2024-02-14**

It seems that, likely as a response to this scraper, the frantext corpus is now entirely behind a paywall. This means it is no longer possible to download text files for free. You're welcome.

This is a scraper/downloader for the [frantext corpus](https://www.frantext.fr/repository/frantext/corpora/view). It was cobbled up in 30 minutes, so don't expect exquisite code quality.

Some texts in the frantext corpus are *sous droits* (under copyright). These cannot be downloaded.

## How to use

1. Install requirements  
    `pip install -r requirements.txt`
2. Run `python frantext-scrape.py` or `python3 frantext-scrape.py`
3. The program will scrape all frantext corpus files available.

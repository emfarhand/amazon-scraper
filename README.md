```markdown
# Amazon Cooking Oil Scraper

## Project Overview
This project demonstrates a basic web scraping and data processing pipeline using Python.  
The scraper collects product data for **cooking oil** from Amazon search results and stores it in a structured CSV format for further analysis.

---

## Project Structure
```

ecommerce-analyst/
├─ data/
│  └─ raw/
│     └─ dt=YYYY-MM-DD/
│        └─ amazon_oil.csv
├─ include/
│  └─ config.py
├─ scripts/
│  └─ scrape_amazon.py
└─ README.md

````

- `data/raw/` → stores raw CSV files partitioned by date  
- `include/config.py` → contains URL, query, headers, delay  
- `scripts/scrape_amazon.py` → main scraper script  

---

## Configuration
Edit `include/config.py` to set your scraping parameters:

```python
BASE_URL = "https://www.amazon.com/s"
QUERY = "cooking oil"
HEADERS = {
    "User-Agent": "Mozilla/5.0",
    "Accept-Language": "en-US,en;q=0.9"
}
DELAY = 2  # seconds between requests
````

---

## Dependencies

Install required Python packages:

```bash
pip install requests beautifulsoup4 pandas
```

---

## How to Run

```bash
python scripts/scrape_amazon.py
```

**Output:**
`data/raw/dt=YYYY-MM-DD/amazon_oil.csv`

---

## Output CSV

| Column       | Description          |
| ------------ | -------------------- |
| title        | Product title        |
| rating       | Product rating       |
| review_count | Number of reviews    |
| scrape_date  | Date of scraping     |
| source       | Data source (Amazon) |

---

## Data Pipeline Flow

```
Amazon Search Page
        |
        v
HTTP Request (requests)
        |
        v
HTML Parsing (BeautifulSoup)
        |
        v
Raw CSV Output
```

---

## Limitations

* The scraper does **not handle CAPTCHA or IP blocking**
* Data availability depends on **Amazon page structure**
* Only suitable for **educational and portfolio purposes**

---

## Learning Objectives

* Basic web scraping with requests and BeautifulSoup
* Partitioning raw data by date
* Generating structured CSVs for downstream analysis
* Creating simple, maintainable Python project structure

---

## Future Improvements

* Add a cleaning layer for normalized/typed data
* Create a curated analytics layer (e.g., top products by review_count)
* Add error logging and retry mechanisms
* Expand to multiple pages or multiple products

```

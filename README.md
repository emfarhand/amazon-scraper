# 🛢️ Amazon Cooking Oil Scraper

A simple Python scraper that collects product data for cooking oil from Amazon search results.  
This project stores data in structured CSV format for further analysis.

---

## 📌 Project Overview

This scraper is designed to:

- Collect product titles, ratings, and review counts from Amazon.  
- Partition raw data by date.  
- Provide a clean dataset for portfolio or educational purposes.

---

## 🛠️ Tech Stack

- **Language:** Python 3  
- **Libraries:**  
  - `requests` – HTTP requests  
  - `BeautifulSoup` – HTML parsing  
  - `pandas` – Optional CSV handling  
- **Tested on:** Windows 10 / Linux with Python 3.10+

---

## 🎯 Features

- Scrapes Amazon search results for cooking oil.  
- Saves raw data in CSV format, partitioned by scrape date.  
- Structured columns: `title`, `rating`, `review_count`, `scrape_date`, `source`.

---

## ▶️ How to Run

1. **Clone this repository:**
   ```bash
   git clone https://github.com/emfarhand/amazon-scraper.git
   cd amazon-scraper
Install dependencies:

bash
Salin kode
pip install -r requirements.txt
Run scraper:

bash
Salin kode
python scripts/scrape_amazon.py
Output CSV:
data/raw/dt=YYYY-MM-DD/amazon_oil.csv

📬 Contact
Email: farhanlangsa003@gmail.com
LinkedIn: linkedin.com/in/emfarhand

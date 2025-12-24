from bs4 import BeautifulSoup

def parse_products(html):
    soup = BeautifulSoup(html, "html.parser")
    products = []

    results = soup.select("div[data-component-type='s-search-result']")

    for item in results:
        title = item.select_one("h2 span")
        rating = item.select_one("span.a-icon-alt")
        reviews = item.select_one("span.s-underline-text")

        products.append({
            "title": title.text.strip() if title else None,
            "rating": rating.text.split()[0] if rating else None,
            "review_count": reviews.text.strip("()") if reviews else None
        })

    return products

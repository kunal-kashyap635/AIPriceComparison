import requests
from config import SERP_API_KEY

# print(SERP_API_KEY)

def search_product_prices(product_name):
    url = "https://serpapi.com/search.json"

    params = {
        "engine": "google_shopping",
        "q": product_name,
        "hl": "en",
        "gl": "in",
        "api_key": SERP_API_KEY,
    }

    data = requests.get(url, params=params).json()

    products = []
    for item in data.get("shopping_results", [])[:5]:
        products.append(
            {
                "title": item.get("title", "N/A"),
                "price": item.get("price", "N/A"),
                "source": item.get("source", "Unknown"),
                "rating": item.get("rating", "N/A"),
                "reviews": item.get("reviews", "N/A"),
                "thumbnail": item.get("thumbnail", "N/A"),
            }
        )

    return products

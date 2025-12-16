from serp_tool import search_product_prices
from llm import recommend_best_deal

def run_price_agent(product_name):
    
    products = search_product_prices(product_name)

    if not products:
        return {"products": [], "decision": "No products found"}

    decision = recommend_best_deal(products)

    return {
        "products": products,
        "decision": decision
    }

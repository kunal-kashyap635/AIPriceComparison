from fastapi import FastAPI
from pydantic import BaseModel
from agent import run_price_agent

app = FastAPI(title="AI Price Comparison Agent")

class ProductRequest(BaseModel):
    product_name: str

@app.get("/")
def home():
    return {"Message": "AI Price API", "Status": "Runing"}

@app.get("/health")
def health():
    return {
        "Owner": "Kunal kashyap",
        "Version": "1.0.0",
    }

@app.post("/compare")
def compare_prices(req: ProductRequest):
    return run_price_agent(req.product_name)

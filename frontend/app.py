import streamlit as st
import requests
import os

API_URL = os.getenv("API_URL")

# ---------------- PAGE CONFIG ----------------
st.set_page_config(page_title="AI Price Comparison", layout="wide")

# ---------------- CUSTOM CSS ----------------
st.markdown(
    """
<style>
.product-card {
    border: 1px solid #e5e7eb;
    border-radius: 14px;
    padding: 14px;
    margin-bottom: 20px;
    background-color: white;
    box-shadow: 0 4px 10px rgba(0,0,0,0.04);
}

.product-image img {
    width: 100%;
    height: 230px;
    object-fit: contain;
    margin-bottom: 10px;
}

.product-title {
    font-size: 15px;
    font-weight: 600;
    margin-bottom: 6px;
}
</style>
""",
    unsafe_allow_html=True,
)

# ---------------- TITLE ----------------
st.title("🛒 AI Product Price Comparison Agent")

product_name = st.text_input("Enter product name")

# ---------------- BUTTON ACTION ----------------
if st.button("Compare Prices") and product_name:
    with st.spinner("🔍 Searching best deals..."):
        response = requests.post(API_URL, json={"product_name": product_name})
        data = response.json()

    products = data.get("products", [])
    decision = data.get("decision", "")

    # ---------------- PRODUCTS GRID ----------------
    if products:
        st.subheader("📦 Products Found")

        cols = st.columns(3)

        for idx, p in enumerate(products):
            with cols[idx % 3]:
                st.markdown('<div class="product-card">', unsafe_allow_html=True)

                if p.get("thumbnail"):
                    st.markdown(
                        f"""
                        <div class="product-image">
                            <img src="{p['thumbnail']}">
                        </div>
                        """,
                        unsafe_allow_html=True,
                    )

                st.markdown(
                    f'<div class="product-title">{p["title"][:80]}</div>',
                    unsafe_allow_html=True,
                )

                st.write(f"💰 **{p['price']}**")
                st.write(f"🏪 {p['source']}")
                st.write(f"⭐ {p['rating']} ({p['reviews']})")

                st.markdown("</div>", unsafe_allow_html=True)

        # ---------------- AI DECISION ----------------
        st.subheader("🤖 AI Recommendation")
        st.markdown(decision)

    else:
        st.warning("❌ No products found.")

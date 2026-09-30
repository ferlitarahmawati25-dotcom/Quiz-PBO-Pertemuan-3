import json
import csv
from typing import List, Dict, Any

# 1. Membaca File JSON
input_file_json: str = "data/raw_products.json"

with open(input_file_json, mode="r", encoding="utf-8") as file:
    payload: Dict[str, Any] = json.load(file)

products: List[Dict[str, Any]] = payload.get("products", [])

# 2. Transformasi Data Menggunakan For Loop
formatted_products: List[Dict[str, Any]] = []

for product in products:
    if product["is_available"] is True:
        formatted_item: Dict[str, Any] = {
            "item_code": product["item_code"],
            "product_name": product["name"].upper(),
            "price": float(product["price"]),
            "stock_category": "High Stock"
            if product["stock"] >= 20
            else "Low Stock"
        }

        formatted_products.append(formatted_item)

# 3. Menyimpan ke File CSV
output_path: str = "data/products_loop.csv"

headers = [
    "item_code",
    "product_name",
    "price",
    "stock_category"
]

with open(output_path, mode="w", encoding="utf-8", newline="") as file:
    writer = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(formatted_products)

print(f"[SUCCESS] Data berhasil disimpan di: {output_path}")
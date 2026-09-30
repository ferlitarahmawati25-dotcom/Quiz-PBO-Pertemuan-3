import json
import csv
from typing import List, Dict, Any

# 1. READ: Membaca langsung dari file JSON
input_file_json: str = "data/raw_products.json"

with open(input_file_json, mode="r", encoding="utf-8") as file:
    payload: Dict[str, Any] = json.load(file)

raw_products: List[Dict[str, Any]] = payload.get("products")
products: List[Dict[str, Any]] = raw_products if isinstance(raw_products, list) else []

# 2. TRANSFORM: Transformasi menggunakan filter dan lambda

# [Langkah 1] Filter Data
filtered_products = filter(
    lambda item: item["is_available"] is True,
    products
)

# [Langkah 2] Mapping Data
mapping_data = map(
    lambda item: {
        "item_code": item["item_code"],
        "product_name": item["name"].upper(),
        "price": float(item["price"]),
        "stock_category": "High Stock"
        if item["stock"] >= 20
        else "Low Stock"
    },
    filtered_products
)

# [Langkah 3] Convert map object to list
available_products: List[Dict[str, Any]] = list(mapping_data)

# 3. WRITE: Menyimpan ke file CSV
output_path: str = "data/products_fp.csv"

headers: List[str] = [
    "item_code",
    "product_name",
    "price",
    "stock_category"
]

with open(output_path, mode="w", encoding="utf-8", newline="") as file:
    writer: csv.DictWriter = csv.DictWriter(file, fieldnames=headers)
    writer.writeheader()
    writer.writerows(available_products)

print(f"[SUCCESS] Data berhasil disimpan di: {output_path}")
import requests
import csv
import os
from logging_config import logging   # ← إضافة اللوق هنا

# 1) رابط API مجاني يعطينا بيانات جاهزة
url = "https://jsonplaceholder.typicode.com/posts"
logging.info("Sending request to API...")

# 2) نرسل طلب لجلب البيانات
response = requests.get(url)
logging.info("API response received.")

# 3) نحول البيانات إلى JSON
data = response.json()
logging.info(f"Fetched {len(data)} records from API.")

# 4) نفتح ملف CSV ونكتب البيانات فيه
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
csv_path = os.path.join(BASE_DIR, "..", "data", "raw", "posts_data.csv")

logging.info(f"Saving data to CSV at: {csv_path}")

with open(csv_path, "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # نكتب العناوين
    writer.writerow(["userId", "id", "title", "body"])
    
    # نكتب البيانات
    for item in data:
        writer.writerow([item["userId"], item["id"], item["title"], item["body"]])

logging.info("Data saved successfully!")
print("Data saved successfully!")

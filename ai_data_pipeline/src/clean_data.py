import pandas as pd
import os

# تحديد المسار الديناميكي
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
raw_path = os.path.join(BASE_DIR, "..", "data", "raw", "posts_data.csv")
processed_path = os.path.join(BASE_DIR, "..", "data", "processed", "clean_posts.csv")

# قراءة البيانات
df = pd.read_csv(raw_path)

# تنظيف البيانات (ما عندنا missing لكن نرتب الأعمدة)
df = df.drop_duplicates()  # إزالة التكرارات
df.columns = df.columns.str.lower()  # توحيد أسماء الأعمدة

# حفظ البيانات النظيفة
df.to_csv(processed_path, index=False)

print("Clean data saved successfully!")

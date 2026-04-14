import os
import subprocess
import traceback
from logging_config import logging   # ← اللوق

try:
    BASE_DIR = os.path.dirname(os.path.abspath(__file__))

    scripts = [
        "data_pipeline.py",        # جلب البيانات
        "clean_data.py",           # تنظيف البيانات
        "feature_engineering.py"   # استخراج الميزات
    ]

    logging.info("Starting full pipeline...")
    print("Starting full pipeline...\n")

    for script in scripts:
        script_path = os.path.join(BASE_DIR, script)

        logging.info(f"Running script: {script}")
        print(f"Running: {script}")

        try:
            subprocess.run(["python", script_path], check=True)
        except subprocess.CalledProcessError as e:
            logging.error(f"Script failed: {script}", exc_info=True)
            raise Exception(f"Pipeline stopped because {script} failed.") from e

        logging.info(f"Finished script: {script}")
        print(f"Finished: {script}\n")

    logging.info("Pipeline completed successfully!")
    print("Pipeline completed successfully!")

except Exception as e:
    logging.error("A critical error occurred in pipeline.py", exc_info=True)
    raise e

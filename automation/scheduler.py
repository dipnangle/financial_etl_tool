import schedule
import time
from main import run_etl_pipeline


def job():
    print("Running ETL pipeline ....")
    run_etl_pipeline()
    
    

def start_scheduler():
    schedule.every().day.at("9:00").do(job)
    while True:
        schedule.run_pending()
        time.sleep(1)
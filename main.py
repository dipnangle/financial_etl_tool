from data_fetch.fetch_yahoo import fetch_stock_data
from data_cleaning.clean_transformation import clean_data, engineering_feature
from data_cleaning.validation import data_validate
from database.db_connector import get_db_engine
from database.save_to_db import save_dataframe

def run_etl_pipeline():
    ticker = "AAPL"  # <-- You can change ticker here
    print(f"Running ETL for {ticker}...")
    print("starting to fetch the data")
    df = fetch_stock_data(ticker, "2023-01-01", "2023-12-31")
    
    if df is None:
        print("Failed to fetch the stick data")
        return
    
    df = clean_data(df, ticker)
    df = engineering_feature(df, ticker)
    
    df.dropna(inplace=True)
    
    data_validate(df, ticker)
    
    print(df.columns)
    
    engine = get_db_engine()
    save_dataframe(df, f"{ticker.lower()}_stock", engine)
    print("ETL pipeline saved successfully")
    
if __name__ == "__main__":
    run_etl_pipeline()
       


import yfinance as yf
import pandas as pd


def fetch_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """_summary_ : Fetch Historical stock data from yahoo finance

    Args:
        ticker (str): _description_
        start_date (str): _description_
        end_date (str): _description_

    Returns:
        pd.DataFrame: _description_
        
    """
    
    df = yf.download(ticker, start=start_date, end=end_date, auto_adjust=True)
    
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = ['_'.join(col).strip() for col in df.columns.values]
    
    df.reset_index(inplace=True)
    
    print(df.head())
    
    return df
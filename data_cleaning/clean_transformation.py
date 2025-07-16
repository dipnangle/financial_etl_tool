import pandas as pd
import numpy as np

def clean_data(df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """_summary_ : clean data with handling missing values, duplicates and feature engineering

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    
    print("Cleaning data...")
    # Drop rows with null values
    df.dropna(inplace=True)
    df.sort_values(by='Date', inplace=True)
    df.reset_index(drop=True, inplace=True)
    return df

def engineering_feature(df: pd.DataFrame, ticker: str) -> pd.DataFrame:
    """_summary_: add volatility and moving average in the stock

    Args:
        df (pd.DataFrame): _description_

    Returns:
        pd.DataFrame: _description_
    """
    
    print("Engineering features...")
    price_col = f"Close_{ticker}"

    # Daily return
    df[f'{ticker}_Daily_Return'] = df[price_col].pct_change()

    # 20-day Moving Average
    df[f'{ticker}_MA_20'] = df[price_col].rolling(window=20).mean()
    
    # 20 days EWM
    df[f'{ticker}_EMA_20'] = df[price_col].ewm(span=20, adjust=False).mean()

    # 20-day Volatility
    df[f'{ticker}_Volatility_20'] = df[f'{ticker}_Daily_Return'].rolling(window=20).std()
    
    # day 14 RSI
    delta = df[price_col].diff()
    gain = delta.clip(lower=0)
    loss = -delta.clip(upper=0)
    avg_gain = gain.rolling(window=14).mean()
    avg_loss = loss.rolling(window=14).mean()
    rs = avg_gain / avg_loss
    df[f'{price_col}_rsi_14'] = 100 - (100 /( 1 + rs ))
    
    #drop rows if Nan has Detected 
    df.dropna(inplace=True)

    return df
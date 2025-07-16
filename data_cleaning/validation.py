import pandas as pd
import numpy as np

def data_validate(df: pd.DataFrame, ticker: str):
    """_summary_
    ensuring the data is not null and the positive if we want to process

    Args:
        df (pd.DataFrame): _description_
    """
    print("Validating data...")
    price_col = f"Close_{ticker}"
    assert not df.isnull().values.any(), "Data contains null values!"
    assert (df[price_col] > 0).all(), "Found non-positive prices!"
    print("Validation passed ✅")
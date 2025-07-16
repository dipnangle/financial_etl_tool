from sqlalchemy import create_engine

def get_db_engine(db_url="sqlite:///financial_data.db"):
    """_summary_
    create database engine to connect database
    
    Args:
        db_url (str, optional): _description_. Defaults to "sqlite:///financial_data.db".
    """
    
    return create_engine(db_url)
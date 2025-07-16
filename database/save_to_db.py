def save_dataframe(df, table_name, engine):
    """_summary_
    save the Pandas Dataframe in Database

    Args:
        df (_type_): _description_
        table_name (_type_): _description_
        engine (_type_): _description_
    """
    
    df.to_sql(table_name, con=engine, if_exists='replace', index=False)
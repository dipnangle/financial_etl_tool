# Financial Data ETL Automation Tool

## Project Description

An automated ETL pipeline that fetches stock price data, engineers technical indicators like MA20, EMA, RSI, and Volatility, and saves processed data into a SQL database for downstream financial analysis.

## Features

- Data extraction from Yahoo Finance using yfinance  
- Data cleaning and validation  
- Feature engineering: Moving averages, RSI, volatility, EMA  
- Saves processed data to SQLite database  
- Easily extensible for additional stocks or features  

## Tech Stack

- Python 3.x  
- Pandas, NumPy  
- yfinance  
- SQLAlchemy (or sqlite3)  
- SQLite DB  

## Setup Instructions

```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
pip install -r requirements.txt
python main.py

```

## Project Structure
```
financial_etl_tool/
│
├── data_fetch/
│   ├── fetch_yahoo.py
│   ├── fetch_fred.py
│
├── data_cleaning/
│   ├── clean_transform.py
│   ├── validation.py
│
├── database/
│   ├── db_connector.py
│   ├── save_to_db.py
│
├── automation/
│   ├── scheduler.py
│
├── tests/
│   ├── test_fetch.py
│   ├── test_cleaning.py
│
├── main.py
├── requirements.txt
└── README.md
```

## Usage
- Clone the repository
- Set up your Python environment and install dependencies (see Setup Instructions)
- Run python main.py to execute the ETL pipeline
- The processed data will be saved into a local SQLite database (financial_data.db)
- Extend the pipeline by adding new tickers or features as needed

## Future Enhancements
- Automate ETL execution with scheduling (cron jobs or Windows Task Scheduler)
- Add more advanced technical indicators (e.g., MACD, Bollinger Bands)
- Deploy the ETL pipeline on a cloud server or containerize using Docker
- Add logging and error handling for better monitoring
- Build a REST API to serve the processed financial data

## Author
Dipesh Maruti Nangle
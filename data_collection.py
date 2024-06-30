import yfinance as yf
from autogen import register_tool

def fetch_historical_stock_data(ticker, start_date, end_date):
    data = yf.download(ticker, start=start_date, end=end_date)
    return data.to_dict('list')

def fetch_financial_news_from_directory(directory_path):
    documents = SimpleDirectoryReader(directory_path).load_data()
    return documents

def fetch_financial_reports_from_directory(directory_path):
    documents = SimpleDirectoryReader(directory_path).load_data()
    return documents

register_tool("StockDataTool", fetch_historical_stock_data, description="Fetch historical stock data for a given ticker symbol")
register_tool("NewsDataTool", fetch_financial_news_from_directory, description="Fetch financial news from a directory")
register_tool("ReportsDataTool", fetch_financial_reports_from_directory, description="Fetch financial reports from a directory")

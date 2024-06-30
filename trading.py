from llama_index.core.tools import FunctionTool

def execute_trade(ticker, action, quantity):
    # Placeholder for trade execution logic
    print(f"Executing trade: {action} {quantity} shares of {ticker}")

trading_tool = FunctionTool.from_defaults(execute_trade, name="TradingTool", description="Execute buy/sell orders")

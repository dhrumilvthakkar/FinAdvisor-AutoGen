from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from config import OPENAI_API_KEY
import pandas as pd


llm = OpenAI(model="gpt-3.5-turbo-0613", api_key=OPENAI_API_KEY)


def provide_advice(customer_data, investment_strategy, market_analysis, industry_trends, financial_ratios, portfolio_management):
    agent = OpenAIAgent.from_tools([], llm=llm, verbose=True)
    prompt = (
        f"Based on the customer data {customer_data}, the generated investment strategy {investment_strategy}, "
        f"and the following analysis:\n\n"
        f"Market Analysis: {market_analysis}\n"
        f"Industry Trends: {industry_trends}\n"
        f"Financial Ratios: {financial_ratios}\n"
        f"Portfolio Management: {portfolio_management}\n\n"
        "provide detailed and personalized financial advice. Include considerations for risk tolerance, investment horizon, and financial goals."
    )
    response = agent.call(prompt)
    return response["choices"][0]["text"].strip()

def generate_market_analysis(historical_data):
    # Placeholder for a more sophisticated market analysis logic
    market_trend = "The market trend shows a bullish sentiment over the past year."
    return market_trend

def generate_industry_trends(ticker):
    # Placeholder for a more sophisticated industry trends analysis
    industry_trend = f"The technology sector, including companies like {ticker}, has been experiencing significant growth due to advancements in AI and cloud computing."
    return industry_trend


def calculate_financial_ratios(historical_data):
    # Placeholder for a more sophisticated financial ratios calculation
    df = pd.DataFrame(historical_data)
    pe_ratio = df['Close'].iloc[-1] / df['Earnings'].iloc[-1]  # Simplified example
    return f"PE Ratio: {pe_ratio:.2f}"

def portfolio_management_advice(customer_risk_tolerance):
    # Placeholder for a more sophisticated portfolio management advice
    if customer_risk_tolerance == "high":
        advice = "Consider a diversified portfolio with a higher percentage in equities and growth stocks."
    elif customer_risk_tolerance == "medium":
        advice = "Consider a balanced portfolio with a mix of equities, bonds, and mutual funds."
    else:
        advice = "Consider a conservative portfolio with a higher percentage in bonds and stable value funds."
    return advice

advice_tool = FunctionTool.from_defaults(provide_advice, name="AdvisoryTool", description="Provide financial advice based on comprehensive

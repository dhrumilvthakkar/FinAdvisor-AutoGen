import pandas as pd
from sklearn.linear_model import LinearRegression
import mlflow
from llama_index import ServiceContext
from llama_index.agent.openai import OpenAIAgent
from config import MLFLOW_TRACKING_URI, OPENAI_API_KEY
from llama_index.llms.openai import OpenAI

llm = OpenAI(model="gpt-3.5-turbo-0613", api_key=OPENAI_API_KEY)

def generate_investment_strategy(historical_data, sentiment_analysis_results, customer_risk_tolerance):
    with mlflow.start_run():
        # Feature engineering (Replace this with your actual feature engineering logic)
        df = pd.DataFrame(historical_data)
        df['SMA_20'] = df['Close'].rolling(window=20).mean()
        df['Sentiment'] = [result['sentiment'] for result in sentiment_analysis_results]

        # Model training (Replace this with your actual model training logic)
        X = df[['SMA_20', 'Sentiment']]
        y = df['Close']
        model = LinearRegression()
        model.fit(X, y)

        # Prediction (Replace this with your actual prediction logic)
        next_day_sentiment = sentiment_analysis_results[-1]['sentiment'] 
        next_day_sma_20 = df['SMA_20'].iloc[-1]
        next_day_prediction = model.predict([[next_day_sma_20, next_day_sentiment]])[0]

        # Log model and parameters to MLflow
        mlflow.sklearn.log_model(model, "linear_regression_model")
        mlflow.log_params({"customer_risk_tolerance": customer_risk_tolerance})

        # Generate strategy based on prediction and risk tolerance
        service_context = ServiceContext.from_defaults(llm=llm)
        agent = OpenAIAgent.from_tools([], llm=llm, service_context=service_context, verbose=True)

        prompt = f"Given a predicted stock price of {next_day_prediction:.2f} and a customer risk tolerance of {customer_risk_tolerance}, generate an investment strategy."
        response = agent.chat(prompt)
        return response.response

strategy_generation_tool = FunctionTool.from_defaults(generate_investment_strategy, name="StrategyGenerationTool", description="Generate investment strategy based on data")


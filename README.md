# FinAdvisor-AutoGen

# Multi-Agent Financial Advisory System with LlamaIndex and AutoGen

This project demonstrates a sophisticated multi-agent system designed to provide comprehensive financial advisory services, leveraging the strengths of both LlamaIndex and AutoGen. The system integrates multiple intelligent agents, each specializing in a specific aspect of financial analysis and decision-making, to deliver personalized, data-driven advice.

## Table of Contents

- [Project Overview](#project-overview)
- [Features](#features)
- [Architecture](#architecture)
- [Agents](#agents)
- [Tools and Technologies](#tools-and-technologies)
- [Getting Started](#getting-started)
  - [Installation](#installation)
  - [Configuration](#configuration)
  - [Usage](#usage)
  - [Troubleshooting](#troubleshooting)
- [Future Enhancements](#future-enhancements)
- [Contributing](#contributing)
- [License](#license)
- [Disclaimer](#disclaimer)

## Project Overview

This prototype simulates an AI-powered financial advisory platform that aims to democratize access to high-quality financial guidance. By combining the knowledge management capabilities of LlamaIndex with the conversation orchestration of AutoGen, the system offers a unique approach to generating personalized investment strategies and financial advice.

## Features

- **Multi-Agent Collaboration:** Leverages multiple specialized agents, each handling a specific task, to achieve a comprehensive financial analysis.
- **LlamaIndex Knowledge Base:** Utilizes LlamaIndex for efficient data indexing, retrieval, and knowledge management, providing agents with relevant information from diverse sources.
- **AutoGen Conversation Orchestration:** Employs AutoGen to manage seamless interactions and communication between agents, ensuring a smooth and informative conversation flow.
- **Personalized Financial Advice:** Delivers tailored investment strategies and financial recommendations based on individual user profiles and preferences.
- **Market and Industry Analysis:** Analyzes market trends, industry developments, and news sentiment to inform investment decisions.
- **Financial Ratio Calculation:** Calculates and interprets key financial ratios for a deeper understanding of investment options.
- **Portfolio Optimization:** Optimizes portfolio allocation based on risk tolerance and expected returns.
- **Risk Assessment:** Evaluates the risk profile of investment choices using volatility analysis.
- **Trading Simulation (Conceptual):** Simulates trade execution based on generated investment strategies.
- **User Interface Interaction (Conceptual):**  Gathers user input and presents information through a user-friendly interface.
- **Explainability:** Provides clear explanations for the reasoning behind investment strategies.

## Architecture

The system architecture combines the strengths of LlamaIndex and AutoGen:

- **LlamaIndex Agents:** Specialized agents are created using LlamaIndex to handle data collection, sentiment analysis, strategy generation, and advisory tasks.
- **AutoGen Agents:** An assistant agent is created using AutoGen, which communicates with the user and uses LlamaIndex agents as tools to accomplish specific tasks. 
- **Orchestration:** AutoGen manages the conversation flow and coordinates interactions between the assistant agent and the user.

## Agents

- **User Proxy Agent (AutoGen):** Represents the user and communicates their financial information and preferences.
- **Financial Advisor Assistant Agent (AutoGen):** Orchestrates the conversation, interacts with the user, and delegates tasks to specialized LlamaIndex agents.
- **LlamaIndex Agents:**
    - **Stock Data Agent:** Fetches historical stock data.
    - **News Data Agent:** Collects and analyzes financial news.
    - **Reports Data Agent:** Analyzes financial reports.
    - **Sentiment Analysis Agent:** Performs sentiment analysis on news and reports.
    - **Strategy Generation Agent:** Generates investment strategies.
    - **Advisory Agent:** Provides personalized financial advice.
    - **Market Analysis Agent:** Analyzes market trends.
    - **Industry Trends Agent:** Assesses industry-specific trends.
    - **Financial Ratios Agent:** Calculates financial ratios.
    - **Portfolio Management Agent:** Provides portfolio advice.
    - **Risk Assessment Agent:** Assesses investment risk.
    - **Explainability Agent:** Explains the rationale behind investment decisions.
    - **Trading Agent:** Simulates trade execution (conceptual).

## Tools and Technologies

- **LlamaIndex:** Enables data indexing, retrieval, and knowledge management for agents.
- **AutoGen:** Facilitates multi-agent conversation and workflow orchestration.
- **OpenAI:** Powers the language models used by the agents for natural language understanding and generation.
- **yfinance:** Fetches historical stock data.
- **Azure Cognitive Services:** Provides sentiment analysis capabilities.
- **MLflow:** (Optional) For tracking machine learning experiments.
- **Gradio:** (Optional) For building a user interface.

## Getting Started

### Installation

1. **Clone the Repository:** 
   ```bash
   git clone https://github.com/dhrumilvthakkar/FinAdvisor-AutoGen.git
   ```
2. **Create a Virtual Environment (Recommended):**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Install Dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

### Configuration

1. **Obtain API Keys and Endpoints:**
    - Get an API key from OpenAI and set the `OPENAI_API_KEY` environment variable.
    - Get an API key and endpoint for Azure Text Analytics and set the `AZURE_KEY` and `AZURE_ENDPOINT` environment variables.

### Usage

1. **Prepare Data:**
    - Organize financial news articles in a `news_data` directory.
    - If you have financial reports, place them in a `reports_data` directory.
2. **Run the Orchestrator:**
    ```bash
    python orchestrator_autogen.py
    ```

## Troubleshooting

- **API Errors:** Make sure your Azure and OpenAI API keys and endpoints are correct.
- **Data Issues:** Verify that the `news_data` and `reports_data` folders contain valid data files.
- **Dependency Issues:** Ensure all required libraries are installed in your virtual environment. Refer to `requirements.txt`.
- **Other Errors:** If you encounter other issues, please refer to the project's documentation or open an issue on the GitHub repository.

## Future Enhancements

This project serves as a foundation for a comprehensive financial advisory system. There are numerous exciting directions for further development and enhancement:

### Core System Improvements

*   **Real-Time Data Integration:**
    *   Integrate with real-time market data feeds (e.g., Alpaca, Interactive Brokers API) to provide up-to-the-minute analysis and decision-making.
    *   Incorporate real-time news sentiment analysis from social media and financial news sources.
*   **Advanced Machine Learning Models:**
    *   Explore and implement more sophisticated machine learning models for stock price prediction, risk assessment, and portfolio optimization (e.g., time series forecasting, reinforcement learning).
    *   Develop models to predict market trends based on macroeconomic indicators and alternative data sources.
*   **Backtesting and Performance Evaluation:**
    *   Implement a robust backtesting framework to evaluate the historical performance of generated investment strategies under different market conditions.
    *   Track and analyze the performance of real trades executed by the system (once trading is fully implemented).

### User Experience and Interface

*   **Interactive Web Application:**
    *   Develop a user-friendly web interface (e.g., using React, Angular, or Vue.js) to provide a seamless user experience.
    *   Allow users to input their financial information, preferences, and goals interactively.
    *   Visualize portfolio performance, risk metrics, and investment recommendations.
*   **Natural Language Interface:**
    *   Enhance the User Interface Agent to understand complex financial queries posed in natural language.
    *   Enable users to ask questions and receive personalized financial advice in a conversational manner.
*   **Customizable Dashboards:**
    *   Offer customizable dashboards to visualize relevant financial information based on user preferences.

### Expanded Functionality

*   **Expanded Asset Classes:**
    *   Support additional asset classes beyond stocks, such as bonds, commodities, cryptocurrencies, and real estate.
    *   Develop specialized agents for each asset class to handle their unique characteristics.
*   **Tax Optimization:**
    *   Incorporate tax-aware investment strategies and advice.
    *   Provide guidance on tax-loss harvesting and other tax optimization techniques.
*   **Retirement Planning:**
    *   Offer dedicated tools and advice for retirement planning, including simulations of different scenarios.
*   **Educational Resources:**
    *   Provide educational resources (articles, tutorials, videos) to help users understand financial concepts and make informed decisions.

### Advanced Features

*   **Behavioral Finance Integration:**
    *   Account for behavioral biases in decision-making (e.g., loss aversion, herding behavior) and provide personalized guidance to mitigate them.
*   **Portfolio Rebalancing:**
    *   Automatically rebalance portfolios to maintain desired asset allocations over time.
*   **Stress Testing:**
    *   Conduct stress tests on portfolios to assess their resilience to adverse market events.
*   **Explainable AI (XAI):**
    *   Enhance the explainability agent to provide more detailed and transparent explanations of the reasoning behind investment decisions, using techniques like LIME or SHAP.
*   **Ethical and Responsible AI:**
    *   Implement safeguards to prevent discriminatory or biased outcomes in financial advice.
    *   Ensure transparency and accountability in the system's decision-making processes by documenting the data and logic used.

### Scalability and Performance

*   **Distributed Architecture:**
    *   Design a scalable architecture (e.g., using microservices or serverless functions) to handle a large number of users and data sources efficiently.
*   **Optimized Data Processing:**
    *   Explore and implement techniques to optimize data processing and reduce computational costs.
*   **Parallel Computing:**
    *   Leverage parallel computing (e.g., using libraries like Dask or Ray) to speed up computationally intensive tasks like model training and backtesting.

## Contributing

Contributions are welcome! Please feel free to open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the `LICENSE.md` file for details.

## Disclaimer

This project is a prototype and should not be used for actual financial decision-making. It is intended for educational and demonstration purposes only. Always consult with a qualified financial advisor before making any investment decisions.





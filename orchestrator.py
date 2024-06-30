import asyncio
from autogen.agentchat import ConversableAgent, GroupChat, GroupChatManager
from autogen.agentchat.contrib.gpt_assistant_agent import GPTAssistantAgent
from autogen.agentchat.memory import ConversationSummaryMemory
from autogen.agentchat.llm_wrapper import OpenAIWrapper
from config import OPENAI_API_KEY
from user_interaction_autogen import get_user_proxy_agent
from data_collection import stock_data_agent, news_data_agent, reports_data_agent
from sentiment_analysis import sentiment_analysis_tool
from strategy_generation import strategy_generation_tool
from advisory import advice_tool, market_analysis_tool, industry_trends_tool, financial_ratios_tool, portfolio_management_tool
from portfolio_optimization import portfolio_optimization_tool
from risk_assessment import risk_assessment_tool
from trading import trading_tool
from explainability import explainability_tool

# LLM wrapper and configuration
llm_wrapper = OpenAIWrapper(
    model="gpt-3.5-turbo-0613",
    api_key=OPENAI_API_KEY,
    temperature=0.7,  
)

# AutoGen agents
user_proxy_agent = get_user_proxy_agent()

assistant_agent = GPTAssistantAgent(
    name="FinancialAdvisorAssistant",
    llm_wrapper=llm_wrapper,
    tools=[
        stock_data_tool, news_data_tool, reports_data_tool, 
        sentiment_analysis_tool, strategy_generation_tool, advice_tool,
        market_analysis_tool, industry_trends_tool, financial_ratios_tool, 
        portfolio_management_tool, portfolio_optimization_tool, risk_assessment_tool,
        trading_tool, explainability_tool
    ],
)

# Orchestration
async def orchestrate():
    groupchat = GroupChat(
        agents=[user_proxy_agent, assistant_agent],
        messages=[],
        max_round=20,
    )
    manager = GroupChatManager(groupchat=groupchat, llm_wrapper=llm_wrapper)

    # Start the chat
    await manager.start_chat()

if __name__ == "__main__":
    asyncio.run(orchestrate())

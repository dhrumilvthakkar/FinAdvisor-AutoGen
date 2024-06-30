from llama_index.agent.openai import OpenAIAgent
from llama_index.llms.openai import OpenAI
from llama_index.core.tools import FunctionTool
from config import OPENAI_API_KEY


llm = OpenAI(model="gpt-3.5-turbo-0613", api_key=OPENAI_API_KEY)


def explain_strategy(investment_strategy):
    agent = OpenAIAgent.from_tools([], llm=llm, verbose=True)
    prompt = f"Explain the rationale behind the investment strategy: {investment_strategy}"
    response = agent.chat(prompt)
    return response.response


explainability_tool = FunctionTool.from_defaults(explain_strategy, name="ExplainabilityTool", description="Explain the investment strategy")

from autogen.agentchat.contrib.user_proxy_agent import UserProxyAgent

def get_user_proxy_agent():
    return UserProxyAgent(
        name="User",
        system_message="You are a user seeking financial advice. Please provide your information and preferences."
    )

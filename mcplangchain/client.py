from langchain_mcp_adapters.client import MultiServerMCPClient
from langchain.agents import create_agent

from dotenv import load_dotenv
load_dotenv()

import asyncio

async def main():
    client = MultiServerMCPClient(
        {
            "math":{
                "command": "python",
                "args": ["mathserver.py"],
                "transport": "stdio",
            },
            "weather": {
                "url": "http://127.0.0.1:8000/mcp",
                "transport": "streamable_http",
            }
        }
    )

    import os
    os.environ["OPENAI_API_KEY"] = os.getenv("OPENAI_API_KEY")

    tools = await client.get_tools()
    agent = create_agent(
        model= "openai:gpt-5.4-mini",
        tools= tools
    )


    math_response = await agent.ainvoke(
        {"messages": [{"role":"user", "content":"what is (3 + 5) x 10 and give reasoning?"}]}
    )

    print("Math response: ", math_response["messages"][-1].content)

    weather_response = await agent.ainvoke(
        {"messages": [{"role":"user", "content":"summarize the weather in chennai, bengaluru, delhi and london?"}]}
    )
    
    print("Weather response: ", weather_response["messages"][-1].content)

asyncio.run(main())
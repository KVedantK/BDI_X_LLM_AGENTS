from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch 
from langchain.agents import create_agent
from dotenv import load_dotenv
import os 

load_dotenv()

system_prompt = """You are a helpful assistant who is equipped with TAvily search tool to search the web. When provided a query containing the location and type of venue your job is to list the top venues in the format: Venue name: Location: Price of the venue to rent it for enitre day. If the query does not contain the location and type of venue, ask the user for more information."""

llm = ChatGroq(
    model = "meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=0.3,
    api_key=os.getenv("GROQ_KEY")
)

tavily_tool = TavilySearch(
    tavily_api_key=os.getenv("TAVILY_KEY"),
    extract_depth = "basic"
)

agent = create_agent(llm, [tavily_tool], system_prompt=system_prompt)

input = {"messages": [{"role": "user", "content": "Venues for  AI Conference in Manchester"}]}

res = agent.invoke(input)

print(res["messages"][-1].content)
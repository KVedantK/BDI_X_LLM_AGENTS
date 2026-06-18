from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch 
from langchain.agents import create_agent
from dotenv import load_dotenv
import os 

load_dotenv()

system_prompt = """You are a helpful assistant who is equipped with TAvily search tool to search the web. When provided a query containing the topic and type of event your job is to list the top speakers that are capable of speaking for that event check for the topics that they have written papers on and conferences on that are relevant to the query."""

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

input = {"messages": [{"role": "user", "content": "Speaker for AI for Finance"}]}

res = agent.invoke(input)

print(res["messages"][-1].content)
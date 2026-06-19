from langchain_groq import ChatGroq
from langchain_tavily import TavilySearch 
from langchain.agents import create_agent
from dotenv import load_dotenv
import os 
import json
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
load_dotenv()


Model_openai = ChatOpenAI(
    base_url="https://router.huggingface.co/v1",
    api_key=os.getenv("HF_KEY"),
    model="meta-llama/Llama-3.1-8B-Instruct:novita"
)

class Venues(BaseModel):
    venue: dict = Field(default={}, description="The dictionary of the venues.")

with open("/Users/vedant/Documents/BDI_X_LLM_AGENTS/beliefs/permanent.json") as f:
    beliefs = json.load(f)
    event_name = beliefs["event"]["name"]
    event_location = beliefs["event"]["location"]
    event_duration = beliefs["event"]["duration_days"]
    event_attendees = beliefs["event"]["expected_attendees"]

    budget = beliefs["budget"]["total"]
    venue_budget = beliefs["budget"]["allocations"]["venue"]
    speaker_budget = beliefs["budget"]["allocations"]["speaker"]
    food_budget = beliefs["budget"]["allocations"]["food"]
    logistics_budget = beliefs["budget"]["allocations"]["logistics"]




system_prompt = """
You are a venue search assistant.

Use Tavily to search for venues, with the provided constraints of the user.

After searching, respond ONLY with valid JSON.

Example:

{
  "venues": [
    {
      "name": "...",
      "location": "...",
      "price_per_day": 10000,
      "capacity": 300
    }
  ]
}"""

llm = ChatGroq(
    model = "meta-llama/llama-4-scout-17b-16e-instruct",
    temperature=0.3,
    api_key=os.getenv("GROQ_KEY")
)


tavily_tool = TavilySearch(
    tavily_api_key=os.getenv("TAVILY_KEY"),
    extract_depth = "basic"
)

agent = create_agent(Model_openai, [tavily_tool], system_prompt=system_prompt)

input = {"messages": [{"role": "user", "content": f"Venue for {event_name} in {event_location} for {event_duration} days with expected attendees of {event_attendees}. Budget allocated for venue is {venue_budget}."}]}

res = agent.invoke(input)
print(res)
cleaned = Venues.model_validate_json(res["messages"])
print(cleaned)
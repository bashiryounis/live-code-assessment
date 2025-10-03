from typing import Dict, Any
from retriever import retriever
from langchain_core.prompts import PromptTemplate

PROMPT = """
Find recent tweets about {topic} from {location} written in {language}.
"""

class FakeAI:
    def __init__(self):
        print("Initializing FakeAI...")

    # TODO: Uuse the retriever to get the top 1 tweet and it belongs to which author (use the retriever.py file)
    # Use this function in the generate_response function after injecting the keys from the context into the PROMPT
    # the query parameter is the string after injecting the keys from the context into the PROMPT
    async def __retrieve(self, query: str) -> Dict[str, Any]:
        retriever = retriever.as_retriever(search_type="mmr", search_kwargs={"k": 1})
        docs =retriever.invoke(query)
        return docs

    # TODO: Inject the keys from the context into the PROMPT
    async def generate_response(self, context: Dict[str, Any]) -> Dict[str, Any]: 
        prompt= PromptTemplate.from_template(PROMPT)
        formatted_prompt = prompt.invoke({"topic": context["topic"], "location": context["location"], "language":context["language"]})
        return await self.__retrieve(formatted_prompt)
    
    


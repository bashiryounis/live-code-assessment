from typing import Dict, Any

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
        # Write code here
        return {"tweet": "fake tweet", "author": {"name": "John Doe", "email": "john@example.com"}}

    # TODO: Inject the keys from the context into the PROMPT
    async def generate_response(self, context: Dict[str, Any]) -> Dict[str, Any]: 
        # Write code here
        return await self.__retrieve("prompt with injected keys")
    
    


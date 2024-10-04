# from .config import API_KEY
from groq import Groq

class LLM:
    def __init__(self, api_key : str = None)  -> None:
        self.client = Groq(api_key="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")

    def call(self, list_of_messages : list) -> str:
        '''
        list of system and user prompts

        Call the LLM, do what you want, only return text

        return str

        '''
        
        chat_completion = self.client.chat.completions.create(messages=list_of_messages, model="llama3-8b-8192")
        
        return chat_completion.choices[0].message.content

llm = LLM()
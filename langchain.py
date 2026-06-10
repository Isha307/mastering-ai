from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
import os

load_dotenv()  # Load environment variables from .env file
llm = ChatGroq(
    model="llama-3.1-8b-instant", 
    temperature=0.5,
    api_key=os.getenv("API_KEY")
    )

response = llm.invoke("What is Docker in one sentence?")
print(response.content)

# {topic} will be replaced when we run the chain
prompt = ChatPromptTemplate.from_template(
    "Explain {topic} in simple terms, in one short paragraph."
)

# pulls the text out of the response object
parser = StrOutputParser()

# wire all three steps together
chain = prompt | llm | parser

# run it — fill in {topic} here
result = chain.invoke({"topic": "how Docker containers work"})
print(result)
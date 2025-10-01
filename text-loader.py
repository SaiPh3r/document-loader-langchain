from langchain_community.document_loaders import TextLoader
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.output_parsers import StrOutputParser
from langchain.prompts import PromptTemplate
from dotenv import load_dotenv
load_dotenv()

loader = TextLoader('requirements.txt')
model = ChatGoogleGenerativeAI(model="models/gemini-2.5-flash") 
promt = PromptTemplate(
    template='write a basic information about following requirement{req}' , 
    input_variables=['req']
)

parser = StrOutputParser()

doc = loader.load()

chain = promt | model | parser

print(doc[0].page_content)

result = chain.invoke({'req':doc[0].page_content})
print(result)


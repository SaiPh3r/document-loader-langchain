from langchain_text_splitters import CharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader("dummy.pdf")
document = loader.load()

splitter = CharacterTextSplitter(
    chunk_size=100, 
    chunk_overlap=0
)

result = splitter.split_documents(document)
print(result[0].page_content)

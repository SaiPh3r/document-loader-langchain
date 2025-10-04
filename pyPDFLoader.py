from langchain_community.document_loaders import PyPDFLoader

loader = PyPDFLoader('dummy.pdf')

doc = loader.load()

print(doc[0].page_content)
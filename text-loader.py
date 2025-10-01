from langchain_community.document_loaders import TextLoader

loader = TextLoader('requirements.txt')

doc = loader.load()

print(type(doc))

print(doc[0])

print(type(doc[0]))
from langchain_community.document_loaders import CSVLoader

loader=CSVLoader('Doc_Loaders/books/fmnist_small.csv')

docs=loader.load()

print(docs[1].metadata)
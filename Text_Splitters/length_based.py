"""
Example script demonstrating how to use CharacterTextSplitter from LangChain
to split a loaded PDF document into smaller chunks based on a fixed character length.
"""
from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import CharacterTextSplitter

# Load the PDF document
loader = PyPDFLoader('Doc_Loaders/Bisakh Patra Resume ML.pdf')
docs = loader.load()

# Initialize the CharacterTextSplitter
# chunk_size: Maximum number of characters in a single chunk
# chunk_overlap: Number of overlapping characters between chunks
# separator: The character used to split the text
splitter = CharacterTextSplitter(
    chunk_size=100,
    chunk_overlap=0,
    separator=''
)

# Split the loaded document into smaller chunks
res = splitter.split_documents(docs)

# Print the content of the first chunk
print(res[0].page_content)
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel
import grandalf

load_dotenv()

model1=ChatHuggingFace(llm=HuggingFaceEndpoint(repo_id="Qwen/Qwen2.5-72B-Instruct",
    task="text-generation"))

model2=GoogleGenerativeAI(model="gemini-2.5-flash")

parser=StrOutputParser()

prompt1=PromptTemplate(
    template='write a detailed report on {text}.\n',
    input_variables=['text']
)

prompt2=PromptTemplate(
    template='write a 5 quiz questions on the following {text}.\n',
    input_variables=['text']
)

prompt3=PromptTemplate(
    template='merge the provided reports and questions in a single document.\n report -> {report}, questions -> {questions}',
    input_variables=['report', 'questions']
)

parallel_chain=RunnableParallel(
    report=prompt1 | model1 | parser,
    questions=prompt2 | model2 | parser
)

merged_chain=prompt3 | model1 | parser

chain=parallel_chain | merged_chain

txt = """Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support
 vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result=chain.invoke({'text': txt})

print(result)

chain.get_graph().print_ascii()
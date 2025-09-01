from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from Vector import retriever

model = OllamaLLM(model="llama3.2")

template = """
You are an expert in answering questions about a Pizza  restaurant.

Here are some relevant rewiews: {rewiews}

Here are some questions to answer: {questions}
"""
prompt  = ChatPromptTemplate.from_template(template)
chain = prompt | model
while True:
    print("\n\n===================================")
    question = input('Ask your question about a pizza restaurent (q to quit): ')
    print("\n\n")
    if question.lower() == 'q':
        break
    rewiews = retriever.invoke(question)
    result = chain.invoke({"rewiews": [], "questions": question})
    print(result)

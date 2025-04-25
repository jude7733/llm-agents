from langchain_ollama import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate

template = """
    Answer the question below.
    
    Here is the conversation history: {context}

    Question: {question}

    Answer:
    """


model = OllamaLLM(model="llama-3b-npu", temperature=0.1)
prompt = ChatPromptTemplate.from_template(template)
chain = prompt | model


def handle_conversation():
    context = ""
    print("Welcome to the conversation agent! Type 'exit' to end the conversation.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            break
        response = chain.invoke({"context": context, "question": user_input})
        context += f"\nUser: {user_input}\nAssistant: {response}\n"
        print(f"Assistant: {response}")


if __name__ == "__main__":
    handle_conversation()

from dotenv import load_dotenv

import streamlit as st
from langchain_openai import ChatOpenAI, OpenAIEmbeddings
from langchain_community.vectorstores.faiss import FAISS
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains.retrieval import create_retrieval_chain
from langchain_core.messages import HumanMessage, AIMessage


load_dotenv()


def get_vectordb(vector_path):
    embedder = OpenAIEmbeddings()
    vector_store = FAISS.load_local(vector_path, embedder, index_name="index", allow_dangerous_deserialization=True)
    return vector_store


def create_chain(vector_db):
    model = ChatOpenAI(model="gpt-4o" , temperature=0.5) # set the model you are wanting to use

    prompt = ChatPromptTemplate.from_messages([
        ('system', 'You are a helpful assistant for BRAC University students. Answer their questions according to the given context {context}.'),
        MessagesPlaceholder('chat_history'),
        ('human', 'Gives greetings'),
        ('system', 'Hi! I am BOKU. I am a chat assistant designed for the students of BRAC University. How may I help you?'),
        ('human', '{input}')
    ])

    chain = create_stuff_documents_chain(
        prompt=prompt,
        llm=model
    )

    retriever = vector_db.as_retriever(search_kwargs={'k': 20}) #set the parameter according to your need
    retrieval_chain = create_retrieval_chain(retriever, chain)

    return retrieval_chain

def process_chat(chain, query, chat_history):
    response = chain.invoke({
        'input': query,
        'chat_history': chat_history
    })
    return response['answer']


vector_db = get_vectordb(vector_path = 'Enter you vector database path here')
chain = create_chain(vector_db)

def main():
    st.set_page_config(page_title="Chat With BOKU", page_icon=":goat:")
    st.header("Chat With BOKU :goat:")

    # Initialize session state for chat history if not already present
    if 'chat_history' not in st.session_state:
        st.session_state['chat_history'] = []

    # Use a form to handle input submission
    with st.form(key='user_input_form', clear_on_submit=True):
        user_input = st.text_input("Ask BOKU anything:", placeholder="Type your message and press Enter")
        submit_button = st.form_submit_button(label='Send')

    # Process the user query when the form is submitted
    if submit_button and user_input:
        with st.spinner('Boku is thinking...'):
            # Add user input to chat history before processing
            st.session_state['chat_history'].append(HumanMessage(content=user_input))

            # Process the chat and get the response
            ai_output = process_chat(chain, user_input, st.session_state['chat_history'])

            # Add the assistant's response to the chat history
            st.session_state['chat_history'].append(AIMessage(content=ai_output))

    # Display chat messages using Streamlit chat_message with newest messages at the top
    for msg in reversed(st.session_state['chat_history']):
        if isinstance(msg, HumanMessage):
            st.chat_message("user", avatar="🧑").markdown(f"**You:** {msg.content}")
        else:
            st.chat_message("assistant", avatar="🤖").markdown(f"**BOKU:** {msg.content}")

if __name__ == '__main__':
    main()

# BokuBot
BOKU is a chatbot application designed for BRAC University students to get help and information using RAG. It leverages Streamlit for the web interface and LangChain for natural language processing and retrieval. This chatbot is powered by GPT-4, a state-of-the-art language model developed by OpenAI.

## Features

- **Interactive Chat**: Engage in a conversation with BOKU, the chatbot assistant.
- **Contextual Assistance**: BOKU provides answers based on a preloaded vector database. The vector database is built on the contents of the BRACU website. I collected the individual webpage urls from the sitemap of the website which are provided as a list in the [urls_list.py] file.
- **History Tracking**: Maintains chat history for a coherent conversation experience.

## Requirements

- Python 3.8+
- Required libraries:
  - `streamlit`
  - `langchain-openai`
  - `langchain-community`
  - `langchain-core`
  - `python-dotenv`
  - `faiss-cpu` or `faiss-gpu` (depending on your setup)

## Installation

1. Clone the repository:
  git clone https://github.com/ProfCode101/BokuBot.git

2. Install the required Python packages:
   pip install -r requirements.txt

3. Create a .env file in the root directory and add your environment variables (e.g., API keys) required by LangChain and OpenAI.
   
## Configuration
 1. While creating the vector store you can use AI1SemanticTextSpliter if you have the option to buy tokens. It will
    give you a better test result than RecursiveCharacterTextSplitter in this case.
 2. Vector Database Path: Update the vector_path variable in the main function with the path to your preloaded vector database.
  vector_db = get_vectordb(vector_path='path/to/your/vector/database')
    ##### Here you can use the [create_vector_store.py] file to create your own database or you can download the database         that I have already created from https://drive.google.com/drive/folders/1BtStFttBSCjCkWNqvePwuUxdqIzx-02w?usp=drive_link. I have used WebBaseLoader by langchain. You can use FireCrawlLoader as due to the anti-scraping-crawling security policy WebBaseLoader cannot collect the email ID of the respected faculties. It is even better if you can build your         custom web crawler which will be able to crawl and collect managing the security restrictions. I'll be uploading a           custom web crawler logic soon.
 3. Chat Model: You can adjust the model parameters in the create_chain function if needed.
 4. For additional information go to https://python.langchain.com/v0.1/docs/use_cases/chatbots/

## Running the Application
1. To start the chat application, run the following command:
      streamlit run app.py
      Replace app.py with the name of your Python script if it is different.

## Usage
 1. Open the web application in your browser.
 2. Type your question or message into the input box and press "Send".
 3. Boku will respond with an answer based on the vector database and its programming.

## Contributing
If you'd like to contribute to this project, please fork the repository and submit a pull request. For bug reports or feature requests, open an issue on GitHub.

## Contact
For any questions or support, please contact tasnimdrmc6461@gmail.com .
  

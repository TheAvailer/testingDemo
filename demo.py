import streamlit as st
import dotenv
import tabulate
from langchain_experimental.agents import create_pandas_dataframe_agent
import pandas as pd
from langchain_openai import ChatOpenAI


def main():
    
    dotenv.load_dotenv()

    st.set_page_config(page_title="Dataset chatbot demo")
    st.header("Ask about your dataset")
    dataset = st.file_uploader("Upload dataset here as csv format", type="csv")

    if dataset is not None:
        question_input = st.text_input("Input question about your dataset") 
        llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0)
        #llm = ChatOpenAI(model="gpt-4", temperature=0)
        df = pd.read_csv(dataset)
        #agent = create_csv_agent(large_lang_model, dataset, verbose=True)   #Verbose set to true for debugging
        agent = create_pandas_dataframe_agent(llm, df, agent_type="openai-tools", verbose=True)
        #agent = langchain_experimental.create_pandas_dataframe_agent(llm, df, agent_type="openai-tools", verbose=True)
        #agent = langchain.create_pandas_dataframe_agent(llm, df, agent_type="openai-tools", verbose=True, a)


        if question_input is not None and question_input != "":
            output = agent.invoke(
                {
                    #"input": "What is the ratio of males to females within this dataset ?"
                    "input" : question_input
                }
            )
            
            st.write(output)





if __name__ == "__main__":
    main()
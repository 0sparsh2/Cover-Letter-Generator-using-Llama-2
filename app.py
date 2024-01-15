import streamlit as st
from langchain.prompts import PromptTemplate

# CTransformers for ggml models
from langchain.llms import CTransformers

## Function to get response from Llama-2 model


def get_llama_response(job_title, job_description, role_type):

    ## Llama2 model
    llm = CTransformers(model="/Users/sparshnagpal/Desktop/projects/models/llama-2-7b.ggmlv3.q8_0.bin",
                        model_type='llama',
                        config={'max_new_tokens':256, 'temperature':0.1})
    
    ## Prompt Template

    template="""
    Write a cover letter for a {role_type} position for the job title : {job_title}. 
    The job description is "{job_description}"
    """

    prompt = PromptTemplate(input_variables=['role_type','job_title','num_words'],
                                             template=template)
    
    ## Generate the response from llama-2 model
    response = llm(prompt.format(role_type=role_type, job_title=job_title, job_description=job_description))

    print(response)







st.set_page_config(
    page_title="Generate Blogs",
    layout="centered",
    initial_sidebar_state="collapsed"
)

st.header("Generate Cover Letter")

job_description = st.text_input("Input Job Description")

## Creating two more columns for additional 2 fields

col1, col2 = st.columns([5,5])

with col1:
    job_title = st.text_input("Enter the Job Title")

with col2:
    role_type = st.selectbox("Applying for", 
                              ("Part-time","Internship","Full-time"), index=0)
    
submit = st.button("Generate")

## Final Response
if submit:
    st.write(get_llama_response(job_description, job_title, role_type))


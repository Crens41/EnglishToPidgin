import os
import openai 
import streamlit as st
from langchain import PromptTemplate
from langchain.llms import OpenAI
from langchain_community.llms import OpenAI

openai.api_key =os.getenv("OPENAI_API_KEY")


template = """
    Below is a sentence that needs to be changed to Nigerian Pidgin language.
    Your goal is to:
    - Properly format the sentence 
    - Convert the input sentence to a specified tone
    - Convert the input text to a specified dialect

    Here are some examples different Tones:
    - Formal: We went to Lagos for the weekend. We have a lot of things to tell
    - Informal: Went to Lagos for the weekend. Lots to tell you.

    Here are some examples of words in different dialects:
    - America English: French Fries, cotton candy, apartment, garbage, cookie, green.
    - British English: candyfloss, flag, rubbish, biscuit, green fingers.
    - Nigeria Pidgin: Oboy, How you de, wetin happen, I go beat you o, You de craze?, i no go fit come again, You de find my trouble o.

    Below is the sentence, tone, and dialect:
    TONE: {tone}
    DIALECT: {dialect}
    SENTENCE: {sentence}

    YOUR RESPONSE:
"""

prompt = PromptTemplate(
    input_variables = ["tone", "dialect", "sentence"],
    template=template,
)

def load_LLM():
    """Logic for loading the chain you want to use should go here."""
    llm = OpenAI(temperature = 0.5)
    return llm

llm = load_LLM()

st.set_page_config(page_title="English To Pidgin",page_icon=":robot:")
st.header("English To Pidgin")

col1, col2 = st.columns(2)

with col1:
    st.markdown("In Nigeria, the formal language is English Language(British and American English). There are diverse dialects in Nigeria, of which the majors are Igbo, Hausa, Yoruba and Efik. However, there is an informal language used among the Nigerians. This is called the Nigerian Pidgin. This app should change any sentence from English to Nigerian Pidgin for anyone lookikng forward to learning the Nigerian Pidgin.")
with col2:
    st.image(image='translate-from-any-language-to-nigerian-pidgin-and-vice-versa.png', width=500, caption='Converting from English to pidgin')

st.markdown("## Enter Your Sentence To Change To Nigerian Pidgin")

col1, col2 = st.columns(2)
with col1:
    option_tone = st.selectbox(
        'Which tone would you like your sentence to have?',
        ('Formal', 'Informal')
    )

with col2:
    option_dialect = st.selectbox(
        'Which English Dialect would you like?',
        ( 'British English', 'Nigerian Pidgin')
    )
def get_text():
    input_text = st.text_area(label="", placeholder="Your Sentence...", key="sentence_input")
    return input_text

sentence_input = get_text()

st.markdown("### Your Converted Sentence:")

if sentence_input:
    prompt_with_sentence = prompt.format(tone=option_tone, dialect=option_dialect, sentence=sentence_input)

    formatted_sentence = llm(prompt_with_sentence)
    
    st.write(formatted_sentence)







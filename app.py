#python 3.9
import streamlit as st
from transformers import AutoModelForSeq2SeqLM, AutoTokenizer
#pip install torch
#pip install sentencepiece


# Load the fine-tuned model
model = AutoModelForSeq2SeqLM.from_pretrained("model +token")
tokenizer = AutoTokenizer.from_pretrained("model +token")

# Define a function for inference
def Generate_code(text):
    # Tokenize input
    inputs = tokenizer(text, return_tensors="pt", max_length=64, truncation=True)
    # Generate translation
    outputs = model.generate(inputs["input_ids"], max_length=100, num_beams=4, early_stopping=True)
    # Decode the translation
    code = tokenizer.decode(outputs[0], skip_special_tokens=True)
    return code

# Streamlit app
st.title('Code Generator ChatBot System')

# Input field for user query
query = st.text_input("Turn your ideas into code through conversation....")

# Button to trigger code generation
if st.button("Generate Code"):
    if query:
        code = Generate_code(query)
        st.subheader("Generated Code:")
        st.code(code, language="python")
    else:
        st.warning("Please enter a query to generate code.")




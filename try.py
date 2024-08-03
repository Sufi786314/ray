import streamlit as st
# from streamlit_exeras.add_vertical_space import add_vertical_space
from pyPDF2 import PdfReader
with st.sidebar:
    st.title('Crown')
    st.markdown('''
    ## About
    This is an LLM-powered Chat-bot
    Which reads the pdf and 
    Analyze is it.
                
                ''')
   

def main():
    st.header("Chat with Pdf Chat bot")

    pdf = st.file_uploader("Upload your pdf",type='pdf')

if __name__ == '__main__':
    main()
import myVoiceTestForStreamlitFrontend
import streamlit as st

import os
import google.generativeai as genai
from dotenv import load_dotenv, find_dotenv

if __name__ == '__main__':
    load_dotenv(find_dotenv(), override=True)
    genai.configure(api_key=os.environ.get('GOOGLE_API_KEY'))

# HEADER FOR MY PROTOTYPES ON STREAMLIT

col1, col2 = st.columns([0.25,0.75])

with col1:

    st.image('hair.png')
    st.subheader('Voice to TextPrompt :stars:')

# UI FOR GETTING VOICE INPUT
    
col3, col4 = st.columns([0.5,0.5])

with col3:

    if st.button('Start Voice'):
        with st.spinner('Tell me a prompt'):
        # st.write('start')
            myVoiceTestForStreamlitFrontend.run_transcriber()

with col4: 
    
    if st.button('End Voice'):
        # st.write('End')
        myVoiceTestForStreamlitFrontend.close_transcriber()

# SHOW THE COMPLETE VOICE PROMPT

prompt = myVoiceTestForStreamlitFrontend.prompt_from_voice()
st.write(prompt)

#GET RESPONSE FROM GEMINI

if prompt:
    model = genai.GenerativeModel('gemini-pro')
    response = model.generate_content([prompt])

    st.text_area('Gemini Response:', value=response.text)
    

#but now i've added this new stuff down here ... what will happen now? 


#but now also this though!


# and now this change made on a branch i created on desktop
import os
import streamlit as st
import assemblyai as aai

from dotenv import load_dotenv, find_dotenv

import assemblyai as aai

aai.settings.api_key = "fc95022e989e4b4eb1806b448e18ffca"

sentence = ''

def on_open(session_opened: aai.RealtimeSessionOpened):
    print("Session ID:", session_opened.session_id) #yyy

def save_to_prompt(phrase):
    global sentence 
    sentence += phrase

def on_data(transcript: aai.RealtimeTranscript):
    if not transcript.text:
        return

    if isinstance(transcript, aai.RealtimeFinalTranscript):
        print(transcript.text, end="\r\n")
        save_to_prompt(transcript.text)
    #else:
       # print(transcript.text, end="\r")


def on_error(error: aai.RealtimeError):
    print("An error occured:", error) #yyy


def on_close():
    print("Closing Session") #yyy


transcriber = aai.RealtimeTranscriber(
    sample_rate=16_000,
    on_data=on_data,
    on_error=on_error,
    on_open=on_open,
    on_close=on_close,
)


# col1, col2 = st.columns([0.25,0.75])

# with col1:

#     st.image('..\hair.png')
#     st.subheader('Talking with an Image :stars:')

def run_transcriber():

    transcriber.connect()

    microphone_stream = aai.extras.MicrophoneStream(sample_rate=16_000)
    transcriber.stream(microphone_stream)

def close_transcriber():

    transcriber.close()

if __name__ == '__main__':
    run_transcriber()
    close_transcriber()

def prompt_from_voice():
    return(sentence)

print(sentence)



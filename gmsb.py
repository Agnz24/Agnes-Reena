import pickle
from pathlib import Path
import streamlit as st
import sys
import requests
import streamlit as st
from streamlit_chat import message as st_message
from transformers import BlenderbotTokenizer
from transformers import BlenderbotForConditionalGeneration

from streamlit_lottie import st_lottie

import openai
import gradio


import os



import streamlit_authenticator as stauth

#openai.api_key = "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"
def load_lottieurl(url):
    r = requests.get(url)
    if r.status_code != 200:
        return None
    return r.json()
lottie_coding=load_lottieurl("https://assets4.lottiefiles.com/packages/lf20_H3shI6.json")
l_c=load_lottieurl("https://assets2.lottiefiles.com/packages/lf20_EHugAD.json")

st.set_page_config(page_title="GuideMySkinBot",layout="wide")
with st.container():
    st.subheader("GuideMySkinBot helps you to find the correct skincare routine as per your skin concern.")
    st.title(" GuideMySkinBot")
    st.write(" Guide My skinbot is all about Delivering skincare routine for all ages and also including from different skin types,Cost effective andreliable solutions.")
    st.write("Also provides you with trust-worthy product recommendations")
with st.container():
    st.write("---")
    
    st.header("Services Provided")
    st.write("##")
    st.write("""1.REGULAR SKINCARE ROUTINE\n
                    Get to know the basic skin routine.\n2.CUSTOMIZED SKINCARE ROUTINE \n
                            (i).Suggests skincare routine according to user concern\n\t(ii).There is product suggestion for each skin concern.
                    
                    """)
with st.container():
    st.write("---")
    
    
    st.header("Regular Skincare Routine Suggestions")
    image_column, text_column = st.columns((2, 1))
    with image_column:
    
        st.write("##")
        st.write("[NormalSkin >](https://www.healthline.com/health/beauty-skincare/the-ultimate-skin-care-routine-for-normal-skin)")
        st.write("[Oily Skin>](https://www.healthline.com/health/beauty-skin-care/skin-care-routine-for-oily-skin)")
        st.write("[Dry skin>](https://www.healthline.com/health/beauty-skin-care/skin-care-routine-for-dry-skin)")
        st.write("[Acne-Prone Skin>](https://www.healthline.com/health/beauty-skin-care/acne-prone-skin)")
        st.write("[Combination skin >](https://www.healthline.com/health/beauty-skin-care/skin-care-routine-for-combination-skin#routine)")
        st.write("[Video recommended >](https://youtu.be/vpB0u6zze-0)")
    with text_column:
        st_lottie(lottie_coding,height=300,key="skincare") 

    
def local_css(file_name):
    with open(file_name) as f:
        st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)


local_css("style.css")
with st.container():
    st.write("---")
    st.header("To get Customized Skincare routine!")
    st.write("##")

    # Documention: https://formsubmit.co/ !!! CHANGE EMAIL ADDRESS !!!
    contact_form = """
    <form action="https://formsubmit.co/agnzreenawin6@gmail.com" method="POST">
        <input type="hidden" name="_captcha" value="false">
        <input type="text" name="name" placeholder="Your name" required>
        <input type="email" name="email" placeholder="Your email" required>
        <textarea name="message" placeholder="Send your skin concern" required></textarea>
        <button type="submit">Send</button>
    </form>
    """
    left_column, right_column = st.columns(2)
    with left_column:
        st.markdown(contact_form, unsafe_allow_html=True)
    with right_column:
        st.empty()
            
            
with st.container():
    st.write("---")
    left_column, right_column = st.columns(2)
    with left_column:
        st.header("Customized Skincare Routine")
        st.write("##")
        st_lottie(l_c,height=300,key="skin") 

        
    with right_column:
        @st.cache_resource
        def get_models():
            # it may be necessary for other frameworks to cache the model
            # seems pytorch keeps an internal state of the conversation
            model_name = "facebook/blenderbot-400M-distill"
            tokenizer = BlenderbotTokenizer.from_pretrained(model_name)
            model = BlenderbotForConditionalGeneration.from_pretrained(model_name)
            return tokenizer, model


        if "history" not in st.session_state:
            st.session_state.history = []

        st.title("Welcome to GuideMySkinBot")


        def generate_answer():
            tokenizer, model = get_models()
            user_message = st.session_state.input_text
            inputs = tokenizer(st.session_state.input_text, return_tensors="pt")
            result = model.generate(**inputs)
            message_bot = tokenizer.decode(
                result[0], skip_special_tokens=True
            )  # .replace("<s>", "").replace("</s>", "")

            st.session_state.history.append({"message": user_message, "is_user": True})
            st.session_state.history.append({"message": message_bot, "is_user": False})


        st.text_input("Talk to the bot", key="input_text", on_change=generate_answer)

        for i, chat in enumerate(st.session_state.history):
            st_message(**chat, key=str(i)) #unpacking

                
            
            




        
            


    

        
    
        
        
    
    

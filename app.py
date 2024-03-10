# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env.

# import streamlit as st
# import os
# import pathlib
# import textwrap
# from PIL import Image
# import google.generativeai as genai

# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Function to load OpenAI model and get respones

# model = genai.GenerativeModel('gemini-pro-vision')

# Q&A Chatbot
#from langchain.llms import OpenAI

# from dotenv import load_dotenv

# load_dotenv()  # take environment variables from .env.

# import streamlit as st
# import os
# import pathlib
# import textwrap
# from PIL import Image


# import google.generativeai as genai


# os.getenv("GOOGLE_API_KEY")
# genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

# ## Function to load OpenAI model and get respones

# def get_gemini_response(input,image,prompt):
#     model = genai.GenerativeModel('gemini-pro-vision')
#     response = model.generate_content([input,image[0],prompt])
#     return response.text
    

# def input_image_setup(uploaded_file):
#     # Check if a file has been uploaded
#     if uploaded_file is not None:
#         # Read the file into bytes
#         bytes_data = uploaded_file.getvalue()

#         image_parts = [
#             {
#                 "mime_type": uploaded_file.type,  # Get the mime type of the uploaded file
#                 "data": bytes_data
#             }
#         ]
#         return image_parts
#     else:
#         raise FileNotFoundError("No file uploaded")


# ##initialize our streamlit app

# st.set_page_config(page_title="Gemini Image Demo")

# st.header("𝙄𝙣𝙫𝙤𝙞𝙘𝙚𝙀𝙭𝙩𝙧𝙖𝙘𝙩𝙤𝙧 𝘼𝙥𝙥𝙡𝙞𝙘𝙖𝙩𝙞𝙤𝙣 ")
# input=st.text_input("Input Prompt: ",key="input")
# submit=st.button("𝘛𝘦𝘭𝘭 𝘮𝘦 𝘢𝘣𝘰𝘶𝘵 𝘵𝘩𝘦 𝘪𝘮𝘢𝘨𝘦")
# uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
# image=""   
# if uploaded_file is not None:
#     image = Image.open(uploaded_file)
#     st.image(image, caption="Uploaded Image.", use_column_width=True)


# # submit=st.button("𝘛𝘦𝘭𝘭 𝘮𝘦 𝘢𝘣𝘰𝘶𝘵 𝘵𝘩𝘦 𝘪𝘮𝘢𝘨𝘦")

# input_prompt = """
#                You are an expert in understanding invoices.
#                You will receive input images as invoices &
#                you will have to answer questions based on the input image
#                """

# ## If ask button is clicked

# if submit:
#     image_data = input_image_setup(uploaded_file)
#     response=get_gemini_response(input_prompt,image_data,input)
#     st.subheader("The Response is")
#     st.write(response)
    
    
# def completion_message():
#     print("Feature completed successfully!")

# # Example usage
#   # Call this when the feature is not implemented yet
# completion_message()  # Call this when the feature is completed
import streamlit as st
from dotenv import load_dotenv
from PIL import Image
import google.generativeai as genai
import os

load_dotenv()  # Load environment variables from .env

genai.configure(api_key=os.getenv("GOOGLE_API_KEY"))

def get_gemini_response(input, image, prompt):
    model = genai.GenerativeModel('gemini-pro-vision')
    response = model.generate_content([input, image[0], prompt])
    return response.text

def input_image_setup(uploaded_file):
    if uploaded_file is not None:
        bytes_data = uploaded_file.getvalue()
        image_parts = [
            {
                "mime_type": uploaded_file.type,
                "data": bytes_data
            }
        ]
        return image_parts
    else:
        raise FileNotFoundError("No file uploaded")

# Initialize Streamlit app
st.set_page_config(page_title="Gemini Image Demo")
st.header("𝘿𝙤𝙘𝙎𝙣𝙖𝙥𝘼𝙣𝙖𝙡𝙯𝙚𝙧 𝘼𝙥𝙥𝙚𝙡𝙞𝙘𝙖𝙩𝙞𝙤𝙣")

input_text = st.text_input("Input Prompt: ", key="input")
submit_button = st.button("𝘛𝘦𝘭𝘭 𝘮𝘦 𝘢𝘣𝘰𝘶𝘵 𝘵𝘩𝘦 𝘪𝘮𝘢𝘨𝘦")
response_placeholder = st.empty()  # Placeholder for the response
uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])
image_upload_notification = st.empty()  # Placeholder for the upload notification
image = ""

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption="Uploaded Image.", use_column_width=True)

    # Display a notification when the file is successfully uploaded
    image_upload_notification.success("File uploaded successfully!")

input_prompt = """
               You are an expert in understanding invoices.
               You will receive input images as invoices &
               you will have to answer questions based on the input image
               """

if submit_button:
    # Process the input and show the response
    image_data = input_image_setup(uploaded_file)
    response = get_gemini_response(input_prompt, image_data, input_text)

    # Display the "This is the response" line below the submit button with each line in bold
    response_lines = response.split('\n')
    response_placeholder.subheader("This is the response:")
    for line in response_lines:
        response_placeholder.markdown(f"**{line}**")

    # Display balloons notification after getting the response
    st.success("Feature completed successfully!")
    st.balloons()

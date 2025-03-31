import streamlit as st

from rag import graph_streamer

IMAGE_ADDRESS = "https://bs-uploads.toptal.io/blackfish-uploads/components/open_graph_image/8957316/og_image/optimized/0919_Machines_and_Trust_Lina_Social-ac9acf8ebc252ec57a9a9014f6be62b2.png"

# title
st.title("BiasReader")

# set the image
st.image(IMAGE_ADDRESS)

from openai import OpenAI

client = OpenAI(api_key=os.environ["OPENAI_API_KEY"])

try:
    response = client.chat.completions.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": "Hello!"}]
    )
    print(response.choices[0].message.content)
except Exception as e:
    print(f"Error: {e}"



# add your topic
user_text = st.text_input("Please Add Your Topic")

if user_text:
    st.subheader("Bias Analysis")
    st.write_stream(graph_streamer(user_text))


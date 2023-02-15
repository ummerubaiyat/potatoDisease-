import streamlit as st
from PIL import Image
import requests
from bs4 import BeautifulSoup


labels = ["Early Blight", "Late Blight", "Healthy"]

 

 

def run():
    st.title("Fruits🍍-Vegetable🍅 Classification")
    img_file = st.file_uploader("Choose an Image", type=["jpg", "png"])
    if img_file is not None:
        img = Image.open(img_file).resize((250, 250))
        st.image(img, use_column_width=False)
        save_image_path = './upload_images/' + img_file.name
        with open(save_image_path, "wb") as f:
            f.write(img_file.getbuffer())

        # if st.button("Predict"):
        if img_file is not None:
            # result = processed_img(save_image_path)
            url = 'http://34.219.140.66:5000/predict'
            form_data = {'file': open(save_image_path, 'rb')}
            resp = requests.post(url, files=form_data)
            resp_dict = resp.json()
            result = resp_dict['prediction']
            print(result)
           


run()

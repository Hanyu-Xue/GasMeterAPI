import sys
import os
base_dir = os.path.dirname(os.path.realpath('__file__'))
import streamlit as st
# To make things easier later, we're also importing numpy and pandas for
# working with sample data.
import numpy as np
import pandas as pd
import time
import GasTemplatesMatching as GM
from PIL import Image

st.title('Gas Meter API v1.0')
image_folder = base_dir+'/Images/'
template_dir = base_dir+'/templates.npy'

def find_images(image_folder):
    images_list = os.listdir(image_folder)
    images_list.sort()
    images_list.remove('.DS_Store')
    return images_list

images_list = find_images(image_folder)

option = st.sidebar.selectbox(
                              'Which image do you want to predict?',
                              images_list)

file_path = image_folder+option

PredictNumber = GM.read_gas_meter(file_path,template_dir)

image = Image.open(file_path)
image = image.convert("RGB")
st.header("Image")
image_slot = st.image(image,caption=option)
image_predict = st.markdown('The number predict: '+ np.array2string(PredictNumber))



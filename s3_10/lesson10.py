import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image



st.title('Stereamlit 超入門')
st.write('Display Image')

text = st.text_input('貴方の趣味は？')
text

condition = st.slider('あなたのコンディションは？',0,100,50)
'コンディション　', condition

"""
option = st.selectbox(
    'あなたの好きな数字を教えてください',
    list(range(1,11))
)

'あなたの好きな数字は、', option, 'です'



if st.checkbox('Show Image'):
    img = Image.open('スクリーンショット_20230105_191620.png')
    st.image(img, caption='sample', use_column_width=True)
"""  
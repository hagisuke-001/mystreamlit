import streamlit as st
import numpy as np
import pandas as pd
from PIL import Image



st.title('Stereamlit 超入門')
st.write('Interactionve Widgets')

text = st.sidebar.text_input('貴方の趣味は？')
condition = st.sidebar.slider('あなたのコンディションは？',0,100,50)
'コンディション　', condition
'あなたの趣味',text

